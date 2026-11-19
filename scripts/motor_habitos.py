# -*- coding: utf-8 -*-
"""
Motor Leve de Aprendizado Sequencial (Zero RAM em background).
Registra transicoes A -> B em _memoria/padroes_sequenciais.json e sincroniza _memoria/grafo_de_habitos.md.
"""
import os
import sys
import json
import datetime
import argparse

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM_DIR = os.path.join(BASE_DIR, "_memoria")
JSON_PATH = os.path.join(MEM_DIR, "padroes_sequenciais.json")
MD_PATH = os.path.join(MEM_DIR, "grafo_de_habitos.md")


def load_data():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "transitions": [
            {"de": "Analise de Caso ou Autos", "para": "Minuta no Papel Timbrado + _RACIOCINIO.md", "count": 2, "user": "sistema"},
            {"de": "Audio ou Transcricao de Atendimento", "para": "Ata Comercial + Proposta de Honorarios", "count": 2, "user": "sistema"},
            {"de": "Minuta de Peca Contenciosa", "para": "Auditoria Juiz Externo + Visual Law", "count": 2, "user": "sistema"},
            {"de": "Arquivos Novos no Downloads", "para": "Triagem Pasta do Cliente + Checklist ADVBOX", "count": 2, "user": "sistema"},
        ],
        "history": []
    }


def save_data(data):
    os.makedirs(MEM_DIR, exist_ok=True)
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    lines = [
        "# Grafo de Habitos e Padroes Sequenciais do Escritorio",
        "",
        "> Atualizado automaticamente pelo Agente Fixo Preditivo e por `scripts/motor_habitos.py`.",
        "",
        "## 1. Transicoes Registradas (Ordenadas por Frequencia)",
        "",
        "| Tarefa Anterior (A) | Proximo Passo Observado (B) | Contagem | Status de Automacao |",
        "|---|---|---|---|",
    ]
    for t in sorted(data["transitions"], key=lambda x: x["count"], reverse=True):
        cnt = t["count"]
        if cnt >= 3:
            st = "Candidato a Atalho Unico (3+ repeticoes)"
        elif cnt == 2:
            st = "Ativo na Opcao 1 da Bussola (2x)"
        else:
            st = "Observado 1x"
        lines.append(f"| `{t['de']}` | `{t['para']}` | {cnt} | {st} |")

    lines.extend(["", "## 2. Ultimas Sequencias Aprendidas", ""])
    for h in data["history"][-15:]:
        lines.append(f"- [{h['date']}] ({h['user']}): `{h['de']}` -> `{h['para']}`")

    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Motor de Aprendizado Sequencial AdvOs")
    sub = parser.add_subparsers(dest="cmd")

    p_reg = sub.add_parser("registrar")
    p_reg.add_argument("--de", required=True)
    p_reg.add_argument("--para", required=True)
    p_reg.add_argument("--usuario", default="equipe")

    p_sug = sub.add_parser("sugerir")
    p_sug.add_argument("--atual", required=True)

    args = parser.parse_args()
    data = load_data()

    if args.cmd == "registrar":
        found = False
        for t in data["transitions"]:
            if t["de"].lower() == args.de.lower() and t["para"].lower() == args.para.lower():
                t["count"] += 1
                found = True
                break
        if not found:
            data["transitions"].append({"de": args.de, "para": args.para, "count": 1, "user": args.usuario})
        data["history"].append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "de": args.de,
            "para": args.para,
            "user": args.usuario,
        })
        save_data(data)
        print(f"Transicao registrada com sucesso: {args.de} -> {args.para}")
    elif args.cmd == "sugerir":
        q = args.atual.lower()
        matches = [t for t in data["transitions"] if q in t["de"].lower() or t["de"].lower() in q]
        matches.sort(key=lambda x: x["count"], reverse=True)
        for m in matches[:3]:
            print(f"[{m['count']}x] Depois de '{m['de']}' -> sugerir: '{m['para']}'")
    else:
        save_data(data)
        print("Grafo de habitos sincronizado.")


if __name__ == "__main__":
    main()
