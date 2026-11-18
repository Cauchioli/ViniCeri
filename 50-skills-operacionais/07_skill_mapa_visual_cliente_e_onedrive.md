# Skill 07: Mapa Visual de Pasta de Cliente & Organização Leve do OneDrive (`/mapa-visual`)

> **Objetivo:** Transformar qualquer pasta de cliente ou caso no OneDrive em uma **Organização Visual Executiva e Planejamento Estratégico em HTML/PDF** de alto impacto para apresentar ao cliente em reunião, além de permitir a organização progressiva do OneDrive (~250 GB) em lotes leves sem sobrecarregar o computador.

---

## 1. Quando Acionar Esta Skill

* Quando o Dr. Vinícius disser: *"gera o mapa visual dessa pasta"*, *"faz o planejamento visual desse cliente"*, *"organiza visualmente o que tem nessa pasta do Drive para eu mostrar pro cliente"*, ou digitar `/mapa-visual`.
* Quando o Dr. Vinícius quiser organizar múltiplas pastas do OneDrive sem travar a memória ou o processador do computador atual (Modo Lote Leve).

---

## 2. Fluxo A: Mapa Visual & Planejamento Executivo de um Cliente (Imediato)

### Passo 1: Leitura Leve da Pasta do Cliente no OneDrive
1. Receba o nome do cliente/caso ou o caminho da pasta no OneDrive (`Clientes Fixos` ou `Processos`).
2. Liste os arquivos usando comando leve de diretório (sem abrir binários pesados na memória de uma só vez), identificando:
   * Contratos, escrituras, matrículas e certidões;
   * Petições iniciais, contestações, recursos e decisões;
   * Comprovantes, guias (ITBI, custas) e documentos pessoais;
   * Subpastas já organizadas na pasta do cliente.

### Passo 2: Construção do Painel HTML Executivo (Padrão Editorial Vértice OS)
Gere dentro da própria pasta do cliente (ou em `10-juridico/mapas-visuais/`) um arquivo HTML standalone (`MAPA_VISUAL_E_PLANEJAMENTO_{CLIENTE}.html`) pronto para abrir no navegador ou salvar em PDF A4 (`window.print()`), contendo:
1. **Cabeçalho Institucional Sóbrio:** Identificação do Escritório Dr. Vinícius Cerineo, nome do cliente, data e objeto do planejamento.
2. **Raio-X Visual do Acervo da Pasta (Cards de Status):**
   * Total de documentos mapeados divididos por categoria (Societário/Contratos, Processual, Imobiliário/Registral, Financeiro/Guias);
   * Indicadores visuais claros: `Documento Validado`, `Em Análise / Revisão`, `Pendente de Envio pelo Cliente`.
3. **Linha do Tempo / Arquitetura da Estratégia Jurídica:**
   * Fluxo visual em etapas numeradas (Etapa 1: Diagnóstico e Saneamento Documental; Etapa 2: Medidas Extrajudiciais/Contratuais; Etapa 3: Protocolo / Execução; Etapa 4: Blindagem e Fechamento).
4. **Árvore Visual Limpa da Pasta do Cliente:**
   * Mapa estruturado de todas as subpastas e documentos principais, permitindo que o Dr. Vinícius mostre na tela ao cliente o domínio completo sobre cada detalhe do caso.
5. **Quadro de Próximos Passos e Responsáveis:**
   * O que está com o escritório (Dr. Vinícius, André, Bia, Danilo) e o que depende do cliente.

### Design Visual Obrigatório do HTML:
* Paleta editorial jurídica de alto padrão: fundo claro `#F9F8F6`, cards `#F0ECE1`, texto `#141413`, destaque dourado/bronze sóbrio `#8C6D46`, tipografia `Cormorant Garamond` para títulos e `Plus Jakarta Sans` para leitura limpa, com botão superior **"Imprimir / Exportar PDF para o Cliente"** que desaparece automaticamente na impressão (`@media print`).

---

## 3. Fluxo B: Organização do OneDrive em Lotes Leves (Sem Travar o Computador)

Como o acervo do OneDrive possui ~250 GB e o computador não deve sofrer picos de CPU/RAM:
1. **Proibição de Varredura Bruta Simultânea pela IA:** Nunca tente ler o conteúdo interno de centenas de PDFs ou DOCX de uma só vez no contexto do modelo.
2. **Mapeamento por Metadados via Python (`scripts/scanner_onedrive.py`):**
   * O mapeamento geral do OneDrive lê apenas nomes de pastas, nomes de arquivos, datas de modificação e tamanhos (execução em poucos segundos, uso quase zero de RAM).
3. **Higienização e Organização em Lotes (Por Gaveta ou Noturno):**
   * Quando o Dr. Vinícius pedir para organizar o Drive, opere em **lotes de no máximo 5 a 10 pastas de clientes por vez** (ou gere um script `.py` determinístico para rodar à noite que apenas move/renomeia arquivos para as subpastas padronizadas `01_Documentos_Pessoais`, `02_Contratos_e_Procuracoes`, `03_Pecas_e_Processo`, `04_Guias_e_Comprovantes`, gerando um índice `INDICE_PASTA.html` em cada cliente sem depender de processamento pesado).
   * Sempre mostre a prévia da organização da pasta antes de mover arquivos definitivos, garantindo segurança total sobre os vínculos com o ADVBOX.
