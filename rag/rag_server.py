# -*- coding: utf-8 -*-
"""
Servidor de busca residente (100% LOCAL, stdlib pura).
Mantém o modelo carregado em RAM (elimina o reload de ~8s por consulta, respondendo em ~0.05s).
Atado a 127.0.0.1 (não aceita conexão externa).

  set RAG_DEVICE=cpu  &&  python rag_server.py
  curl "http://127.0.0.1:8799/query?q=sua+pergunta&k=8&filtro=Cliente"
  curl "http://127.0.0.1:8799/health"
  curl "http://127.0.0.1:8799/index?path=C:/caminho/da/pasta"
"""
import os, json, threading, hashlib, time
os.environ.setdefault("RAG_DEVICE", "cpu")
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs, unquote
import rag_acervo as R

HOST, PORT = "127.0.0.1", 8799
_lock      = threading.Lock()
_tbl       = None
_db        = None

def _ready():
    global _tbl, _db
    import lancedb
    _db = lancedb.connect(R.DB_DIR)
    if R.TABLE not in R._tables(_db):
        raise RuntimeError("Indice vazio: rode 'rag_acervo.py index' primeiro")
    _tbl = _db.open_table(R.TABLE)
    R.get_model()
    print(f"[server] pronto em http://{HOST}:{PORT}  "
          f"(device={os.environ['RAG_DEVICE']}, linhas={_tbl.count_rows()})")

def search(q, k, filtro=""):
    filtro_norm = (filtro or "").strip().lower()
    fetch_k = max(k * 10, 80) if filtro_norm else k
    with _lock:
        qv   = R.embed([q], "query")[0]
        rows = _tbl.search(qv).limit(fetch_k).to_list()
    if filtro_norm:
        rows = [r for r in rows if filtro_norm in r.get("path", "").lower() or filtro_norm in r.get("fname", "").lower()][:k]
    return [{"rank": i, "fname": r["fname"], "path": r["path"], "rel": r.get("rel", ""),
             "chunk": r.get("chunk", 0),
             "dist": round(float(r.get("_distance", 0)), 4), "text": r["text"]}
            for i, r in enumerate(rows, 1)]

def index_path(folder: str) -> dict:
    global _tbl, _db
    import lancedb

    folder = os.path.normpath(unquote(folder))
    if not os.path.isdir(folder):
        raise ValueError(f"pasta nao encontrada: {folder}")

    manifest = R.load_manifest()
    files    = list(R.walk_docs([folder]))
    novos = pulados = total_chunks = 0
    t0 = time.time()

    with _lock:
        if _db is None:
            _db = lancedb.connect(R.DB_DIR)

        for path, ext in files:
            try:
                mtime = os.path.getmtime(path)
            except OSError:
                continue

            if path in manifest and abs(manifest[path]["mtime"] - mtime) < 1:
                pulados += 1
                continue

            chunks = R.chunk_text(R.extract(path, ext))
            if not chunks:
                manifest[path] = {"mtime": mtime, "nchunks": 0}
                continue

            vecs = R.embed(chunks, "passage")
            rel  = os.path.relpath(path, folder)
            rows = [{"id":     hashlib.md5(f"{path}#{i}".encode()).hexdigest(),
                     "vector": v, "text": c, "path": path, "rel": rel,
                     "fname":  os.path.basename(path), "ext": ext,
                     "chunk":  i, "mtime": mtime}
                    for i, (c, v) in enumerate(zip(chunks, vecs))]

            if _tbl is None:
                _tbl = _db.create_table(R.TABLE, data=rows)
            else:
                _tbl.add(rows)

            manifest[path] = {"mtime": mtime, "nchunks": len(chunks)}
            novos        += 1
            total_chunks += len(chunks)

        R.save_manifest(manifest)

    return {
        "folder":       folder,
        "candidatos":   len(files),
        "novos":        novos,
        "pulados":      pulados,
        "chunks_add":   total_chunks,
        "total_rows":   _tbl.count_rows() if _tbl else 0,
        "tempo_s":      round(time.time() - t0, 1),
    }

class H(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        b = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        u  = urlparse(self.path)
        qs = parse_qs(u.query)

        if u.path == "/health":
            rows = _tbl.count_rows() if _tbl else 0
            return self._send(200, {"ok": True, "rows": rows,
                                    "model": R.MODEL_NAME,
                                    "device": os.environ["RAG_DEVICE"]})

        if u.path == "/query":
            q_list = [x.strip() for x in (qs.get("q") or []) if x.strip()]
            filtro = (qs.get("filtro") or qs.get("f") or [""])[0].strip()
            try:    k = int((qs.get("k") or ["8"])[0])
            except ValueError: k = 8
            if not q_list:
                return self._send(400, {"ok": False, "erro": "faltou ?q="})
            try:
                if len(q_list) == 1:
                    return self._send(200, {"ok": True, "q": q_list[0], "k": k, "filtro": filtro,
                                            "hits": search(q_list[0], k, filtro)})
                else:
                    results = [{"q": q_item, "hits": search(q_item, k, filtro)} for q_item in q_list]
                    return self._send(200, {"ok": True, "k": k, "filtro": filtro, "results": results})
            except Exception as e:
                return self._send(500, {"ok": False, "erro": str(e)})

        if u.path == "/index":
            path = (qs.get("path") or [""])[0].strip()
            if not path:
                return self._send(400, {"ok": False, "erro": "faltou ?path="})
            print(f"[index] iniciando: {path}")
            try:
                result = index_path(path)
                print(f"[index] concluido: {result}")
                return self._send(200, {"ok": True, **result})
            except Exception as e:
                print(f"[index] erro: {e}")
                return self._send(500, {"ok": False, "erro": str(e)})

        self._send(404, {"ok": False, "erro": "rotas: /query?q= | /health | /index?path="})

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    _ready()
    print(f"[server] rotas disponiveis:")
    print(f"  GET /health")
    print(f"  GET /query?q=<pergunta>&k=8&filtro=<pasta_ou_cliente>")
    print(f"  GET /index?path=<pasta>")
    ThreadingHTTPServer((HOST, PORT), H).serve_forever()
