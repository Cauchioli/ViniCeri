# -*- coding: utf-8 -*-
"""
Scanner e Conector Automático do OneDrive — Vértice OS
Escritório Dr. Vinícius Cerineo

O que este script faz:
1. Localiza automaticamente a pasta do OneDrive no Windows (ou recebe o caminho por argumento).
2. Identifica as pastas estruturais do escritório no OneDrive:
   - Clientes Fixos
   - Processos
   - Modelos (e localiza o arquivo do Papel Timbrado oficial em .docx)
   - Despesas de Clientes
3. Dimensiona o acervo (total de arquivos, pastas de clientes e processos, extensões) sem gastar tokens.
4. Atualiza automaticamente o arquivo rag/rag_config.json para que o RAG local indexe e consulte
   o OneDrive do escritório (respeitando o bloqueio de pastas financeiras internas quando aplicável).
5. Salva o diagnóstico em _memoria/raiox_onedrive.md.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent
MEMORIA_DIR = BASE_DIR / "_memoria"
RAG_CFG_PATH = BASE_DIR / "rag" / "rag_config.json"


def detectar_onedrive(custom_path=None):
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p

    candidatos = []
    for env_key in ("OneDriveCommercial", "OneDrive", "OneDriveConsumer"):
        val = os.environ.get(env_key)
        if val and Path(val).exists():
            candidatos.append(Path(val))

    home = Path.home()
    for p in home.iterdir():
        if p.is_dir() and "onedrive" in p.name.lower():
            if p not in candidatos:
                candidatos.append(p)

    if not candidatos:
        return None

    # Prioriza o OneDrive que contenha pastas como Processos, Modelos ou Clientes Fixos
    for c in candidatos:
        try:
            nomes = {x.name.lower() for x in c.iterdir() if x.is_dir()}
            if nomes & {"processos", "modelos", "clientes fixos", "escritorio", "escritório"}:
                return c
        except Exception:
            continue
    return candidatos[0]


def escanear_onedrive(custom_path=None):
    MEMORIA_DIR.mkdir(parents=True, exist_ok=True)
    od_path = detectar_onedrive(custom_path)

    print("=================================================================")
    print("  VÉRTICE OS: CONECTOR E SCANNER DO ONEDRIVE DO ESCRITÓRIO")
    print("=================================================================")

    if not od_path or not od_path.exists():
        msg = (
            "# Raio-X do OneDrive — Escritório Dr. Vinícius Cerineo\n\n"
            "- **Status:** Caminho do OneDrive não detectado automaticamente nas variáveis padrão.\n"
            "- **Ação na Entrevista (`/instalar`):** Solicitar ao Dr. Vinícius o caminho da pasta do OneDrive "
            "e rodar `python scripts/scanner_onedrive.py \"CAMINHO_DO_ONEDRIVE\"`.\n"
        )
        (MEMORIA_DIR / "raiox_onedrive.md").write_text(msg, encoding="utf-8")
        print("[AVISO] OneDrive nao detectado automaticamente. Sera perguntado no /instalar.")
        return

    print(f"[OK] OneDrive localizado em: {od_path}")

    subpastas_chave = {
        "clientes_fixos": None,
        "processos": None,
        "modelos": None,
        "despesas_clientes": None,
    }
    timbrados_encontrados = []
    total_arquivos = 0
    extensoes = {}
    pastas_topo = []

    try:
        for item in od_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                pastas_topo.append(item.name)
                nl = item.name.lower()
                if "fixo" in nl or "cliente" in nl:
                    subpastas_chave["clientes_fixos"] = item
                elif "processo" in nl:
                    subpastas_chave["processos"] = item
                elif "modelo" in nl:
                    subpastas_chave["modelos"] = item
                elif "despesa" in nl:
                    subpastas_chave["despesas_clientes"] = item
    except Exception:
        pass

    # Varredura rápida (limitada em profundidade/contagem para ser instantânea mesmo em 250GB)
    limite_arquivos_scan = 25000
    for root, dirs, files in os.walk(od_path):
        if any(skip in root.lower() for skip in [".git", "node_modules", ".venv", "__pycache__", "lancedb"]):
            continue
        for f in files:
            total_arquivos += 1
            ext = os.path.splitext(f)[1].lower()
            extensoes[ext] = extensoes.get(ext, 0) + 1
            fl = f.lower()
            if ext in (".docx", ".dotx") and any(k in fl for k in ["timbrado", "papel", "modelo", "padrao", "padrão"]):
                if len(timbrados_encontrados) < 10:
                    timbrados_encontrados.append(str(Path(root) / f))
        if total_arquivos >= limite_arquivos_scan:
            break

    # Atualiza rag/rag_config.json para incluir o OneDrive e o Segundo Cérebro local
    caminhos_indexacao = [
        str(BASE_DIR / "_memoria"),
        str(BASE_DIR / "10-juridico"),
        str(BASE_DIR / "20-comercial"),
        str(BASE_DIR / "30-administrativo"),
        str(BASE_DIR / "50-skills-operacionais"),
        str(BASE_DIR / "90-historico-importado"),
        str(BASE_DIR / "dados"),
    ]
    # Se encontrou subpastas operacionais específicas no OneDrive, indexa elas (ou o OneDrive raiz)
    adicionou_sub = False
    for ch in ("modelos", "clientes_fixos", "processos"):
        if subpastas_chave[ch]:
            caminhos_indexacao.append(str(subpastas_chave[ch]))
            adicionou_sub = True
    if not adicionou_sub:
        caminhos_indexacao.append(str(od_path))

    RAG_CFG_PATH.parent.mkdir(parents=True, exist_ok=True)
    cfg_rag = {
        "obsidian_vault_path": str(BASE_DIR),
        "onedrive_office_path": str(od_path),
        "additional_index_paths": caminhos_indexacao,
        "excluded_folders": ["40-financeiro-restrito", "Financeiro", "Diretoria", ".git", ".venv", "node_modules"]
    }
    RAG_CFG_PATH.write_text(json.dumps(cfg_rag, ensure_ascii=False, indent=2), encoding="utf-8")

    relatorio = f"""# Raio-X do OneDrive & Conexão RAG — Escritório Dr. Vinícius Cerineo

- **Data da Varredura:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Caminho do OneDrive Detectado:** `{od_path}`
- **Total de Arquivos Inspecionados (Amostra Rápida):** {total_arquivos}{'+' if total_arquivos >= limite_arquivos_scan else ''}

---

## 1. Pastas Estruturais Mapeadas no OneDrive
- **Pastas no Nível Raiz:** {', '.join(f'`{p}`' for p in pastas_topo[:20]) or '*(Nenhuma subpasta listada)*'}
- **Clientes Fixos:** `{subpastas_chave['clientes_fixos'] or 'Mapear na entrevista'}`
- **Processos:** `{subpastas_chave['processos'] or 'Mapear na entrevista'}`
- **Modelos (Papel Timbrado):** `{subpastas_chave['modelos'] or 'Mapear na entrevista'}`
- **Despesas de Clientes:** `{subpastas_chave['despesas_clientes'] or 'Mapear na entrevista'}`

---

## 2. Arquivos de Papel Timbrado e Modelos Detectados (`.docx`)
{chr(10).join(f'- `{t}`' for t in timbrados_encontrados) if timbrados_encontrados else '- *(Nenhum arquivo com nome timbrado/modelo detectado no nível superficial; confirmar caminho exato na pasta Modelos)*'}

---

## 3. Distribuição de Formatos no OneDrive
{chr(10).join(f'- **{ext or "sem extensão"}**: {qtd} arquivos' for ext, qtd in sorted(extensoes.items(), key=lambda x: x[1], reverse=True)[:8])}

---

## 4. Configuração do RAG Local (`rag/rag_config.json`)
O buscador semântico já foi apontado para consultar simultaneamente este repositório do Vértice OS e as pastas operacionais do OneDrive acima.
"""
    (MEMORIA_DIR / "raiox_onedrive.md").write_text(relatorio, encoding="utf-8")
    print(f"[OK] Raio-X do OneDrive salvo em: {MEMORIA_DIR / 'raiox_onedrive.md'}")
    print(f"[OK] Configuração do RAG atualizada em: {RAG_CFG_PATH}")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    escanear_onedrive(arg)
