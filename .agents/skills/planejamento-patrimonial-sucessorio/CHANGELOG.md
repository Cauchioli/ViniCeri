# CHANGELOG — planejamento-patrimonial-sucessorio

Registro de versões da skill. Toda alteração estrutural, criação/remoção de módulo e incorporação de lição passa por aqui. Versionamento da skill, sem acoplamento a sistemas externos.

---

## v1.0 — versão inicial

**Origem.** Skill autônoma e genérica (sem identidade de escritório), derivada metodologicamente de uma arquitetura de sistema jurídico já existente. Reaproveita integralmente a *dinâmica* — método, 6 modos, gates, anti-alucinação, tensionamento, sub-skills, governança de estado e de lições — e a reorienta para o planejamento patrimonial e sucessório e a estruturação de holdings.

**Escopo.** Domínio majoritariamente **consultivo e preventivo**: a entrega típica é uma estrutura (desenho societário-sucessório) e seus atos (contrato social, doação de quotas com usufruto, acordo de sócios, protocolo familiar, testamento) ou um parecer/memorando — não uma petição. O contencioso é derivado (defesa do planejamento).

**Eixo adversário (a diferença central em relação a domínios contenciosos).** O adversário não é um juízo presente, é **triplo e ausente**: o **Fisco** (ITCMD/ITBI/IR), os **credores** (fraude contra credores/execução, desconsideração) e os **herdeiros necessários** (legítima, inoficiosa, colação) — somados ao **tempo** (mudança legislativa). O Passo 4-A (Tensionamento Adversário) e a sub-skill `tensionamento-adversario.md` foram reescritos como tensionamento **triplo + tempo**; `perfil-julgador.md` foi reescrito como **arenas adversárias**; `juiz-externo.md` simula auditor fiscal / juízo de sucessões / credor.

**Quatro bloqueios anti-alucinação próprios do domínio** (somados ao bloqueio universal de alucinação documental):
1. Afirmar economia tributária sem confrontar a **alíquota e a base do ITCMD do estado específico** (estadual, progressivo obrigatório pós-EC 132/2023 e LC 227/2026, base = valor de mercado).
2. Afirmar imunidade de ITBI na integralização sem analisar o **Tema 796/STF** (a imunidade não alcança o valor que exceder o capital social).
3. Afirmar "blindagem" oponível a credores sem analisar **fraude/execução/desconsideração e propósito negocial** (Carf reconhece simulação).
4. Dispor em prejuízo da **legítima** dos herdeiros necessários sem o teste da inoficiosidade.

**Módulo crítico.** `references/quantificacao-tributaria-e-patrimonial.md` — valuation + cálculo de ITCMD/ITBI/IR + **teste da legítima**. É o módulo de maior valor e maior risco de uso ingênuo: a economia prometida e a exposição ignorada nascem no número.

**Inventário de arquivos (v1.0).**
- Raiz: `SKILL.md`, `CHANGELOG.md`, `MANIFESTO.md`.
- Núcleo/método: `motor-comum.md`, `intencao-estrategica-por-modo.md`, `formato-saida.md`, `pesquisa-jurisprudencial.md`, `revisao-forense.md`, `padroes-argumentativos.md`, `precedentes-distinguishing-overruling.md`, `seguranca-ingestao.md`.
- Estado/governança: `_meta.md`, `_licoes-aprendidas.md`, `perfil-julgador.md` (arenas), `perfil-operador.md` (template).
- Módulo crítico: `quantificacao-tributaria-e-patrimonial.md`.
- Documentos: `documentos-e-due-diligence.md`.
- Módulos de área: `fundamentos-holding.md` (FUND), `constituicao-holding.md` (HOLD), `planejamento-sucessorio.md` (SUC), `planejamento-tributario.md` (TRIB), `protecao-patrimonial.md` (PROT), `governanca-familiar.md` (GOV), `regime-bens-familia.md` (FAM), `patrimonio-imobiliario.md` (IMOB), `contencioso-derivado.md` (CONT).
- Sub-skills: `sub-skills/_schema.md`, `sub-skills/devils-advocate.md`, `sub-skills/tensionamento-adversario.md`, `sub-skills/juiz-externo.md`.

**Itens voláteis datados (verificação jun/2026)** — ver `_meta.md`:
- ITCMD progressivo: EC 132/2023 + **LC 227/2026 (sancionada 13/01/2026)** — base de mercado, agregação de doações, trusts; efeitos dependentes de **lei estadual** (anterioridade). A janela de antecipação é **datada**.
- ITBI: **Tema 796/STF** (excedente ao capital); **Tema 1.348/STF pendente** (atividade preponderante imobiliária); Tema 1.113/STJ (base de cálculo).
- VGBL/PGBL: **Tema 1.214/STF** (ITCMD não incide por morte) — com tentativa de reinclusão e flanco de dissimulação.
- Tributação da holding: lucro presumido × Reforma do consumo (LC 214/2025; IBS/CBS; transição 2027-2028; Lei 15.270/2025); **Carf — Acórdão 2401-012.193/2025** (simulação por falta de propósito negocial).

**Maturidade.** Todos os módulos em `ESQUELETO` (estrutura + método + âncoras verificadas; sem calibragem em caso real). Evoluem para `EM USO` e `MADURO` conforme aplicação — ver `_meta.md`.
