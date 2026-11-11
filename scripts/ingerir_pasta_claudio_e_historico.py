# -*- coding: utf-8 -*-
"""
Ingestor e Minerador Determinístico: Pasta CLAUDIO + Exports ChatGPT & Claude Web
Escritório Dr. Vinícius Cerineo — Vértice OS

O que este script faz (100% local, zero gasto de tokens da IA):
1. Localiza automaticamente a pasta 'Cláudio' / 'CLAUDIO' / 'Claudio' na Área de Trabalho
   (incluindo OneDrive Desktop), Downloads ou caminho passado por argumento.
2. Absorve todas as Skills, prompts, rascunhos (.md, .txt, .docx, .py) que o Dr. Vinícius
   já criou na pasta CLAUDIO, copiando-os de forma organizada para:
   50-skills-operacionais/skills_importadas_claudio/
3. Localiza arquivos de exportação do Claude Web e do ChatGPT Web (arquivos .zip ou
   conversations.json de até dezenas de milhões de caracteres, projects.json, memories.json)
   tanto na pasta CLAUDIO quanto em Downloads.
4. Quebra e classifica cada conversa nos 4 Pilares do escritório:
   - 10-juridico (casos, petições, contratos, Tio Rui Barbosa, Perfil Técnico Jurídico, Usucapião, ITBI)
   - 20-comercial (propostas, clientes novos, marketing, Conselho Estratégico)
   - 30-administrativo (ADVBOX, OneDrive, equipe, fluxos)
   - 40-financeiro-restrito (honorários, despesas, cobranças, Gabi)
5. Extrai instruções de projetos e padrões recorrentes para sugerir novas Skills e gera:
   - 50-skills-operacionais/00_CATALOGO_UNIFICADO_SKILLS.md
   - 90-historico-importado/00_INDICE_GERAL_HISTORICO_IA.md
"""

import json
import os
import re
import shutil
import sys
import zipfile
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_IMPORT_DIR = BASE_DIR / "50-skills-operacionais" / "skills_importadas_claudio"
HIST_IMPORT_DIR = BASE_DIR / "90-historico-importado"
MEMORIA_DIR = BASE_DIR / "_memoria"


def encontrar_pastas_candidatas(custom_path=None):
    """Procura a pasta CLAUDIO / Cláudio e a pasta Downloads no computador do usuário."""
    home = Path.home()
    candidatas_claudio = []
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            candidatas_claudio.append(p)

    # Locais comuns de Desktop (local e OneDrive) e Documentos
    bases = [
        home / "Desktop",
        home / "Área de Trabalho",
        home / "OneDrive" / "Desktop",
        home / "OneDrive" / "Área de Trabalho",
        home / "Documents",
        home / "Documentos",
        home / "OneDrive" / "Documents",
        home / "OneDrive" / "Documentos",
        home,
    ]
    # Adiciona OneDrive de variáveis de ambiente se existir
    for env_key in ("OneDrive", "OneDriveCommercial", "OneDriveConsumer"):
        val = os.environ.get(env_key)
        if val:
            od = Path(val)
            bases.extend([od, od / "Desktop", od / "Área de Trabalho", od / "Documents", od / "Documentos"])

    nomes_claudio = {"claudio", "cláudio", "claude", "pasta claudio", "pasta cláudio"}
    vistas = set()
    for b in bases:
        try:
            if not b.exists():
                continue
            for item in b.iterdir():
                if item.is_dir() and item.name.lower().strip() in nomes_claudio:
                    rp = str(item.resolve())
                    if rp not in vistas and rp != str(BASE_DIR.resolve()):
                        vistas.add(rp)
                        candidatas_claudio.append(item)
        except Exception:
            continue

    downloads = home / "Downloads"
    return candidatas_claudio, downloads


def classificar_pilar(texto):
    t = texto.lower()
    if any(k in t for k in ["boleto", "despesa", "faturamento", "gabi", "fluxo de caixa", "nota fiscal", "imposto do escritório"]):
        return "40-financeiro-restrito", "Financeiro"
    if any(k in t for k in ["advbox", "onedrive", "cadastrar parte", "numeração de pasta", "beatriz", "bia", "agenda", "relatório mensal"]):
        return "30-administrativo", "Administrativo"
    if any(k in t for k in ["proposta", "honorário", "marketing", "instagram", "fechamento", "conselho estratégico", "captação", "comercial"]):
        return "20-comercial", "Comercial"
    return "10-juridico", "Jurídico"


def limpar_slug(texto, max_len=60):
    s = re.sub(r"[^\w\s-]", "", texto or "sem_titulo", flags=re.UNICODE)
    s = re.sub(r"[-\s]+", "_", s).strip("_").lower()
    return (s[:max_len] or "item")


def extrair_mensagens_conversa(conv):
    """Suporta tanto o formato de exportação do Claude Web quanto o do ChatGPT Web."""
    titulo = conv.get("name") or conv.get("title") or "Conversa sem título"
    created = conv.get("created_at") or conv.get("create_time") or ""
    if isinstance(created, (int, float)):
        try:
            created = datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M")
        except Exception:
            created = str(created)
    elif isinstance(created, str) and len(created) >= 10:
        created = created[:16].replace("T", " ")

    mensagens = []
    # Formato Claude Web: chat_messages
    if "chat_messages" in conv and isinstance(conv["chat_messages"], list):
        origem = "Claude Web"
        for m in conv["chat_messages"]:
            sender = m.get("sender", "user")
            papel = "Dr. Vinícius" if sender in ("human", "user") else "Claude"
            txt = m.get("text") or ""
            if not txt and isinstance(m.get("content"), list):
                partes = [p.get("text", "") for p in m["content"] if isinstance(p, dict) and p.get("text")]
                txt = "\n".join(partes)
            if txt.strip():
                mensagens.append((papel, txt.strip()))
        return titulo, created, origem, mensagens

    # Formato ChatGPT Web: mapping
    if "mapping" in conv and isinstance(conv["mapping"], dict):
        origem = "ChatGPT Web"
        nodes = list(conv["mapping"].values())
        for node in nodes:
            msg = node.get("message")
            if not msg:
                continue
            role = (msg.get("author") or {}).get("role", "")
            if role not in ("user", "assistant", "system"):
                continue
            content = msg.get("content") or {}
            parts = content.get("parts") or []
            texto_partes = [str(p) for p in parts if isinstance(p, (str, int, float)) and str(p).strip()]
            txt = "\n".join(texto_partes).strip()
            if txt:
                papel = "Dr. Vinícius" if role == "user" else ("Sistema/Projeto" if role == "system" else "ChatGPT")
                mensagens.append((papel, txt))
        return titulo, created, origem, mensagens

    return titulo, created, "Histórico IA", mensagens


def processar_json_conversas(caminho_json, indice_conversas, prompts_recorrentes):
    """Lê conversations.json (mesmo gigante de 27MB+) e gera notas organizadas por Pilar e Caso."""
    print(f"[INGESTOR] Processando arquivo de conversas: {caminho_json.name} ({caminho_json.stat().st_size / (1024*1024):.2f} MB)...")
    try:
        with open(caminho_json, "r", encoding="utf-8", errors="replace") as f:
            dados = json.load(f)
    except Exception as e:
        print(f"[AVISO] Nao foi possivel carregar JSON {caminho_json}: {e}")
        return 0

    if isinstance(dados, dict):
        # Caso seja um manifesto ou objeto com chave 'conversations' ou 'data'
        for k in ("conversations", "data", "items", "projects"):
            if k in dados and isinstance(dados[k], list):
                dados = dados[k]
                break
        else:
            dados = [dados]

    if not isinstance(dados, list):
        return 0

    total_importadas = 0
    for idx, conv in enumerate(dados):
        if not isinstance(conv, dict):
            continue
        titulo, data_criacao, origem, msgs = extrair_mensagens_conversa(conv)
        if not msgs:
            continue

        amostra_texto = titulo + "\n" + "\n".join(m[1][:600] for m in msgs[:6])
        pasta_pilar, nome_pilar = classificar_pilar(amostra_texto)

        # Captura comandos/instruções longas do usuário que parecem prompts de skill
        for papel, txt in msgs[:3]:
            if papel == "Dr. Vinícius" and len(txt) > 180 and any(w in txt.lower() for w in ["atue como", "sempre que", "papel timbrado", "revise", "petição", "contrato", "relatório", "modelo"]):
                prompts_recorrentes.append((titulo, origem, txt[:1500]))

        # Monta resumo enxuto da conversa (primeiras e últimas interações para não gerar arquivos gigantes)
        blocos = []
        msgs_selecionadas = msgs if len(msgs) <= 10 else (msgs[:5] + [("...", f"[{len(msgs) - 8} mensagens intermediárias preservadas no JSON original]")] + msgs[-3:])
        for papel, txt in msgs_selecionadas:
            trecho = txt if len(txt) <= 2500 else (txt[:2500] + "\n...[truncado para leitura rápida]...")
            blocos.append(f"### {papel}\n{trecho}")

        subpasta = HIST_IMPORT_DIR / pasta_pilar
        subpasta.mkdir(parents=True, exist_ok=True)
        nome_arq = f"{idx+1:04d}_{limpar_slug(titulo)}.md"
        caminho_nota = subpasta / nome_arq

        conteudo_nota = f"""---
tipo: historico_ia
titulo: "{titulo.replace('"', "'")}"
origem: "{origem}"
pilar: "{nome_pilar}"
data_original: "{data_criacao}"
total_mensagens: {len(msgs)}
status: importado
---

# {titulo}

- **Origem:** {origem}
- **Pilar Classificado:** {nome_pilar}
- **Data:** {data_criacao}
- **Total de Interações:** {len(msgs)}

---

{chr(10).join(blocos)}
"""
        caminho_nota.write_text(conteudo_nota, encoding="utf-8")
        indice_conversas.append({
            "titulo": titulo,
            "origem": origem,
            "pilar": nome_pilar,
            "data": data_criacao,
            "msgs": len(msgs),
            "arquivo": f"90-historico-importado/{pasta_pilar}/{nome_arq}"
        })
        total_importadas += 1

    return total_importadas


def processar_json_projetos_ou_memorias(caminho_json):
    """Extrai projetos (projects.json) ou memórias (memories.json) do Claude/ChatGPT."""
    try:
        with open(caminho_json, "r", encoding="utf-8", errors="replace") as f:
            dados = json.load(f)
        destino = HIST_IMPORT_DIR / f"memoria_extraida_{limpar_slug(caminho_json.stem)}.md"
        texto = json.dumps(dados, ensure_ascii=False, indent=2)
        if len(texto) > 60000:
            texto = texto[:60000] + "\n...[arquivo completo preservado no original]..."
        destino.write_text(
            f"# Dados Importados: {caminho_json.name}\n\n```json\n{texto}\n```\n",
            encoding="utf-8"
        )
        return True
    except Exception:
        return False


def executar_ingestao(custom_claudio_dir=None):
    SKILLS_IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    HIST_IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    MEMORIA_DIR.mkdir(parents=True, exist_ok=True)

    pastas_claudio, pasta_downloads = encontrar_pastas_candidatas(custom_claudio_dir)
    skills_encontradas = []
    indice_conversas = []
    prompts_recorrentes = []
    zips_extraidos = []

    fontes_busca = list(pastas_claudio)
    if pasta_downloads.exists():
        fontes_busca.append(pasta_downloads)

    print("=================================================================")
    print("  VÉRTICE OS: ABSORÇÃO DA PASTA CLAUDIO + HISTÓRICO CHATGPT/CLAUDE")
    print("=================================================================")
    print(f"Pastas CLAUDIO detectadas: {[str(p) for p in pastas_claudio] or 'Nenhuma pasta com nome Cláudio detectada ainda'}")

    # 1. Varre as pastas CLAUDIO para absorver skills (.md, .txt, .docx, .py) e JSONs/ZIPs
    for p_claudio in pastas_claudio:
        for root, dirs, files in os.walk(p_claudio):
            if any(ig in root.lower() for ig in [".git", "node_modules", ".venv", "__pycache__"]):
                continue
            for file in files:
                fp = Path(root) / file
                ext = fp.suffix.lower()
                fn_low = file.lower()

                # Se for arquivo de Skill, Prompt, Regra ou Documento criado na pasta CLAUDIO
                if ext in (".md", ".txt", ".docx", ".py") and "conversations" not in fn_low:
                    dest = SKILLS_IMPORT_DIR / f"{limpar_slug(fp.stem)}{ext}"
                    try:
                        shutil.copy2(fp, dest)
                        resumo = ""
                        if ext in (".md", ".txt"):
                            resumo = fp.read_text(encoding="utf-8", errors="ignore")[:300].replace("\n", " ").strip()
                        skills_encontradas.append({
                            "nome": file,
                            "origem": str(fp),
                            "copiado_para": str(dest.relative_to(BASE_DIR)),
                            "resumo": resumo
                        })
                    except Exception:
                        pass

    # 2. Procura arquivos de exportação (.zip ou conversations.json / projects.json / memories.json)
    arquivos_json_para_ler = []
    for base in fontes_busca:
        if not base.exists():
            continue
        # Na pasta Downloads, olha apenas o nível raiz ou pastas com nome claude/chatgpt/export
        iterador = os.walk(base) if base in pastas_claudio else [(str(base), [], [f.name for f in base.iterdir() if f.is_file()])]
        for root, _, files in iterador:
            for file in files:
                fp = Path(root) / file
                fn_low = file.lower()
                ext = fp.suffix.lower()

                if ext == ".zip" and (base in pastas_claudio or any(k in fn_low for k in ["claude", "chatgpt", "openai", "export", "conversa", "data"])):
                    pasta_unzip = HIST_IMPORT_DIR / f"_unzip_{limpar_slug(fp.stem)}"
                    if not pasta_unzip.exists():
                        try:
                            with zipfile.ZipFile(fp, "r") as zf:
                                nomes_internos = [n.lower() for n in zf.namelist()]
                                eh_export_ia = (base in pastas_claudio) or any(
                                    "conversations.json" in n or "projects.json" in n or "memories.json" in n
                                    for n in nomes_internos
                                )
                                if eh_export_ia:
                                    pasta_unzip.mkdir(parents=True, exist_ok=True)
                                    zf.extractall(pasta_unzip)
                                    zips_extraidos.append(str(fp))
                                    for r2, _, f2 in os.walk(pasta_unzip):
                                        for subf in f2:
                                            if subf.lower().endswith(".json"):
                                                arquivos_json_para_ler.append(Path(r2) / subf)
                        except Exception:
                            pass

                elif ext == ".json" and any(k in fn_low for k in ["conversation", "project", "memor", "chat", "claude", "manifest"]):
                    arquivos_json_para_ler.append(fp)

    # Remove duplicados preservando ordem
    vistos_json = set()
    for jp in arquivos_json_para_ler:
        rjp = str(jp.resolve())
        if rjp in vistos_json:
            continue
        vistos_json.add(rjp)
        fn_low = jp.name.lower()
        if "conversation" in fn_low:
            processar_json_conversas(jp, indice_conversas, prompts_recorrentes)
        elif any(k in fn_low for k in ["project", "memor", "manifest"]):
            processar_json_projetos_ou_memorias(jp)

    # 3. Gera o Catálogo Unificado de Skills (Nativas Vértice OS + Absorvidas da Pasta CLAUDIO + Extraídas do Histórico)
    catalogo_path = BASE_DIR / "50-skills-operacionais" / "00_CATALOGO_UNIFICADO_SKILLS.md"
    linhas_cat = [
        "# Catálogo Unificado de Skills: Escritório Dr. Vinícius Cerineo",
        "",
        f"**Última Atualização:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Pastas `Cláudio` Inspecionadas:** {', '.join(f'`{p}`' for p in pastas_claudio) if pastas_claudio else '*(Aguardando indicação do caminho da pasta Cláudio na entrevista)*'}",
        "",
        "---",
        "",
        "## 1. Skills Oficiais do Vértice OS (Já Ativas e Configuradas)",
        "",
        "| Comando / Skill | Arquivo | Função Prática no Escritório |",
        "|---|---|---|",
        "| `/instalar` | `.agents/skills/instalar/SKILL.md` | Absorve a pasta `Cláudio`, importa históricos do ChatGPT/Claude, conecta ao OneDrive e conduz a entrevista guiada. |",
        "| `/abrir` | `.agents/skills/abrir/SKILL.md` | Carrega a memória do escritório, checa o RAG no OneDrive e abre o painel do dia. |",
        "| `/revisao-cruzada` | `50-skills-operacionais/01_skill_elaboracao_e_revisao_cruzada.md` | Método de dupla checagem (Claude + Codex), gerando a peça no Papel Timbrado do OneDrive + `_RACIOCINIO.md` + numeração de documentos. |",
        "| `/triagem-downloads` | `50-skills-operacionais/02_skill_triagem_downloads_e_advbox.md` | Lê arquivos e áudios recém-baixados no `Downloads`, organiza na pasta do cliente no OneDrive e gera o checklist de cadastro no ADVBOX para a Bia. |",
        "| `Supervisão Sênior` | `50-skills-operacionais/03_skill_supervisao_senior_vinicius.md` | Auditoria em 3 minutos de peças feitas pelo André, Danilo ou Fernando com parecer de protocolo. |",
        "| `Comercial & Contratos` | `50-skills-operacionais/04_skill_comercial_e_contratos.md` | Resumo de atendimento/áudio, proposta de honorários, contratos e termos de distrato/quitação. |",
        "| `Relatórios & Parceiros` | `50-skills-operacionais/05_skill_relatorio_mensal_e_parceiros.md` | Geração de relatórios mensais de andamento para clientes e cobrança organizada de parceiros (ex.: Salata). |",
        "| `Financeiro & Admin (Gabi)` | `50-skills-operacionais/06_skill_financeiro_e_administrativo_gabi.md` | Apoio às rotinas repetitivas do financeiro (despesas no ADVBOX, guias de ITBI/custas e controle de contratos). |",
        "",
        "---",
        "",
        f"## 2. Skills e Arquivos Absorvidos da Pasta `Cláudio` ({len(skills_encontradas)} encontrados)",
        ""
    ]
    if skills_encontradas:
        for s in skills_encontradas:
            linhas_cat.append(f"- **`{s['nome']}`** (Importado para `{s['copiado_para']}`)")
            if s["resumo"]:
                linhas_cat.append(f"  - *Prévia:* {s['resumo']}...")
    else:
        linhas_cat.append("- *Nenhum arquivo avulso encontrado ainda na busca automática; se a pasta `Cláudio` estiver em outro caminho, informe durante o `/instalar`.*")

    linhas_cat.extend([
        "",
        "---",
        "",
        f"## 3. Padrões e Prompts Extraídos do Histórico ChatGPT / Claude ({len(prompts_recorrentes)} detectados)",
        ""
    ])
    if prompts_recorrentes:
        for tit, orig, pr in prompts_recorrentes[:15]:
            linhas_cat.append(f"### Origem: {tit} ({orig})\n```text\n{pr}\n```\n")
    else:
        linhas_cat.append("- *Assim que o arquivo `conversations.json` for processado, os prompts recorrentes aparecerão aqui automaticamente.*")

    catalogo_path.write_text("\n".join(linhas_cat), encoding="utf-8")

    # 4. Gera o Índice Geral do Histórico Importado
    indice_path = HIST_IMPORT_DIR / "00_INDICE_GERAL_HISTORICO_IA.md"
    por_pilar = {"Jurídico": [], "Comercial": [], "Administrativo": [], "Financeiro": []}
    for item in indice_conversas:
        por_pilar.setdefault(item["pilar"], []).append(item)

    linhas_ind = [
        "# Índice Geral do Histórico Importado (ChatGPT Web + Claude Web)",
        "",
        f"**Total de Conversas Importadas e Classificadas:** {len(indice_conversas)}",
        f"**Pacotes ZIP Extraídos:** {len(zips_extraidos)}",
        "",
        "---",
    ]
    for pilar, lista in por_pilar.items():
        linhas_ind.append(f"\n## Pilar {pilar} ({len(lista)} conversas)\n")
        if lista:
            for it in lista[:80]:
                linhas_ind.append(f"- **[{it['titulo']}]({it['arquivo']})** ({it['origem']}, {it['msgs']} msgs, {it['data']})")
        else:
            linhas_ind.append("- *(Nenhuma conversa classificada neste pilar ainda)*")

    indice_path.write_text("\n".join(linhas_ind), encoding="utf-8")

    print(f"[OK] Skills absorvidas da pasta CLAUDIO: {len(skills_encontradas)}")
    print(f"[OK] Conversas importadas e organizadas: {len(indice_conversas)}")
    print(f"[OK] Catalogo salvo em: {catalogo_path}")
    print(f"[OK] Indice de historico salvo em: {indice_path}")


if __name__ == "__main__":
    arg_path = sys.argv[1] if len(sys.argv) > 1 else None
    executar_ingestao(arg_path)
