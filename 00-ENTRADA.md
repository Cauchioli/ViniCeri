# Segundo Cérebro Jurídico & Operacional: Escritório Dr. Vinícius Cerineo

Bem-vindo ao **Vértice OS** configurado sob medida para o escritório do **Dr. Vinícius Cerineo**.
Este ecossistema unifica em um único lugar:
1. O acervo vivo do escritório no **OneDrive (~250 GB)**;
2. Todas as skills e arquivos criados na pasta **`Cláudio`** (Área de Trabalho);
3. Todo o histórico de conversas, projetos e memórias exportados do **ChatGPT Web** e do **Claude Web**;
4. A esteira de produção jurídica, revisão cruzada (**Claude + Codex**), controle do **ADVBOX** e gestão comercial/financeira.

---

## 1. Princípio de Ouro: Converta UMA Vez, Consulte Infinitas Vezes
1. **O OneDrive guarda a prova documental:** Os arquivos originais (`.pdf`, `.docx`, áudios e autos de processos em `Clientes Fixos`, `Processos`, `Modelos` e `Despesas de Clientes`) permanecem intocáveis em suas pastas de origem no OneDrive.
2. **O Segundo Cérebro guarda o índice e a inteligência ativa:** Resumos de casos, teses, skills e o histórico minerado do ChatGPT/Claude ficam organizados em notas Markdown leves, permitindo busca semântica instantânea via RAG local sem estourar o limite de tokens.

---

## 2. Mapa Organizacional dos 4 Pilares do Escritório

* `00-ENTRADA.md`: Mapa central de navegação do escritório.
* `01-REGRAS.md`: Leis inegociáveis de redação, Papel Timbrado oficial, numeração de documentos e sigilo.
* `02-PROTOCOLO-ORGANIZADOR.md`: Protocolo com lacre para organização do OneDrive e da pasta `Cláudio`.
* `03-SCHEMA.md`: Padrão de metadados das notas e peças do sistema.
* `00-triagem-downloads/`: Área de passagem para triagem automática de documentos e áudios recém-baixados do WhatsApp.
* `10-juridico/`:
  * `clientes-fixos/`: Dossiês e histórico estratégico dos clientes de assessoria recorrente.
  * `processos/`: Notas de raciocínio (`_RACIOCINIO.md`), relatórios de autos e minutas por caso.
  * `modelos-e-teses/`: Espelho indexado do Papel Timbrado e das melhores peças e teses do escritório (ex.: Tema 1348 STF ITBI, usucapião, desocupação, inventários, contratos).
* `20-comercial/`: Atas de atendimento inicial, resumos de áudios do NotebookLM, propostas em negociação e parâmetros de precificação.
* `30-administrativo/`: Checklists de abertura de caso no **ADVBOX** (para a Bia), relatórios mensais de andamento e controle de parceiros (ex.: Salata).
* `40-financeiro-restrito/`: Rotinas financeiras da Gabi, controle de despesas de clientes e contratos de honorários (pasta blindada).
* `50-skills-operacionais/`: Catálogo unificado contendo as skills do Vértice OS + todas as skills absorvidas da pasta `Cláudio` e dos projetos do ChatGPT.
* `90-historico-importado/`: Índice estruturado e notas extraídas das exportações do ChatGPT Web e do Claude Web (`conversations.json`, `projects.json`, `memories.json`).
* `rag/` e `scripts/`: Motor de busca semântica local conectado ao OneDrive e scripts de ingestão automática.

---

## 3. Comandos Principais no Dia a Dia
1. **`/instalar`**: Roda a absorção da pasta `Cláudio`, importa o histórico do ChatGPT/Claude, conecta o OneDrive e conduz a entrevista de calibragem fina.
2. **`/abrir`**: Carrega o contexto do escritório e as prioridades do dia.
3. **`/triagem-downloads`**: Lê tudo o que você acabou de baixar no `Downloads` (documentos e áudios do WhatsApp), separa por cliente, organiza no OneDrive e gera a tarefa pronta para a Bia cadastrar no ADVBOX.
4. **`/revisao-cruzada`**: Executa o método de dupla checagem (análise estratégica + redação no Papel Timbrado do OneDrive + auditoria crítica + nota `_RACIOCINIO.md`).
5. **`/absorver-claudio`**: Atualiza o sistema sempre que novos arquivos ou exportações forem colocados na pasta `Cláudio`.
