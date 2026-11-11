# -*- coding: utf-8 -*-
"""
RAG Local Vértice OS (100% local, privado e offline após download inicial do modelo).
Embeddings: sentence-transformers (intfloat/multilingual-e5-small).
Vector store: LanceDB (embarcado, persistente em disco).

Uso:
  python rag_acervo.py index
  python rag_acervo.py index "<PASTA_DO_ACERVO>"
  python rag_acervo.py index <root> --reset
  python rag_acervo.py query "pergunta 1" "pergunta 2" [-f "filtro"] [-k 8] [--curto]
  python rag_acervo.py stats
"""
import sys, os, json, argparse, hashlib, time, re, warnings
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
warnings.filterwarnings("ignore", category=DeprecationWarning)

def _tables(db):
    if hasattr(db, "list_tables"):
        res = db.list_tables()
        names = getattr(res, "tables", res)
        return list(names)
    return list(db.table_names())

BASE       = os.path.dirname(os.path.abspath(__file__))
DB_DIR     = os.path.join(BASE, "lancedb")
MANIFEST   = os.path.join(BASE, "manifest.json")
CONFIG     = os.path.join(BASE, "rag_config.json")
TABLE      = "acervo"
MODEL_NAME = "intfloat/multilingual-e5-small"
CHUNK      = 1200
OVERLAP    = 200
BATCH      = 16

DOC_EXT = {".pdf", ".docx", ".txt", ".md", ".csv", ".xlsx"}
SKIP_EXT = {".exe", ".rar", ".zip", ".7z", ".png", ".jpg", ".jpeg", ".gif",
            ".sfp", ".l", ".re", ".001", ".bak", ".tmp", ".db", ".lnk",
            ".mp4", ".mp3", ".wav", ".mov", ".ttf", ".otf", ".ico"}
SKIP_DIR = re.compile(r"[\\/](_lixo[^\\/]*|quarentena[^\\/]*|_quarentena[^\\/]*|_tmp[^\\/]*|\.git|\.venv|venv|node_modules|lancedb|__pycache__)([\\/]|$)", re.I)

def extract(path, ext):
    try:
        if ext == ".pdf":
            import pdfplumber
            out = []
            with pdfplumber.open(path) as pdf:
                for pg in pdf.pages:
                    t = pg.extract_text() or ""
                    if t.strip(): out.append(t)
            return "\n".join(out)
        if ext == ".docx":
            import docx
            d = docx.Document(path)
            return "\n".join(p.text for p in d.paragraphs if p.text.strip())
        if ext in (".txt", ".md", ".csv"):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        if ext == ".xlsx":
            import openpyxl
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
            out = []
            for ws in wb.worksheets:
                for row in ws.iter_rows(values_only=True):
                    cells = [str(c) for c in row if c is not None]
                    if cells: out.append(" | ".join(cells))
            return "\n".join(out)
    except Exception as e:
        print(f"  ! erro extraindo {os.path.basename(path)}: {e}")
    return ""

def chunk_text(txt):
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip()
    if not txt: return []
    chunks, i, n = [], 0, len(txt)
    while i < n:
        chunks.append(txt[i:i + CHUNK].strip())
        i += CHUNK - OVERLAP
    return [c for c in chunks if len(c) > 40]

def walk_docs(roots):
    for root in roots:
        for dp, dns, fns in os.walk(root):
            if SKIP_DIR.search(dp + os.sep):
                dns[:] = []; continue
            dns[:] = [d for d in dns if not SKIP_DIR.search(os.path.join(dp, d) + os.sep)]
            for fn in fns:
                ext = os.path.splitext(fn)[1].lower()
                if ext in DOC_EXT and ext not in SKIP_EXT:
                    yield os.path.join(dp, fn), ext

_model = None
def get_model():
    global _model
    if _model is None:
        import torch
        torch.inference_mode = torch.no_grad
        want = os.environ.get("RAG_DEVICE", "auto").lower()
        dev = "cpu"
        if want != "cpu":
            try:
                import torch_directml
                if torch_directml.device_count() > 0:
                    dev = torch_directml.device()
            except Exception:
                pass
            if dev == "cpu" and torch.cuda.is_available():
                dev = "cuda"
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL_NAME, device=dev)
        try: _model.max_seq_length = 384
        except Exception: pass
        print(f"[modelo] {MODEL_NAME} carregado em: {dev}")
    return _model

def embed(texts, kind):
    m = get_model()
    pref = [f"{kind}: {t}" for t in texts]
    for bs in (BATCH, 8, 4, 1):
        try:
            return m.encode(pref, normalize_embeddings=True, batch_size=bs,
                            show_progress_bar=False).tolist()
        except RuntimeError as e:
            if "memory" in str(e).lower() and bs > 1: continue
            raise

def load_manifest():
    if os.path.exists(MANIFEST):
        with open(MANIFEST, "r", encoding="utf-8") as f: return json.load(f)
    return {}

def save_manifest(m):
    with open(MANIFEST, "w", encoding="utf-8") as f: json.dump(m, f, ensure_ascii=False)

def _resolve_default_roots():
    vertice_root = os.path.dirname(BASE)
    candidates = []
    if os.path.exists(CONFIG):
        try:
            with open(CONFIG, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            if cfg.get("obsidian_vault_path"):
                candidates.append(os.path.normpath(os.path.join(vertice_root, cfg["obsidian_vault_path"])))
            for p in cfg.get("additional_index_paths", []):
                candidates.append(os.path.normpath(os.path.join(vertice_root, p)))
        except Exception:
            pass
    for sub in ("_memoria", "identidade", "dados", "modelos", "acervo"):
        p = os.path.join(vertice_root, sub)
        if p not in candidates:
            candidates.append(p)
    valid = [r for r in candidates if os.path.exists(r)]
    return valid if valid else [vertice_root]

def cmd_index(args):
    import lancedb
    if args.reset:
        import shutil
        shutil.rmtree(DB_DIR, ignore_errors=True)
        if os.path.exists(MANIFEST): os.remove(MANIFEST)
        print("[reset] indice zerado.")
    db = lancedb.connect(DB_DIR)
    manifest = load_manifest()
    roots = args.roots if args.roots else _resolve_default_roots()
    files = list(walk_docs(roots))
    print(f"[scan] {len(files)} arquivos candidatos.")
    tbl = db.open_table(TABLE) if TABLE in _tables(db) else None
    novos = pulados = total_chunks = 0
    t0 = time.time()
    for idx, (path, ext) in enumerate(files, 1):
        try:
            mtime = os.path.getmtime(path)
            size = os.path.getsize(path)
        except OSError:
            continue
        if path in manifest and abs(manifest[path]["mtime"] - mtime) < 1:
            pulados += 1; continue
        if size > 15 * 1024 * 1024:
            print(f"  ! pulando {os.path.basename(path)} (muito grande: {size/(1024*1024):.1f}MB)")
            manifest[path] = {"mtime": mtime, "nchunks": 0}
            continue
        chunks = chunk_text(extract(path, ext))
        if not chunks:
            manifest[path] = {"mtime": mtime, "nchunks": 0}; continue
        vecs = embed(chunks, "passage")
        rel = os.path.relpath(path, os.path.commonpath(roots)) if len(roots) == 1 else path
        rows = [{"id": hashlib.md5(f"{path}#{i}".encode()).hexdigest(),
                 "vector": v, "text": c, "path": path, "rel": rel,
                 "fname": os.path.basename(path), "ext": ext, "chunk": i, "mtime": mtime}
                for i, (c, v) in enumerate(zip(chunks, vecs))]
        if tbl is None:
            tbl = db.create_table(TABLE, data=rows)
        else:
            tbl.add(rows)
        manifest[path] = {"mtime": mtime, "nchunks": len(chunks)}
        novos += 1; total_chunks += len(chunks)
        import gc
        gc.collect()
        if novos % 10 == 0:
            save_manifest(manifest)
            print(f"  [{idx}/{len(files)}] {novos} arqs, {total_chunks} chunks, {time.time()-t0:.0f}s")
    save_manifest(manifest)
    print(f"[ok] novos={novos} pulados={pulados} chunks+={total_chunks} tempo={time.time()-t0:.0f}s")

def cmd_query(args):
    import lancedb
    db = lancedb.connect(DB_DIR)
    if TABLE not in _tables(db):
        print("Indice vazio. Rode 'index' primeiro."); return
    tbl = db.open_table(TABLE)
    queries = args.q if isinstance(args.q, list) else [args.q]
    qvs = embed(queries, "query")
    filtro = (args.filtro or "").strip().lower()
    fetch_k = max(args.k * 10, 80) if filtro else args.k

    for q_text, qv in zip(queries, qvs):
        res = tbl.search(qv).limit(fetch_k).to_list()
        if filtro:
            res = [r for r in res if filtro in r.get("path", "").lower() or filtro in r.get("fname", "").lower()][:args.k]
        titulo_filtro = f" [filtro: {args.filtro}]" if filtro else ""
        print(f"\n>> {q_text}{titulo_filtro}\n" + "=" * 70)
        if not res:
            print("  (nenhum resultado encontrado para este filtro/consulta)")
            continue
        for i, r in enumerate(res, 1):
            raw_txt = r.get("text", "").strip()
            corpo = (re.sub(r"\s+", " ", raw_txt)[:280] + "...") if args.curto else raw_txt
            print(f"\n[{i}] {r['fname']}  (dist={r.get('_distance',0):.3f}, chunk={r.get('chunk',0)})\n    Caminho: {r['path']}\n    ---\n{corpo}\n    ---")

def cmd_stats(args):
    import lancedb
    db = lancedb.connect(DB_DIR)
    m = load_manifest()
    files = sum(1 for v in m.values() if v.get("nchunks", 0) > 0)
    chunks = sum(v.get("nchunks", 0) for v in m.values())
    n = db.open_table(TABLE).count_rows() if TABLE in _tables(db) else 0
    print(f"arquivos indexados: {files}\nchunks (manifest): {chunks}\nlinhas na tabela: {n}\nmodelo: {MODEL_NAME}\nDB: {DB_DIR}")

def main():
    ap = argparse.ArgumentParser(description="RAG local de um acervo de documentos")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pi = sub.add_parser("index"); pi.add_argument("roots", nargs="*"); pi.add_argument("--reset", action="store_true")
    pq = sub.add_parser("query")
    pq.add_argument("q", nargs="+", help="Uma ou mais perguntas em linguagem natural (carrega o modelo 1 unica vez)")
    pq.add_argument("-k", type=int, default=8, help="Numero de trechos retornados por pergunta")
    pq.add_argument("-f", "--filtro", type=str, default="", help="Filtra resultados pelo caminho ou nome do arquivo")
    pq.add_argument("--curto", action="store_true", help="Retorna apenas snippet curto de 280 caracteres em vez do chunk completo de 1200 caracteres")
    sub.add_parser("stats")
    args = ap.parse_args()
    {"index": cmd_index, "query": cmd_query, "stats": cmd_stats}[args.cmd](args)

if __name__ == "__main__":
    main()
