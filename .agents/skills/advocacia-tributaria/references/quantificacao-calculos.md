# Quantificação e Simulação de Cenários Tributários

Este módulo define as regras matemáticas de cálculo de descontos, amortização com créditos contábeis e simulações de fluxo de caixa para transações fiscais perante a PGFN e a Receita Federal.

---

## 1. COMPOSIÇÃO DA DÍVIDA E BASE DESCONTÁVEL

Uma dívida tributária federal inscrita em Dívida Ativa da União é composta por:

$$\text{Dívida Total} = \text{Tributo Principal} + \text{Multa (Mora/Ofício)} + \text{Juros de Mora (Selic)} + \text{Encargos Legais (DL 1.025/69)}$$

### A Regra de Desconto
1. **Principal**: O valor do tributo principal **não pode sofrer descontos** (impedimento constitucional de renúncia de receita fiscal sem lei específica de anistia).
2. **Encargos e Acessórios**: A multa, os juros e os encargos legais constituem a **Base Descontável** (geralmente representa cerca de **33% do passivo consolidado**).
3. **Teto de Desconto**: O desconto nominal anunciado pela transação (ex: 65% ou 70%) aplica-se **exclusivamente** sobre a Base Descontável.

### Fórmula do Desconto Real Efetivo
Para apurar a redução real sobre o valor bruto que o cliente de fato pagará:

$$\text{Desconto Real Efetivo} = \text{Desconto Teórico da Transação (ex: 65\%)} \times \frac{\text{Base Descontável}}{\text{Dívida Total}} \times \text{Fator Histórico de Rescisões}$$

---

## 2. FATOR HISTÓRICO DE RESCISÕES (LEI 14.690/2023)

O histórico de cumprimento de acordos anteriores do contribuinte penaliza a nova transação. A skill deve aplicar o seguinte fator redutor sobre o desconto teórico antes de prosseguir com a simulação:

| Perfil do Devedor | Acordos Rompidos (últimos 36 meses) | Fator Aplicado sobre o Desconto |
|---|---|---|
| **Reincidente Leve** | 1 a 2 rescisões | **85%** |
| **Reincidente Médio** | 3 a 5 rescisões | **65%** |
| **Reincidente Pesado** | 6 a 9 rescisões | **45%** |
| **Devedor Contumaz** | Classificação formal (Lei 14.690/2023) | **20%** |

*Exemplo Prático (Empresa ABC)*:
- Dívida total: R$ 31.178.680,39 (composta por 67,23% Principal e 32,77% encargos).
- Desconto anunciado no Edital: 65%.
- Histórico do cliente: 9 rescisões de acordos.
- Desconto real efetivo = $65\% \times 32,77\% \times 45\% = 9,58\%$.
- Saldo final após desconto: R$ 28,1M (redução de apenas 9,6% sobre o passivo total).

---

## 3. AMORTIZAÇÃO COM PREJUÍZO FISCAL E CSLL (BCN)

A Lei 14.375/2022 permite o uso de prejuízo fiscal de IRPJ e de base de cálculo negativa (BCN) de CSLL para amortizar parcelas de transações tributárias:

1. **Moeda de Pagamento**: Créditos acumulados de prejuízos fiscais podem quitar saldo devedor.
2. **Limite**: O uso de PF/BCN é limitado a **no máximo 70%** do saldo da transação que restou após a aplicação dos descontos.
3. **Requisito Contábil**: Os valores de prejuízo fiscal devem estar devidamente escriturados no LALUR (Livro de Apuração do Lucro Real) da empresa devedora (ou de empresa do mesmo grupo econômico sob condições específicas).

---

## 4. CLASSIFICAÇÃO DE CAPAG E RECLASSIFICAÇÃO POR APORTE

A capacidade de pagamento (CAPAG) estimada pela PGFN define a elegibilidade de descontos.
- **CAPAG A e B**: Considerados devedores com alta/média recuperabilidade. Acesso limitado a descontos e prazos curtos.
- **CAPAG C e D**: Considerados devedores de difícil recuperação. Acesso a descontos máximos e prazos estendidos (até 120 ou 145 meses).

### Reclassificação Estratégica via Aporte
Quando há um investidor interessado (M&A):
1. O investidor demonstra a intenção de realizar aporte de capital na empresa.
2. A PGFN recalcula a CAPAG da empresa com base no novo fluxo financeiro planejado.
3. Isso pode reclassificar a empresa de C para B, abrindo a possibilidade de uma Transação Individual Personalizada com descontos estruturados de acordo com o plano de recuperação viável, diminuindo o saldo total e melhorando a parcela mensal (conforme Cenários 2 e 3 da proposta).
