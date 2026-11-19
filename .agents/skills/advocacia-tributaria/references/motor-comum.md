# Motor Comum — Sistema de Raciocínio Tributário

Este módulo unifica os padrões metodológicos de análise, intake, classificação estratégica, avaliação de riscos, estrutura de redação e checklist de revisão para todas as demandas tributárias federais.

---

## 1. FLUXOS DE TRABALHO E URGÊNCIA

Antes de iniciar qualquer análise, a skill deve registrar o fluxo de trabalho aplicável de acordo com o prazo:

| Fluxo | Critério de Entrada | Registro Obrigatório | Consequências Processuais |
|---|---|---|---|
| **Completo** | Sem prazo iminente de execução ou vencimento | (Nenhum) | Execução sequencial obrigatória de todos os modos (DIAGNÓSTICO → ESTRATÉGIA → MINUTA → REVISÃO). |
| **Abreviado** | Prazo processual inferior a 5 dias úteis ou eCAC parcial | `[FLUXO ABREVIADO]` | Priorização de teses centrais, semáforo de suficiência documental e mapeamento de lacunas. |
| **Emergencial** | Prazo hoje / Execução Fiscal com penhora BACENJUD ativa / Leilão judicial amanhã | `[FLUXO EMERGENCIAL]` | Grau de confiança BAIXO automático. Produção de defesa para stay emergencial e carimbo de REVISÃO obrigatória imediata. |

---

## 2. INTAKE ESTRUTURADO (MAPEAMENTO TRIBUTÁRIO)

A skill nunca prossegue sem preencher o cadastro de passivo:

```markdown
### CADASTRO DE PASSIVO FISCAL
- Contribuinte: [Razão Social / CNPJ]
- Passivo total PGFN: R$ [Valor] (CDAs: [Quantidade])
- Débitos em aberto RFB (DCTFWeb): R$ [Valor] (Competências: [Quantidade])
- Classificação CAPAG declarada: [A/B/C/D]
- Histórico de acordos rompidos: [Quantidade] nos últimos 36 meses
- Proporção Principal × Encargos: [ex: 67% principal, 33% encargos]
- Prejuízo Fiscal / CSLL no LALUR: R$ [Valor]
- Sócio sob Risco Penal: [Sim/Não] (INSS retido: R$ [Valor])
- Situação processual crítica: [ex: 3 CDAs ajuizadas com bloqueio de contas]
```

---

## 3. QUADRANTE ESTRATÉGICO FISCAL

A skill classifica o caso em um quadrante cruzando **Complexidade Societária (Societária/M&A vs. Pura Renegociação)** com **Urguência de Bloqueio Patrimonial (Baixa vs. Alta)**:

```
                  Complexidade Societária
                    societária / M&A
                           ▲
                           │
       Q3: SANEAMENTO PRÉ-M&A   │ Q4: RECUPERAÇÃO JUDICIAL
       E TRANSAÇÃO INDIVIDUAL   │ E ALIENAÇÃO DE UPI
       - Foco: Reclassificar    │ - Foco: Proteção total,
         CAPAG, aporte de      │   blindagem de comprador,
         recursos e TPI.        │   Tema 122 STF, stays.
                           │
 ──────────────────────────┼───────────────────────────► Urgência
                           │                             de Bloqueio
       Q1: TRANSAÇÃO POR    │ Q2: DEFESA EM EXECUÇÃO
       ADESÃO (EDITAIS)     │ FISCAL E STAY EMERGENCIAL
       - Foco: Acordos via  │ - Foco: Exceção de pré-
         Regularize, editais│   executividade, embargos
         PGDAU, parcelamento.│   garantia, MS.
                           │
                           ▼
                          pura
```

---

## 4. AVALIAÇÃO DE RISCO EM 4 DIMENSÕES

Todo diagnóstico deve quantificar o risco para cada cenário nas seguintes dimensões (escala de 1 a 5, onde 5 é o risco mais grave):

1. **Risco de Caixa (RC)**: Impacto imediato no fluxo de caixa mensal da empresa (parcelas mínimas do acordo).
2. **Risco Societário (RS)**: Risco de sucessão tributária em caso de venda de ativos ou cotas (CTN art. 132/133).
3. **Risco Patrimonial (RP)**: Probabilidade de penhora online, restrição de veículos, leilão de imóveis ou redirecionamento ao CPF do sócio (art. 135 CTN).
4. **Risco Penal (RN)**: Probabilidade de oferecimento de denúncia criminal contra os sócios-administradores por crimes fiscais (art. 168-A CP).

---

## 5. REVISÃO FORENSE TRIBUTÁRIA EM 6 CAMADAS

A revisão final antes do protocolo segue as seguintes camadas:

1. **Camada Fática**: Toda informação sobre CDAs, valores, datas e parcelas confere com o eCAC e Regularize?
2. **Camada Quantitativa**: Os cálculos de desconto real, parcelamento mínimo e créditos de Prejuízo Fiscal estão corretos?
3. **Camada Legal**: Os artigos de leis (ex: Lei 13.988, Lei 11.101) e portarias de transação da PGFN citados estão vigentes e consolidados?
4. **Camada de Bifurcação Processual**: A decisão entre Mandado de Segurança × Ação Ordinária com Tutela foi tecnicamente justificada no corpo da peça?
5. **Camada Societária**: O impacto de sucessão tributária está mitigado de acordo com a estrutura escolhida (Share/Asset/UPI)?
6. **Camada Anti-Alucinação**: Existe algum campo `[VERIFICAR]` ou placeholder pendente na minuta?
