# Leis de Operação, Redação e Governança Institucional: Escritório Dr. Vinícius Cerineo

Este documento estabelece as leis universais e inegociáveis para qualquer agente de inteligência artificial (Claude Code, Codex CLI, Antigravity) ou colaborador atuando no ecossistema do escritório do **Dr. Vinícius Cerineo**.

---

## 1. Princípio da Validação Humana e Nota de Raciocínio Obrigatória
1. Nenhuma peça processual, contrato, notificação extrajudicial ou parecer é protocolado ou enviado ao cliente sem a validação final do Dr. Vinícius Cerineo (ou do advogado responsável designado).
2. **Padrão Duplo de Entrega (Peça + Resumo de Raciocínio):** Toda minuta gerada pela equipe (André, Danilo) ou pela IA deve ser salva na pasta correspondente do **OneDrive** acompanhada do arquivo `[NOME_DA_PECA]_RACIOCINIO.md`, contendo em até 15 linhas:
   - O que aconteceu no processo / caso até aqui;
   - Qual linha estratégica foi adotada e por quê;
   - Quais documentos da pasta do cliente foram utilizados e numerados;
   - Quais pontos exigem atenção especial do Dr. Vinícius na revisão.

---

## 2. Fidelidade ao Papel Timbrado Oficial (OneDrive -> Pasta `Modelos`)
1. Toda peça jurídica, contrato ou notificação em `.docx` deve utilizar estritamente o **Papel Timbrado oficial** localizado na subpasta `Modelos` do **OneDrive** do escritório.
2. **Preservação Tipográfica:** Manter a fonte serifada padrão do timbrado (família Times New Roman moderna do escritório), alinhamento justificado, espaçamento, formato de endereçamento, recuo de citações e rodapé institucional.
3. **Proibição de Emojis e Travessões Soltos:** É terminantemente proibido o uso de emojis em peças, contratos e relatórios, bem como o uso de travessões soltos como separadores de frases (utilizar vírgulas, dois-pontos ou parênteses).

---

## 3. Rigor Técnico, Probatório e Documental
1. **Validação Compulsória de Vigência e Temas Vinculantes:**
   - Nenhum artigo de lei, súmula ou tema de repercussão geral/repetitivo (ex.: Tema 1348 do STF sobre ITBI) pode ser citado sem verificação de vigência e aderência fática ao caso.
   - Zero jurisprudência inventada: quando houver necessidade de julgados específicos além do acervo local, sinalizar expressamente `[INSERIR/VALIDAR JULGADO TRIBUNAL COMPETENTE]` ou consultar fonte oficial verificável.
2. **Menção Obrigatória de Folhas/IDs e Documentos:**
   - Em manifestações, réplicas, contestações e recursos, indicar o número das folhas (`fls. XX`) ou IDs dos autos eletrônicos.
3. **Numeração Sequencial de Documentos (Padrão Vértice OS):**
   - Os documentos probatórios citados na peça devem ser numerados e nomeados na pasta do cliente no OneDrive exatamente na ordem em que aparecem no texto (`01_Procuracao_e_Documentos`, `02_Contrato_...`, `03_Notificacao_...`).
4. **Nomenclatura Padronizada no OneDrive:**
   - Minutas devem ser salvas com identificação clara para busca semântica no RAG: `[CLIENTE]_[TIPO_DE_PECA_OU_CONTRATO]_[TESE_PRINCIPAL]_[AUTOR_OU_STATUS].docx`.

---

## 4. Segurança, Sigilo e Isolamento no OneDrive (LGPD)
1. **Isolamento Financeiro e Societário:**
   - Pastas de controle financeiro interno do escritório (geridas pelo Dr. Vinícius e pela Gabi) e documentos societários internos permanecem isolados quando o sistema operar nas estações da equipe técnica.
2. **Acesso Operacional:**
   - O RAG local consulta as pastas `Clientes Fixos`, `Processos` e `Modelos` do OneDrive, além do histórico importado em `90-historico-importado/` e das skills em `50-skills-operacionais/`.
