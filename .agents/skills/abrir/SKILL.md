---
name: abrir
description: >
  Carrega a memória operacional do escritório do Dr. Vinícius Cerineo, verifica a conexão
  com o OneDrive e o histórico importado da pasta CLAUDIO, e apresenta o briefing executivo da sessão.
---

# `/abrir`: Inicialização Diária do Vértice OS (Dr. Vinícius Cerineo)

1. Leia `_memoria/contexto.md`, `_memoria/equipe_e_fluxos.md`, `_memoria/estrategia.md` e `_memoria/raiox_onedrive.md`.
2. Verifique se `_memoria/entrevista_concluida.flag` existe:
   - Se **não existir**, avise ao Dr. Vinícius e inicie imediatamente o fluxo `/instalar` (`.agents/skills/instalar/SKILL.md`).
3. Se já estiver instalado, apresente um resumo de até 8 linhas com:
   - Status do conector OneDrive + RAG local;
   - Atalhos disponíveis (`/triagem-downloads`, `/revisao-cruzada`, `/absorver-claudio`);
   - Pergunte qual caso ou frente (`Jurídico`, `Comercial`, `Administrativo` ou `Financeiro`) vamos atacar agora.
