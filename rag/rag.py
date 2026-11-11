# -*- coding: utf-8 -*-
"""
Cliente unificado de busca semântica (RAG local).
  python rag.py "pergunta 1" "pergunta 2" -f "Clientes Fixos" -k 5
  python rag.py --curto "pergunta"
  python rag.py --json "pergunta"
Bate primeiro no servidor residente na porta 8799 (resposta em ~0.05s).
Se o servidor estiver desligado, executa em modo batch local (carrega o modelo 1 única vez para todas as perguntas).
Retorna por padrão o bloco completo (1.200 caracteres) + caminho absoluto da fonte, eliminando leituras secundárias.
"""
import json, argparse, urllib.request, urllib.parse, sys, re

URL = "http://127.0.0.1:8799/query"

def via_server(queries, k, filtro):
    out = []
    for q in queries:
        params = {"q": q, "k": k}
        if filtro:
            params["filtro"] = filtro
        qs = urllib.parse.urlencode(params)
        with urllib.request.urlopen(f"{URL}?{qs}", timeout=30) as r:
            data = json.loads(r.read().decode("utf-8"))
            out.append((q, data.get("hits", [])))
    return out

def via_local(queries, k, filtro):
    import os
    os.environ.setdefault("RAG_DEVICE", "cpu")
    import rag_acervo as R, lancedb
    db = lancedb.connect(R.DB_DIR)
    tbl = db.open_table(R.TABLE)
    qvs = R.embed(queries, "query")
    filtro_norm = (filtro or "").strip().lower()
    fetch_k = max(k * 10, 80) if filtro_norm else k
    out = []
    for q, qv in zip(queries, qvs):
        rows = tbl.search(qv).limit(fetch_k).to_list()
        if filtro_norm:
            rows = [r for r in rows if filtro_norm in r.get("path", "").lower() or filtro_norm in r.get("fname", "").lower()][:k]
        hits = [{"rank": i, "fname": r["fname"], "path": r["path"], "rel": r.get("rel", ""),
                 "chunk": r.get("chunk", 0),
                 "dist": round(float(r.get("_distance", 0)), 4), "text": r["text"]}
                for i, r in enumerate(rows, 1)]
        out.append((q, hits))
    return out

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Busca semantica no acervo (RAG local)")
    ap.add_argument("q", nargs="+", help="Uma ou mais perguntas em linguagem natural")
    ap.add_argument("-k", type=int, default=8, help="Numero de trechos por pergunta")
    ap.add_argument("-f", "--filtro", type=str, default="", help="Filtra por pasta ou nome de arquivo")
    ap.add_argument("--curto", action="store_true", help="Exibe apenas snippet curto de 280 caracteres")
    ap.add_argument("--json", action="store_true", help="Saida em JSON")
    a = ap.parse_args()

    queries = a.q if isinstance(a.q, list) else [a.q]
    try:
        results, origem = via_server(queries, a.k, a.filtro), "servidor-residente (0.05s)"
    except Exception:
        results, origem = via_local(queries, a.k, a.filtro), "batch-local"

    if a.json:
        print(json.dumps([{"query": q, "origem": origem, "hits": h} for q, h in results], ensure_ascii=False, indent=2))
        return

    filtro_tag = f" | filtro='{a.filtro}'" if a.filtro else ""
    for q, hits in results:
        print(f"\nBUSCA [{origem}{filtro_tag}]: {q}\n" + "=" * 72)
        if not hits:
            print("  (nenhum resultado encontrado)")
            continue
        for h in hits:
            raw_txt = h.get("text", "").strip()
            corpo = (re.sub(r"\s+", " ", raw_txt)[:280] + "...") if a.curto else raw_txt
            print(f"\n[{h['rank']}] {h['fname']}  (dist={h['dist']}, chunk={h.get('chunk',0)})\n    FONTE: {h['path']}\n    ---\n{corpo}\n    ---")

if __name__ == "__main__":
    main()
