---
name: instalar
description: >
  Conduz a instalação guiada passo a passo do Vértice OS no computador do Dr. Vinícius Cerineo:
  absorve tudo que está na pasta CLAUDIO (skills criadas + histórico exportado do ChatGPT e Claude),
  conecta e indexa o OneDrive do escritório no RAG local, e conduz uma entrevista estratégica
  passo a passo (uma pergunta por vez) para calibrar toda a operação da equipe (André, Bia, Danilo,
  Fernando e Gabi) e do ADVBOX.
---

# `/instalar`: Setup Completo, Absorção da Pasta CLAUDIO, Conexão OneDrive e Entrevista Guiada

Use este fluxo sempre que o Dr. Vinícius Cerineo iniciar a instalação, pedir para configurar o sistema ou digitar `/instalar`.

---

## FASE 1: Varredura Automática da Pasta `CLAUDIO` e do `OneDrive` (Executar Primeiro!)

Antes de fazer qualquer pergunta ao Dr. Vinícius, execute os 2 scripts abaixo no terminal para descobrir tudo o que já existe na máquina dele:

```bash
python scripts/ingerir_pasta_claudio_e_historico.py
python scripts/scanner_onedrive.py
```

Em seguida, leia os arquivos gerados:
1. `50-skills-operacionais/00_CATALOGO_UNIFICADO_SKILLS.md`
2. `90-historico-importado/00_INDICE_GERAL_HISTORICO_IA.md`
3. `_memoria/raiox_onedrive.md`

### Se a pasta `Cláudio` ou o `OneDrive` estiver em um caminho diferente do padrão:
Caso algum dos dois scripts avise que não encontrou a pasta automaticamente, pergunte primeiro ao Dr. Vinícius:
> "Dr. Vinícius, para eu puxar tudo sem perder nenhum arquivo: confirme para mim onde está salva a pasta `Cláudio` (com as skills e o JSON exportado do Claude/ChatGPT) e qual é o caminho da pasta do escritório no `OneDrive`?"
E rode novamente passando o caminho entre aspas:
```bash
python scripts/ingerir_pasta_claudio_e_historico.py "CAMINHO_DA_PASTA_CLAUDIO"
python scripts/scanner_onedrive.py "CAMINHO_DO_ONEDRIVE"
```

---

## FASE 2: Apresentação do Diagnóstico Absorvido

Apresente ao Dr. Vinícius um resumo claro e objetivo do que você já integrou:
- Quantas skills/arquivos pré-existentes da pasta **`Cláudio`** foram incorporados em `50-skills-operacionais/skills_importadas_claudio/`;
- Quantas conversas e projetos exportados do **ChatGPT Web** e do **Claude Web** (`conversations.json`, `projects.json`, `memories.json`) foram classificados nos 4 pilares (`10-juridico`, `20-comercial`, `30-administrativo`, `40-financeiro-restrito`);
- Confirmação da estrutura detectada no **OneDrive** (`Clientes Fixos`, `Processos`, `Modelos` com o Papel Timbrado em Word, e `Despesas de Clientes`).

---

## FASE 3: Entrevista Guiada Passo a Passo (1 Pergunta por Vez!)

Conduza a entrevista abaixo fazendo **UMA única pergunta por vez**, aguardando a resposta do Dr. Vinícius, aprofundando se necessário e registrando na memória antes de passar à próxima. Não repita o que já sabemos da reunião inicial (sabemos que a equipe tem André, Bia, Danilo, Fernando e Gabi, que usam ADVBOX e OneDrive com ~250 GB, e que ele usa Claude + ChatGPT).

### Pergunta 1: Estrutura do OneDrive, Papel Timbrado e Isolamento de Sigilo
> "Dr. Vinícius, vi aqui a estrutura do seu OneDrive (`Clientes Fixos`, `Processos`, `Modelos` e `Despesas de Clientes`) e o Papel Timbrado na pasta `Modelos`. Para deixarmos o buscador inteligente (RAG) 100% seguro antes de expandirmos para a equipe: além da parte financeira da Gabi, existe alguma pasta específica dentro do OneDrive que deve ficar bloqueada para os advogados/Bia, ou alguma subpasta de modelos que você considera o seu 'padrão ouro'?"

### Pergunta 2: Divisão Fina de Carteira e Peças (André, Danilo e Fernando)
> "Sobre a linha de produção jurídica com o **André**, o **Danilo** e o **Fernando**: como vocês dividem os processos hoje entre eles (por área do direito, por fase processual ou por cliente fixo vs. avulso)? E quando uma peça deles chega para você revisar, qual é o ajuste que você mais precisa fazer?"

### Pergunta 3: Fim do 'Apagar Incêndio' no WhatsApp (Passagem de Bastão com a Bia no ADVBOX)
> "Na nossa conversa ficou claro que muitos casos urgentes chegam no seu WhatsApp e acabam ficando só com você antes de a **Bia** cadastrar no ADVBOX e abrir a pasta sequencial no OneDrive. Quando você jogar os documentos/áudios do cliente na pasta `Downloads` e rodar o comando `/triagem-downloads`, além de criar a pasta no OneDrive e resumir o caso, quais campos e tarefas padrão você quer que eu já deixe mastigados para a Bia lançar no ADVBOX em 2 minutos?"

### Pergunta 4: Calibragem da Revisão Cruzada (Claude + Codex) e Top 5 Demandas
> "Integrando aquele seu método de jogar no ChatGPT e revisar no Claude (como você fazia no *Tio Rui Barbosa* e no *Perfil Técnico Jurídico*): quais são hoje os **3 a 5 tipos de peças ou contratos** que mais consomem o seu tempo pessoal (ex.: revisão de contratos de obra/parceria como CS e TSK, isenção de ITBI Tema 1348, notificação de desocupação, usucapião, inventário)? E no comando `/revisao-cruzada`, você prefere que eu sempre te mostre primeiro um cardápio curto de linhas estratégicas para você aprovar antes de eu gerar o Word no Papel Timbrado?"

### Pergunta 5: Inteligência Comercial, Propostas e Contratos de Honorários
> "Na frente **Comercial**: quando você ou o André atendem um cliente novo, como vocês definem o valor dos honorários hoje (tabela por tipo de ação, percentual no êxito, ou análise de complexidade)? Onde ficam salvos no OneDrive os contratos de honorários já fechados para eu indexar como base de precificação e gerar minutas de contrato ou termos de distrato/quitação em segundos?"

### Pergunta 6: Rotina Financeira e Administrativa (Gabi e Relatórios de Clientes)
> "Por fim, pensando na **Gabi** (Financeiro) e no relacionamento com clientes e parceiros (como o Salata): quais são as 2 tarefas mais repetitivas da Gabi na semana e como vocês fazem hoje o envio de informações de andamento para os clientes fixos e avulsos?"

---

## FASE 4: Gravação da Memória, Indexação do RAG no OneDrive e Ativação

Assim que o Dr. Vinícius responder a 6ª pergunta:
1. Atualize os arquivos em `_memoria/` (`contexto.md`, `equipe_e_fluxos.md`, `estrategia.md`, `preferencias.md`) com todas as respostas reais dele.
2. Se durante a entrevista surgir qualquer rotina específica nova, crie uma skill dedicada em `50-skills-operacionais/` e atualize `50-skills-operacionais/00_CATALOGO_UNIFICADO_SKILLS.md`.
3. Crie o arquivo `_memoria/entrevista_concluida.flag` com a data de conclusão.
4. Execute a instalação e indexação do RAG local conectado ao OneDrive:
   ```bash
   python rag/install_rag.py
   python rag/rag_acervo.py index
   ```
5. Apresente o quadro final de confirmação e proponha **1 teste prático imediato** em cima de um caso real da fila dele!
