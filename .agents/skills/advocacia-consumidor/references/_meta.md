# _meta — Estado da Skill

*Fonte única de estado. Carregado sempre. NÃO é banco de teses: identificador aqui não vira conteúdo (regra anti-alucinação §0.2 do motor-comum).*

## Versão
v0.1.0 — base inicial despersonalizada.

## Arquivos (inventário)
| Arquivo | Estado |
|---|---|
| `SKILL.md` | maduro (orquestrador) |
| `references/motor-comum.md` | maduro |
| `references/cdc-transversal.md` | maduro |
| `references/cobranca-negativacao-indevida.md` | maduro |
| `references/formato-saida.md` | maduro |
| `references/intencao-estrategica-por-modo.md` | maduro |
| `references/_meta.md` | este arquivo |
| `CHANGELOG.md` | raiz |
| `MANIFESTO.md` | raiz |

## Maturidade por sub-área
| Sub-área | Estado |
|---|---|
| CDC transversal | implementado |
| Cobrança/negativação indevida (CNI) | implementado (bilateral) |
| Transporte aéreo | NÃO implementado (onda 2) |
| Planos de saúde | NÃO implementado (onda 2) |
| Telecom/internet | NÃO implementado (onda 3) |
| Superendividamento (Lei 14.181/21) | NÃO implementado (onda 3) |
| Bancário-consumo | NÃO implementado (onda 4 — fronteira com skill bancária dedicada) |

## Roadmap de ondas
- **Onda 2:** módulos transporte aéreo (Tema 210/STF [VERIFICAR]) e planos de saúde (Lei 14.454/22 — rol ANS [VERIFICAR]).
- **Onda 3:** telecom/internet + superendividamento.
- **Onda 4:** bancário-consumo, com fronteira declarada vs. skill bancária revisional (consumo/dano aqui; revisional/contratual lá; híbrido cross-carrega — motor-comum §9).
- **Onda 5 (infra):** sub-skills formais (devil's advocate, juiz externo, revisão forense como interface própria); módulo de pesquisa jurisprudencial dedicado; esqueleto de perfis de Turma Recursal/comarca; bateria de testes.

## Decisões canônicas (não relitigar sem novo argumento)
- Skill **despersonalizada**: sem identidade de banca, sem repertório próprio, sem template de marca, sem perfis nominados, sem acoplamento a SaaS.
- **Bilateral**: declara polo no intake; método inverte. Reversível por subtração se o uso for só-autor.
- **Anti-alucinação absoluta**: súmula/precedente só com texto conferido ou `[VERIFICAR]`. Crescimento por ondas, nunca conteúdo simulado para sub-área não implementada.
