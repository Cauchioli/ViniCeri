# Protocolo Organizador de Acervo: OneDrive & Pasta CLAUDIO (Vértice OS)

Este protocolo estabelece o procedimento seguro e auditável para inventariar, integrar e organizar tanto o acervo de **~250 GB no OneDrive** do escritório quanto os arquivos e exportações da pasta **`Cláudio`** na Área de Trabalho, sem risco de perda ou corrupção de dados.

---

## 1. As 5 Leis Inegociáveis do Organizador

1. **Proibição Absoluta de Apagar:**
   - Nenhum arquivo ou pasta do OneDrive ou da pasta `Cláudio` é excluído pela IA. Caso algum arquivo temporário ou duplicado precise ser isolado, ele é movido apenas para uma pasta `_quarentena_AAAA-MM-DD` mediante autorização.
2. **Lei da Caixa Lacrada (Processos no OneDrive):**
   - Pastas de processos já existentes dentro de `Processos` ou `Clientes Fixos` no OneDrive são caixas lacradas: a IA lê e indexa seu conteúdo para responder perguntas e redigir peças, mas jamais renomeia ou altera arquivos brutos de autos baixados de tribunais sem ordem expressa.
3. **Intocabilidade de Documentos Fiscais, Contábeis e Societários:**
   - Guias de ITBI, custas, comprovantes bancários, notas fiscais e contratos em `Despesas de Clientes` ou no Financeiro da Gabi jamais são alterados.
4. **Parada Obrigatória para Movimentações em Lote:**
   - A triagem de novos arquivos vindos da pasta `Downloads` apresenta primeiro o plano `DE -> PARA` (qual pasta do OneDrive será criada/atualizada e qual tarefa será gerada para o ADVBOX) antes de mover os arquivos definitivos.
5. **Rastreabilidade Total:**
   - Toda importação da pasta `Cláudio` e toda triagem de `Downloads -> OneDrive` é registrada em log auditável (`00-LOG-movimentacoes.md`).

---

## 2. Integração da Pasta `Cláudio` (Desktop) + Histórico ChatGPT e Claude

1. **Absorção de Skills Pré-Existentes:**
   - Tudo o que o Dr. Vinícius já criou dentro da pasta `Cláudio` na Área de Trabalho (arquivos `.md`, `.txt`, `.docx`, scripts e modelos) é copiado e catalogado em `50-skills-operacionais/skills_importadas_claudio/`, preservando os arquivos originais intocados.
2. **Mineração Determinística dos Exports (`conversations.json`, `projects.json`, `memories.json`):**
   - Como os arquivos `conversations.json` exportados do Claude e do ChatGPT podem ultrapassar 25 milhões de caracteres, o script `scripts/ingerir_pasta_claudio_e_historico.py` processa o JSON localmente em Python (zero gasto de tokens) e separa automaticamente as conversas nos 4 pilares do escritório:
     - `10-juridico` (casos, teses, revisões cruzadas, "Tio Rui Barbosa", "Perfil Técnico Jurídico", "Usucapião 4ª Vara")
     - `20-comercial` (propostas, negociações, marketing, "Conselho Estratégico")
     - `30-administrativo` (fluxos ADVBOX, organização de pastas, tarefas da equipe)
     - `40-financeiro-restrito` (precificação, honorários, despesas e rotinas da Gabi)
