---
name: absorver-claudio
description: >
  Reexecuta a varredura da pasta CLAUDIO (Área de Trabalho) e de Downloads para absorver
  novas skills, documentos ou exportações de histórico do ChatGPT e do Claude Web.
---

# `/absorver-claudio`: Sincronização da Pasta CLAUDIO e Históricos Web

1. Execute no terminal:
   ```bash
   python scripts/ingerir_pasta_claudio_e_historico.py
   python rag/rag_acervo.py index
   ```
2. Leia `50-skills-operacionais/00_CATALOGO_UNIFICADO_SKILLS.md` e `90-historico-importado/00_INDICE_GERAL_HISTORICO_IA.md`.
3. Apresente ao Dr. Vinícius a lista de novas skills e conversas que acabaram de ser integradas e indexadas no RAG.
