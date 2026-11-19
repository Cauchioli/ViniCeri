# Schema de Sub-skill — Spec Declarativa

*Toda sub-skill em `references/sub-skills/` preenche este schema. Formato padronizado, campos obrigatórios, ordem fixa. Em conflito com este schema em matéria de FORMA de sub-skill, este vence; em conflito com SKILL.md em matéria de ARQUITETURA, SKILL.md vence.*

## Princípio

Sub-skill ≠ módulo de referência. Módulo = conhecimento sobre área/método, carregado conforme o modo. Sub-skill = operação executável sobre input específico, invocação pontual, saída estruturada. Sub-skill tem assinatura — entrada → processo → saída — análoga a uma função em código. A interface é a fronteira.

## Schema obrigatório (nesta ordem)

1. **PROPÓSITO** — uma frase: o que entra, o que sai, com que finalidade operacional.
2. **QUANDO ACIONAR** — modos compatíveis; ponto do fluxo; condições de entrada; anti-gatilhos.
3. **ENTRADA ESTRUTURADA** — itens obrigatórios; opcionais; validações sobre a entrada.
4. **PROCESSAMENTO** — o que faz internamente; inspecionável; fontes de consulta; gatilhos de desvio.
5. **SAÍDA ESTRUTURADA** — formato fixo, reconhecível como output da sub-skill.
6. **RESTRIÇÕES** — cláusulas "Não..." que evitam drift de escopo e overlap.
7. **ARTICULAÇÃO COM OUTRAS SUB-SKILLS** — sequenciamento; sobreposição evitada; cadeias típicas.
8. **CRITÉRIO DE SAÍDA** — quando o output está completo.
9. **ANTI-PADRÕES** — modos de falha + sinal de detecção + correção.
10. **NOTA DE MANUTENÇÃO** — versões, lições, articulações novas.

## Padrão de invocação

> *"Acionando sub-skill `[nome]`. Entrada: [resumo]. Output esperado: [tipo]."*
> ...
> *"Output de `[nome]` recebido. Próximo passo no modo `[modo]`: [continuação]."*

## Lista de sub-skills

| Sub-skill | Propósito | Modos |
|---|---|---|
| `devils-advocate.md` | Ataque construtivo à tese **antes** de fixada | DIAGNÓSTICO, ESTRATÉGIA |
| `tensionamento-adversario.md` | Simulação da resposta da instituição financeira à tese da casa | ESTRATÉGIA, MINUTA |
| `juiz-externo.md` | Leitura adversária após peça pronta, simulando julgador hostil | REVISÃO |
| `revisao-forense.md` *(reside em references/)* | Revisão multicamada em 6 níveis | REVISÃO |

## Regra de criação de sub-skill nova
1. Justificar não-overlap com as existentes. 2. Identificar ao menos um modo + ponto do fluxo. 3. Schema completo. 4. Bump de versão no `_meta.md`.
