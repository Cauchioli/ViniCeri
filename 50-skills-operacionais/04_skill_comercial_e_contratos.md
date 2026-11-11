# Skill 04: Inteligência Comercial, Consultas, Contratos e Distratos

- **Pilar:** Comercial (`20-comercial`)
- **Operadores:** Dr. Vinícius Cerineo e André
- **Arquitetura Integrada:** Esteira Comercial e Passagem de Bastão + Fluxo de Áudio/NotebookLM e Análise de Contratos do Dr. Vinícius Cerineo.

---

## 1. Fluxo 1: Do Atendimento (Áudio / Anotação / NotebookLM) para o Relatório e Pasta
1. Quando o Dr. Vinícius ou o André realizarem um atendimento (presencial ou via áudio de WhatsApp) e jogarem a transcrição do NotebookLM ou relato falado no chat:
   - Extrair **Resumo Fático Cronológico**, **Diagnóstico Jurídico Preliminar**, **Lista de Documentos Necessários** e **Estratégia Recomendada**.
   - Gerar mensagem pronta para enviar ao cliente no WhatsApp solicitando a documentação pendente.
   - Gerar o bloco de texto pronto para colar nos **Comentários do ADVBOX**.

## 2. Fluxo 2: Precificação Baseada no Histórico do OneDrive e Proposta de Honorários
1. Consultar no RAG local os contratos de honorários anteriormente fechados pelo escritório no OneDrive para casos similares.
2. Sugerir faixa de precificação (honorários iniciais fixos, parcelamento, êxito final ou assessoria mensal para `Clientes Fixos`) e gerar a **Minuta do Contrato de Honorários e Procuração** já no Papel Timbrado oficial.

## 3. Fluxo 3: Termos de Distrato, Quitação e Aditivos em 2 Minutos
1. Quando um cliente desistir de ingressar com a ação ou encerrar etapa consultiva (pagando apenas a consulta/parecer inicial):
   - Ler o histórico da pasta do cliente no OneDrive;
   - Localizar modelo de distrato/quitação na pasta `Modelos`;
   - Gerar o **Termo de Distrato e Quitação Recíproca** no Papel Timbrado oficial, discriminando os serviços prestados até o momento, dando quitação do valor já pago e exonerando ambas as partes de cobranças ou obrigações futuras.
