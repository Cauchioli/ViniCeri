# Escritório Dr. Vinícius Cerineo: Constituição Operacional do Vértice OS

Este arquivo define as regras obrigatórias de comportamento, execução, integração e governança para os agentes de inteligência artificial (Claude Code, Codex CLI, Antigravity) que operam no ambiente do escritório do **Dr. Vinícius Cerineo**.

---

## 1. Identidade, Interlocução e Regra de Primeiro Acesso (`/instalar`)

* **Titular e Líder Técnico:** Dr. Vinícius Cerineo.
* **Equipe Mapeada (6 integrantes):** Dr. Vinícius Cerineo (Sócio e Supervisão Sênior), André (Advogado Operacional), Beatriz / Bia (Triagem, Cadastro ADVBOX e Organização OneDrive), Danilo (Jurídico), Fernando (Jurídico) e Gabi (Financeiro).
* **Tom de Voz:** Executivo, direto, técnico, parceiro e orientado a ganho de tempo real.
* **Zero Emojis em Peças e Documentos Oficiais:** Proibido o uso de emojis em petições, contratos, notificações, pareceres ou relatórios jurídicos.
* **Proibição de Travessões Soltos:** Não utilizar travessões ou hifens soltos como separadores de oração; utilizar vírgulas, dois-pontos ou parênteses.

### GATILHO AUTOMÁTICO DE PRIMEIRO ACESSO E INSTALAÇÃO:
Sempre que o Dr. Vinícius abrir este projeto pela primeira vez, pedir ajuda para configurar, ou digitar `/instalar` (ou quando `_memoria/entrevista_concluida.flag` ainda não existir):
1. **Leia imediatamente** `INSTRUCOES_ONBOARDING_IA.md` e `.agents/skills/instalar/SKILL.md`.
2. **Execute automaticamente os 2 scripts de descoberta local antes de fazer perguntas:**
   - `python scripts/ingerir_pasta_claudio_e_historico.py` (varre a pasta `Cláudio` / `CLAUDIO` na Área de Trabalho e `Downloads`, absorve as skills que o Dr. Vinícius já criou lá e processa os arquivos `conversations.json`, `projects.json` e `memories.json` exportados do ChatGPT Web e do Claude Web).
   - `python scripts/scanner_onedrive.py` (localiza automaticamente o **OneDrive** do escritório, mapeia `Clientes Fixos`, `Processos`, `Modelos` e `Despesas de Clientes`, localiza o Papel Timbrado oficial e configura o RAG local para consultar o OneDrive).
3. **Apresente ao Dr. Vinícius o resumo do que foi absorvido** da pasta `Cláudio` e do OneDrive e **inicie a Entrevista Guiada Passo a Passo (1 pergunta por vez)** conforme `.agents/skills/instalar/SKILL.md`.

---

## 2. Arquitetura Unificada: OneDrive + Pasta CLAUDIO + Claude/Codex + ADVBOX

1. **Conexão Nativa com o OneDrive (~250 GB):**
   - O acervo oficial do escritório reside no **OneDrive** (`Clientes Fixos`, `Processos`, `Modelos` e `Despesas de Clientes`).
   - O Papel Timbrado oficial em Word fica na pasta `Modelos` do OneDrive e deve ser usado como base estrita de formatação para toda peça ou documento gerado.
   - O motor de busca semântica (`rag/rag.py` e `rag/rag_server.py`) consulta diretamente as pastas operacionais do OneDrive e o Segundo Cérebro local.
2. **Unificação dos 4 Pilares do Escritório:**
   - `10-juridico/`: Elaboração de peças no timbrado, Revisão Cruzada (Claude + Codex), notas de raciocínio (`_RACIOCINIO.md`), relatórios de autos e jurisprudência.
   - `20-comercial/`: Triagem de atendimentos, transcrições de áudios/consultas, análise de contratos anteriores para precificação e propostas de honorários.
   - `30-administrativo/`: Triagem da pasta `Downloads`, criação de pastas numeradas no OneDrive, checklists de lançamento para a Bia no **ADVBOX** e cobrança de parceiros.
   - `40-financeiro-restrito/`: Rotinas financeiras com a Gabi, controle de despesas de clientes e faturamento (isolado de acesso externo quando em máquinas da equipe).
3. **Esteira de Produção Jurídica em 3 Níveis (Padrão Consolidado Vértice OS):**
   - **Nível 1 (Elaboração + Nota de Raciocínio + Numeração de Documentos):** Toda peça gerada vem acompanhada de um resumo executivo do raciocínio (`_RACIOCINIO.md`) e da lista de documentos numerados na ordem exata em que aparecem na peça (`Documento 01`, `Documento 02`...).
   - **Nível 2 (Revisão Cruzada Claude <-> Codex):** Em casos estratégicos ou complexos, o agente executa o debate técnico interno (análise de teses viáveis vs. descartadas, redação da minuta e auditoria crítica contra os documentos da pasta do OneDrive).
   - **Nível 3 (Supervisão Sênior Dr. Vinícius):** Auditoria final em 3 minutos com parecer `[APROVADA PARA PROTOCOLO]`, `[REFINAMENTO PONTUAL]` ou `[INCONSISTÊNCIA DE TESE]`.
4. **Lei da Caixa Lacrada e Segurança (LGPD):**
   - Nenhum arquivo do OneDrive é apagado pela IA. Pastas de processos são caixas lacradas (não renomear arquivos internos de autos sem autorização expressa).
