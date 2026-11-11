# Skill 01: Elaboração no Timbrado Oficial & Revisão Cruzada (Claude + Codex)

- **Pilar:** Jurídico (`10-juridico`)
- **Operadores:** Dr. Vinícius Cerineo, André, Danilo e Fernando
- **Arquitetura Integrada:** Método de Revisão Cruzada do Dr. Vinícius ("Tio Rui Barbosa" / "Perfil Técnico Jurídico") + Esteira de 3 Níveis e Nota de Raciocínio Separada (`_RACIOCINIO.md`).

---

## 1. Fluxo de Execução em 4 Passos

### Passo 1: Busca no OneDrive e no RAG Local
1. Antes de redigir, consulte o RAG local (`python rag/rag.py "nome do cliente" "tema da peça"`) e a pasta do cliente dentro do **OneDrive** (`Clientes Fixos` ou `Processos`).
2. Localize na pasta `Modelos` do OneDrive:
   - O arquivo `.docx` do **Papel Timbrado oficial** do escritório;
   - Eventual peça paradigma anterior do escritório sobre o mesmo tema (ex.: isenção de ITBI Tema 1348 STF, notificação de desocupação, usucapião, inventário, contrato de parceria/obra).

### Passo 2: Filtro de Linhas Estratégicas (Para Casos Complexos)
1. Analise a íntegra dos documentos/autos da pasta e apresente ao Dr. Vinícius (ou ao advogado operador) as **Linhas Estratégicas Viáveis**:
   - **Linha A (Tese Principal de Maior Probabilidade)**
   - **Linha B (Tese Subsidiária / Preliminar / Prejudicial)**
   - **Teses Descartadas (e o motivo técnico pelo qual não compensa segui-las)**
2. Caso o comando já traga a linha definida pelo Dr. Vinícius, avance direto ao Passo 3.

### Passo 3: Revisão Cruzada (Elaboração + Crítica Adversarial)
1. **Estágio Redator:** Estrutura a minuta completa (fatos cronológicos ancorados em documentos, subsunção jurídica com artigos vigentes, jurisprudência/temas vinculantes e pedidos líquidos/determinados).
2. **Estágio Revisor Crítico (Papel de Advogado Contrário / Juiz):** Audita o rascunho perguntando:
   - Algum documento da pasta do cliente deixou de ser citado ou impugnado?
   - Há alguma cláusula contratual leonina, prazo decadencial/prescricional ou falha de legitimidade?
   - O texto está incisivo e direto no estilo do Dr. Vinícius?
   - Incorpora imediatamente as correções antes de gerar o arquivo final.

### Passo 4: Saída Tripla Obrigatória na Pasta do Cliente (OneDrive)
1. **Peça Final no Papel Timbrado (`.docx`):**
   - Clonada a partir do arquivo de Papel Timbrado da pasta `Modelos` do OneDrive (preservando fonte serifada Times moderna, margens, cabeçalho, citações recuadas e rodapé).
   - Nomeada no padrão: `[CLIENTE]_[TIPO_DE_PECA]_[TESE_PRINCIPAL]_[RESPONSAVEL].docx`.
2. **Nota de Resumo do Raciocínio (`[CLIENTE]_[TIPO_DE_PECA]_RACIOCINIO.md`):**
   - Documento curto (máximo 1 página) salvo ao lado da peça para que o Dr. Vinícius entenda em 2 minutos o que aconteceu no caso, qual linha foi seguida e o que revisar.
3. **Rol e Numeração Sequencial de Documentos:**
   - Lista exata dos documentos citados na peça (`01_Procuracao...`, `02_Contrato...`), renomeando/organizando os anexos na ordem em que aparecem na narrativa.
