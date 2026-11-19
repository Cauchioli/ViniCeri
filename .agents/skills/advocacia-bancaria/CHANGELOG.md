# CHANGELOG — advocacia-bancaria

Formato: registro por versão. Toda alteração de módulo, gate, sub-skill ou repertório passa por aqui. Versionamento independente — sem acoplamento a SaaS ou a outra skill.

---

## v1.0 — versão inicial

**Origem.** Skill autônoma de advocacia bancária, derivada metodologicamente de uma arquitetura de sistema jurídico de escritório. **Nenhuma identidade, dado, benchmark ou repertório do escritório de origem foi transportado** — apenas a dinâmica (método, gates, anti-alucinação, tensionamento, disciplina de modo). Destinada a uso genérico por qualquer operador, mediante preenchimento do `perfil-operador.md`.

**Escopo.** Eixo primário: cliente/consumidor × instituição financeira. Eixo secundário reescopável: defesa da instituição (`defesa-instituicao.md`), com ônus e tese invertidos. Áreas: fundamentos (FUND), revisional (REV), consignado (CONS), busca e apreensão (BAF), execução (EXEC), negativação (NEG), fraudes/golpes (FRA), superendividamento (SEND), defesa da instituição (DEF), judicialização/recursos (JUD/REC).

**Adicionados — núcleo metodológico (reescrito para o domínio bancário):**
- `SKILL.md` — orquestração: Intenção Estratégica (Auftragstaktik), 6 modos + camada EXECUTIVO, Passos 0–4-A, thresholds, gates anti-pulo-de-mapa, hierarquias de autoridade (consumidor bancário; alienação fiduciária; superendividamento), regras globais.
- `references/motor-comum.md` — §0 anti-alucinação bancário (níveis de confiabilidade, controle de dados/normas, taxa média BCB como parâmetro), fluxos, intake por área, mapa/quadrante, risco, arquitetura, redação, checklist, gate, híbridos (com regra "lado primeiro").
- `references/formato-saida.md` — graus de confiança calibrados (revisional sem cotejo BCB nunca > BAIXO; fraude sem fronteira nunca > MÉDIO); datas-chave bancárias; blocos por modo.
- `references/intencao-estrategica-por-modo.md` — Auftragstaktik por modo, exemplos bancários.
- `references/pesquisa-jurisprudencial.md` — hierarquia STF/STJ bancária; Gate de Enriquecimento; Devil's Advocate; §4 casos-sentinela.
- `references/revisao-forense.md`, `padroes-argumentativos.md`, `precedentes-distinguishing-overruling.md`, `seguranca-ingestao.md` — reescritos com exemplos bancários.
- `references/sub-skills/` — `_schema.md`, `devils-advocate.md`, `tensionamento-adversario.md`, `juiz-externo.md` (instituição financeira como adversário; planilha como prova).
- `references/_meta.md`, `_licoes-aprendidas.md`, `perfil-operador.md`, `perfil-julgador.md`, `prova-e-documentos.md`.

**Adicionados — módulo crítico e domínio:**
- `references/pericia-contabil-impugnacao.md` — **módulo de maior valor e maior risco de uso ingênuo.** Impugnação metodológica da planilha de evolução da dívida e do laudo contábil; premissa válida × derrubável; recálculo verificável.
- 10 módulos de área (FUND, REV, CONS, BAF, EXEC, NEG, FRA, SEND, DEF, JUD/REC).

**Postura anti-alucinação (cross-skill).** Toda Súmula/Tema/REsp/Resolução e toda taxa entram com `[VERIFICAR]` até conferência em fonte oficial (STF/STJ/BCB). Premissa FALSA combatida ativamente: "juros acima de 12% a.a. são abusivos" (Súmula 596/STF; REsp 1.061.530/RS). Parâmetro real de abusividade: taxa média de mercado do BCB da modalidade/período.

**Pontos voláteis datados (verificação em jun/2026 — reconfirmar a cada uso):**
1. **Fraude/golpe** — Súmula 479/STJ (fortuito interno) estável; fronteira fortuito interno × culpa exclusiva/fortuito externo MÓVEL (jurisprudência STJ 2025-2026). Conta-destino: Res. BCB 4.753/2019.
2. **Superendividamento** — Lei 14.181/21 vigente; mínimo existencial (Decreto 11.150/22, alt. 11.567/23) controvertido; inclusão do consignado no mínimo existencial = `[VERIFICAR alta prioridade]` (decisão STF abr/2026 de fonte secundária — não cravar).
3. **Revisional/tarifas/comissão de permanência** — Tema 618 (marco 30/04/2008); comissão de permanência extinta por resolução do CMN (conferir marco); capitalização válida se pactuada (Súmulas 539/541; RE 592.377).

**Maturidade.** Todos os módulos em `ESQUELETO` (estrutura + método, sem calibragem em caso real). Ver `_meta.md`.

**Pendências para o operador.** Preencher `perfil-operador.md` (voz/repertório) e o slot local de `perfil-julgador.md`. Validar identificadores em fonte oficial no primeiro uso. Incorporar lições reais via `_licoes-aprendidas.md` (slot L-003 do domínio aberto).
