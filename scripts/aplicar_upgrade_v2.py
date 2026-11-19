# -*- coding: utf-8 -*-
"""
Atualizador Local Seguro (Upgrade v2.0 - AdvOs Preditivo & Curso Vivo).
Preserva 100% das customizacoes locais feitas pelo escritorio (faz backup previo)
e acopla o Agente Fixo Preditivo (Bussola de 3 Opcoes + Motor de Habitos + Curso Vivo)
ao final de AGENTS.md, CLAUDE.md e GEMINI.md sem sobrescrever as regras existentes.
"""
import os
import sys
import shutil
import datetime

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
BKP_DIR = os.path.join(ROOT, "_backups_locais", f"backup_antes_upgrade_v2_{TS}")
BLOCO_PATH = os.path.join(ROOT, "40-operacional", "upgrade-v2-preditivo", "BLOCO_AGENTE_PREDITIVO_LAYER0.md")


def main():
    os.makedirs(BKP_DIR, exist_ok=True)
    # 1. Backup dos arquivos locais de governanca e memoria
    alvos_bkp = [
        "AGENTS.md", "CLAUDE.md", "GEMINI.md", "00-ENTRADA.md", "01-REGRAS.md",
        os.path.join("vertice-os", "_memoria", "contexto.md"),
        os.path.join("vertice-os", "_memoria", "estrategia.md"),
        os.path.join("vertice-os", "_memoria", "preferencias.md"),
    ]
    for rel in alvos_bkp:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            dst = os.path.join(BKP_DIR, rel.replace(os.sep, "_"))
            shutil.copy2(p, dst)

    print(f"[1/3] Backup das customizacoes locais salvo em: {BKP_DIR}")

    # 2. Acoplar (append) o bloco do Agente Fixo Preditivo nos arquivos de constituicao locais sem apagar nada
    if os.path.exists(BLOCO_PATH):
        bloco = open(BLOCO_PATH, "r", encoding="utf-8").read()
        for cf in ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]:
            cf_path = os.path.join(ROOT, cf)
            if os.path.exists(cf_path):
                atual = open(cf_path, "r", encoding="utf-8").read()
                if "Bussola de Antecipacao" not in atual:
                    with open(cf_path, "a", encoding="utf-8") as f:
                        f.write("\n\n---\n\n" + bloco)
                    print(f"[2/3] Agente Fixo Preditivo acoplado com seguranca ao final de: {cf}")
                else:
                    print(f"[2/3] {cf} ja contem a Bussola de Antecipacao (preservado).")

    # 3. Inicializar o grafo de habitos local se ainda nao existir
    motor = os.path.join(ROOT, "scripts", "motor_habitos.py")
    if os.path.exists(motor):
        os.system(f'python "{motor}"')

    print("[3/3] Upgrade v2.0 concluido com sucesso! Todas as nuances locais do escritorio foram preservadas.")


if __name__ == "__main__":
    main()
