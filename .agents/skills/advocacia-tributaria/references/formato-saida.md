# Padrões de Formato de Saída (Output) — Skill Tributária

Este módulo disciplina a entrega visual e o nível de detalhamento estrutural exigido para cada modo de operação.

---

## 1. MODO TRIAGEM (MAPA DE ENTRADA)

A saída no modo `TRIAGEM` deve apresentar a seguinte estrutura:

```markdown
# [TRIAGEM] — [NOME DO CONTRIBUINTE]
- **Código de Prática**: `TRANS` / `TRIB` / `RJ` / `MA` / `PEN` / `EXEC`
- **Gravidade do Passivo**: BAÌXA / MÉDIA / ALTA
- **Risco de Caixa imediato**: SIM / NÃO
- **Risco Penal**: SIM / NÃO

### Resumo do Caso
[Breve resumo dos fatos identificados em 3 parágrafos]

### Decisão de Admissão
[Recomendação explícita: Prosseguir / Recusar / Redesenhar mandato]
```

---

## 2. MODO DIAGNÓSTICO (MATRIZ DE CENÁRIOS)

A saída no modo `DIAGNÓSTICO` deve apresentar a matriz de simulação de cenários em tabela estruturada, seguida das lacunas identificadas:

```markdown
# [DIAGNÓSTICO] — MATRIZ DE CENÁRIOS DE REGULARIZAÇÃO

| # | Cenário | Redução Est. (%) | Saldo Refinado (R$) | Parcela Mensal Est. (R$) | Prós | Contras |
|---|---|---|---|---|---|---|
| **0** | Status quo (Manter parcelamentos simplificados) | < [X]% | R$ [X] | R$ [X] | Nenhuma alteração contratual | Risco de rescisão e execução imediata |
| **1** | Transação Adesão / Individual sem Aporte | [X]% | R$ [X] | R$ [X] | Simplicidade operacional | Desconto limitado pela CAPAG atual |
| **2** | Transação Individual com Aporte de Capital | [X]% | R$ [X] | R$ [X] | Reclassificação de CAPAG | Exige investidor estruturado |
| **3** | Transação + Uso de Prejuízo Fiscal / CSLL | [X]% | R$ [X] | R$ [X] | Amortização de até 70% | Exige contabilidade auditada |
| **4** | Transação em Recuperação Judicial | [X]% | R$ [X] | R$ [X] | Desconto máximo automático | Processo de RJ custoso e complexo |
| **5** | RJ com leilão de UPI | [X]% | R$ [X] | R$ 0 (massa) | Blindagem total contra sucessão | Alienação do controle operacional |

### Lacunas Críticas Identificadas
1. [ex: Extrato eCAC incompleto de competências do IRPJ]
2. [ex: Falta memória do LALUR para prejuízo fiscal]
```

---

## 3. MODO ESTRATÉGIA (O GATE MS × ORDINÁRIA)

No modo `ESTRATÉGIA`, a skill deve justificar a escolha estratégica processual e detalhar a arquitetura da peça:

```markdown
# [ESTRATÉGIA] — CURSO DE AÇÃO SELECIONADO
- **Caminho Primário**: Transação Individual / Defesa Processual
- **Gate Strategic**: Mandado de Segurança × Ação Ordinária com Tutela

### Fundamentação da Bifurcação Processual
> **Escolha**: [MS / Ordinária]
> **Razão**: [Apresentar por que o MS é ou não aplicável, demonstrando a necessidade de dilação probatória ou urgência de honorários]

### Arquitetura da Peça (Estrutura)
1. **Preliminar**: [ex: Inelegibilidade subjetiva do edital]
2. **Mérito 1**: [Tese de composição das CDAs]
3. **Mérito 2 (Subsidiária)**: [Tese de descaracterização da mora]
4. **Pedido de Stay**: [Pedido de suspensão da execução fiscal]
```
