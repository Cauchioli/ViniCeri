# _meta — Fonte Única de Estado

*Arquivo de controle. Carregar em MANUTENÇÃO. Consultar no início de qualquer sessão de evolução da skill.*

---

## Versão

**v1.0** — versão inicial. Skill autônoma de advocacia bancária (eixo cliente × instituição financeira, com módulo secundário de defesa da instituição), derivada metodologicamente de uma arquitetura de sistema jurídico, sem identidade do escritório de origem.

## Princípio de estado

Este arquivo é a **única fonte de verdade** sobre versão e maturidade dos módulos. Qualquer divergência entre o que outro arquivo afirma e o que está aqui resolve-se a favor deste arquivo. Atualizar aqui ao fechar sessão de manutenção.

## Maturidade dos módulos

Escala: `ESQUELETO` (estrutura + método, sem repertório calibrado em caso real) → `EM USO` (validado contra ao menos um caso real) → `MADURO` (validado contra múltiplos casos, com lições incorporadas).

| Módulo | Maturidade | Observação |
|---|---|---|
| motor-comum.md | ESQUELETO | núcleo metodológico estável |
| SKILL.md (orquestração) | ESQUELETO | 6 modos + gates + eixo consumidor/instituição |
| fundamentos-bancarios.md | ESQUELETO | base CDC + Súmula 297/ADI 2.591 |
| revisional-contratos.md | ESQUELETO | premissa falsa dos 12% combatida; taxa média BCB como parâmetro |
| credito-consignado.md | ESQUELETO | margem, RMC/cartão consignado |
| busca-apreensao.md | ESQUELETO | DL 911/69 c/ Lei 13.043/2014 — purgação/pagamento integral |
| titulos-execucao.md | ESQUELETO | CCB; embargos; exceção de pré-executividade |
| negativacao-cadastros.md | ESQUELETO | Súmulas 385 e 359 como gates |
| fraudes-golpes.md | ESQUELETO | Súmula 479 estável; fronteira fortuito interno × culpa exclusiva DATADA — [VERIFICAR] |
| superendividamento.md | ESQUELETO | Lei 14.181/21; mínimo existencial controvertido — [VERIFICAR] |
| defesa-instituicao.md | ESQUELETO | eixo invertido — ônus e tese do banco |
| judicializacao.md | ESQUELETO | JEC × vara comum; inclui camada de recursos |
| pericia-contabil-impugnacao.md | ESQUELETO | metodologia substantiva — crítico |
| prova-e-documentos.md | ESQUELETO | contrato, extratos, planilha, prints, SCR |
| perfil-julgador.md | ESQUELETO | preencher com experiência local (JEC/vara/Turma) |
| perfil-operador.md | TEMPLATE | preencher antes do primeiro uso autoral |

## Regra de não-acoplamento

A skill não tem dependência de versão com nenhum sistema externo, SaaS, ou outra skill. Evolui isoladamente.

## Itens voláteis sob vigilância (revisar a cada uso)

Estes pontos mudam por fato externo, não por decisão do operador. Sempre reconfirmar via fonte oficial / web antes de afirmar em peça:

1. **Taxa média de mercado (BCB)** — divulgada mensalmente por modalidade; é o parâmetro objetivo de abusividade. Sempre buscar a da modalidade e do período do contrato.
2. **Salário mínimo / mínimo existencial** — o salário mínimo muda anualmente; o mínimo existencial do superendividamento (Decreto 11.150/22, alterado pelo Decreto 11.567/23) tem valor/critério controvertido e em debate de constitucionalidade. *[VERIFICAR]*
3. **Fraude/golpe — fronteira fortuito interno × culpa exclusiva da vítima / fortuito externo** — Súmula 479/STJ estável; a fronteira é móvel e decidida caso a caso (jurisprudência STJ 2025-2026 em evolução). Reconfirmar o estado antes de afirmar responsabilidade. Ver `fraudes-golpes.md`.
4. **Consignado no cálculo do mínimo existencial** — ponto quente em definição no STF (notícia de fonte secundária, abr/2026) — tratar como `[VERIFICAR alta prioridade]`, não cravar. Ver `superendividamento.md`.
5. **Comissão de permanência** — extinta por resolução do CMN a partir de marco regulatório; conferir a data do contrato e a redação da resolução vigente. *[VERIFICAR marco]*
6. **Tarifas (TAC/TEC, cadastro) — Tema 618/STJ** — marco temporal de 30/04/2008 distingue o tratamento; conferir a data do contrato. *[VERIFICAR]*
