# Skill 02: Triagem Automática de Downloads, Abertura no OneDrive e Card ADVBOX

- **Pilar:** Administrativo & Jurídico (`00-triagem-downloads` / `30-administrativo`)
- **Operadores:** Dr. Vinícius Cerineo e Beatriz (Bia)
- **Objetivo:** Eliminar o gargalo de casos que chegam pelo WhatsApp do Dr. Vinícius e ficam sem cadastro no **ADVBOX** ou espalhados na pasta `Downloads`.

---

## 1. Quando Acionar (`/triagem-downloads`)
Sempre que o Dr. Vinícius (ou o André/Bia) baixar documentos, PDFs, contratos, imagens ou áudios do WhatsApp na pasta `Downloads` (mesmo que sejam de 3 ou 4 clientes diferentes misturados).

## 2. Passo a Passo de Execução da IA
1. **Leitura e Agrupamento:**
   - Inspecione os arquivos recentes na pasta `Downloads` (ou na pasta indicada).
   - Leia o conteúdo dos PDFs, Word, imagens e transcrições de áudio para identificar a qual **Cliente / Caso** pertence cada arquivo.
2. **Apresentação do Plano de Organização (`DE -> PARA`):**
   - Liste para o Dr. Vinícius os grupos identificados:
     - **Cliente / Caso Identificado**
     - **Pasta Existente no OneDrive** (ou sugestão de nova pasta sequencial em `Processos` / `Clientes Fixos`)
     - **Lista de Documentos Numerados** (`01_RG_CPF...`, `02_Matricula_Imovel...`, `03_Contrato...`)
     - **Documentos Faltantes** (o que ainda precisa cobrar do cliente no WhatsApp, com sugestão de prazo `D+3`).
3. **Geração da Ficha de Cadastro para a Bia no ADVBOX:**
   - Gere automaticamente na pasta do caso o arquivo `00_CADASTRO_ADVBOX_BIA.md` contendo:
     - **Nome Completo do Cliente e Partes Contrarias**
     - **Telefone / WhatsApp**
     - **Grupo de Ação e Tipo de Ação** (Judicial ou Extrajudicial)
     - **Resumo do Caso para os Comentários do ADVBOX** (para que qualquer pessoa da equipe saiba exatamente onde o caso parou sem precisar perguntar)
     - **Checklist de Tarefas Padrão ADVBOX:**
       - [ ] Cadastrar todas as partes no ADVBOX
       - [ ] Digitalizar / validar documentos na pasta do OneDrive
       - [ ] Criar número de pasta na sequência (`Processos`)
       - [ ] Lançar valor financeiro / honorários e despesas iniciais
       - [ ] Agendar tarefa de cobrança de documentos faltantes (`D+3`) ou prazo de elaboração da peça para André / Danilo / Fernando.
