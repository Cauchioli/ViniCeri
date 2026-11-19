# 🎙️ Bônus 1: A Ata Comercial Inteligente
*Automatizando o Diagnóstico, Triage & Onboarding de Clientes de Elite*

A reunião inicial de diagnóstico (consulta) com o cliente é o momento mais rico de informações e, ao mesmo tempo, o maior ralo de tempo do advogado. Escrever manifestações fáticas enquanto o cliente fala impede a escuta ativa e drena o foco. 

Este manual ensina a transformar um áudio bruto de reunião em um **Dossiê Comercial e Técnico de Caso** estruturado em segundos usando Inteligência Artificial (Claude ou Gemini).

---

## 🛠️ Passo 1: Captura & Transcrição
1. **Gravação:** Grave a reunião (presencial ou online pelo Meet/Zoom/Teams) utilizando o gravador do celular ou a ferramenta da própria plataforma.
   * *Regra Ética:* Informe ao cliente que, para a segurança e precisão do atendimento dele, a conversa será gravada de forma restrita e confidencial.
2. **Transcrição:** Extraia o texto do áudio. Você pode usar ferramentas automáticas como Riverside.fm, Whisper (OpenAI) ou o recurso de transcrição nativa do Teams/Zoom.

---

## 🧠 Passo 2: O Prompt de IA para Geração do Dossiê

Abra um chat privado com a IA (recomenda-se o **Claude 3.5 Sonnet** ou **Gemini 1.5 Pro** devido à alta capacidade fática e lógica), cole a transcrição da reunião e rode o prompt abaixo:

```markdown
# Role
Você é um Auditor Jurídico de Elite e Assistente Comercial Sênior do escritório de advocacia. Sua especialidade é analisar transcrições de consultas de clientes e desmembrar os fatos jurídicos de forma cirúrgica, separando a emoção do cliente dos dados fáticos reais necessários para a ação.

# Contexto
Você recebeu a transcrição bruta de uma consulta inicial realizada com um cliente. Seu objetivo é organizar esse fluxo caótico de informações em um Dossiê Técnico e Comercial unificado, que servirá tanto para alimentar a redação da Petição Inicial quanto para instruir o time comercial nas tratativas de fechamento do contrato de honorários.

# Instruções de Processamento
Analise o texto em anexo e elabore o **Dossiê Comercial e Técnico de Caso** dividido exatamente nos seguintes tópicos:

## 1. DADOS CADASTRAIS E TEMPO DE RELACIONAMENTO
Identifique e extraia do texto:
- Nome do cliente.
- Nome da parte contrária (empresa/réu).
- Período de vigência do contrato/relação de trabalho (datas exatas de início e fim, se houver).
- Último salário ou valor econômico envolvido (se citado).

## 2. RELATO FÁTICO CRONOLÓGICO (LINHA DO TEMPO)
Construa uma tabela cronológica linear de todos os eventos citados pelo cliente na reunião, seguindo a ordem dos acontecimentos (da data mais antiga para a mais recente).
Colunas da tabela: [Data / Período] | [Acontecimento / Fato Relatado] | [Pessoas Envolvidas].
*Nota: Se o cliente não citar a data exata, coloque uma estimativa baseada no contexto (ex: "Meados de 2025").*

## 3. AUDITORIA DE PROVAS E PONTOS FRACOS (RISCOS)
Analise o relato do cliente com um olhar cético (como o advogado da parte contrária faria) e aponte:
- **Contradições Internas:** Onde o cliente se contradiz em datas, valores ou condutas.
- **Lacunas de Informação:** Fatos importantes que o cliente não explicou direito ou omitiu durante o áudio.
- **Fraquezas Processuais:** Condutas do cliente que podem enfraquecer o caso (ex: demora para reclamar, falta de boletim de ocorrência, concordância com a situação em algum momento).

## 4. CHECKLIST DE DOCUMENTOS COMPROBATÓRIOS
Crie uma lista de documentos que o advogado deve solicitar ao cliente antes de assinar o contrato, associando cada documento ao fato que ele precisa provar.
Colunas da tabela: [Documento Necessário] | [Fato que Comprova] | [Status (Obtido / Solicitar)].

## 5. ENQUADRAMENTO JURÍDICO & TESES SUGERIDAS
Identifique quais são os danos reais sofridos e proponha o enquadramento de direito inicial:
- **Tese Principal:** O coração da ação (ex: rescisão indireta por assédio, indenização por acidente típico).
- **Teses Secundárias:** Pedidos acessórios (ex: danos morais por ausência de registro, horas extras).
- **Pedidos Fundamentais:** O que deve ser requerido em termos financeiros ou de obrigação de fazer.
```

---

## 📝 Exemplo Prático de Saída (Output do Dossiê)

Abaixo está um exemplo de como a IA formatará a resposta após rodar o prompt:

### 📋 DOSSIÊ COMERCIAL E TÉCNICO DE CASO
* **Cliente:** João da Silva
* **Parte Contrária:** Indústrias Metalúrgicas Alfa Ltda.

#### 1. Linha do Tempo Fática (Cronologia)
| Data | Fato Relatado | Pessoas Envolvidas |
| :--- | :--- | :--- |
| **15/03/2023** | Admissão de João na função de operador de empilhadeira. | João e RH Alfa |
| **12/08/2024** | Acidente de trabalho típico. Palete de ferro caiu sobre o pé esquerdo de João. | João e Supervisor Roberto |
| **12/08/2024** | Atendimento de emergência no hospital, sem emissão imediata de CAT pela empresa. | João e Médico plantonista |
| **15/08/2024** | João solicita a CAT ao RH. Empresa recusa emitir alegando "desatenção do funcionário". | João e RH Alfa |
| **20/09/2024** | Retorno ao trabalho após 30 dias de atestado. Rebaixado para a função de auxiliar de limpeza. | João e Supervisor Roberto |

#### 2. Auditoria de Provas & Pontos Fracos
* **Lacuna de Informação:** João diz que o Supervisor Roberto presenciou o acidente, mas não fica claro se Roberto admitiu a culpa ou se havia outros funcionários no setor que possam testemunhar.
* **Fraqueza Processual:** O rebaixamento de função ocorreu em setembro de 2024, mas João continuou trabalhando e só buscou auxílio jurídico agora (maio de 2026). A parte ré alegará perdão tácito.
* **Contradição:** João afirma que não conseguia andar após o acidente, mas a empresa possui registro de ponto assinado por ele no dia seguinte. É preciso verificar se o ponto foi assinado retroativamente.

#### 3. Checklist de Documentos a Solicitar
| Documento Necessário | Fato que Comprova | Status |
| :--- | :--- | :--- |
| **Prontuário Médico de Emergência** | O atendimento no dia do acidente e a lesão no pé. | Solicitar ao hospital |
| **Exames e Atestados Médicos** | A incapacidade temporária de 30 dias. | Já obtido (anexo) |
| **Testemunhas (Contato de ex-colegas)** | A recusa da empresa em emitir a CAT e o desvio de função. | Solicitar a João |
| **Holerites pós-setembro/2024** | Redução salarial decorrente do rebaixamento de função. | Solicitar a João |
