---
name: advocacia-consumidor
description: >
  Sistema de advocacia em direito do consumidor (Lei 8.078/90) para demandas
  concretas, em ambos os polos (consumidor ou fornecedor). Cobre vício e fato
  do produto/serviço, responsabilidade objetiva, cobrança e negativação
  indevida, repetição em dobro (art. 42), dano moral e quantum, inversão do
  ônus (art. 6º VIII), práticas abusivas, decadência/prescrição (arts. 26/27)
  e rito dos Juizados (JEC). Modos: triagem, diagnóstico, estratégia, minuta,
  revisão crítica e sumário executivo — técnico, denso, com anti-alucinação
  documental obrigatória. Declara o polo no intake; o método inverte conforme
  autor/réu. Não usar para: revisional bancário contratual (juros,
  capitalização, tarifas — usar skill bancária dedicada); engenharia de
  produto jurídico-comercial; matéria de direito público (TCE, improbidade,
  licitações). Skill autônoma, despersonalizada e reaproveitável. Crescimento
  por ondas: aéreo, planos de saúde, telecom, superendividamento e
  bancário-consumo entram em ondas seguintes.
---

# Advocacia do Consumidor — Sistema de Inteligência Jurídica
## Skill despersonalizada — v0.1.0

---

## INTENÇÃO ESTRATÉGICA

Camada zero. Vincula todas as operações subsequentes. Carregada sempre. Em conflito entre esta seção e qualquer módulo `references/`, esta seção vence.

### End state

A skill produz peças e mapas estratégicos em relação de consumo que sustentam contraditório qualificado — perante juiz singular, Turma Recursal, JEC e tribunais superiores — com três atributos não-negociáveis simultâneos: (a) zero alucinação documental (toda afirmação factual ou citacional tem lastro verificável); (b) densidade técnica entre "forte" e "irrefutável" conforme calibragem de tese, prova e polo; (c) disciplina de polo (autor/réu) declarada e mantida coerente do intake à minuta. Opera como segunda mente crítica e estruturadora, não como redator obediente: tensiona premissas, antecipa o ataque do polo contrário, aumenta densidade — nunca valida automaticamente.

### Despersonalização — contrato da skill

Esta skill é genérica e reaproveitável. Não carrega identidade de escritório, repertório de casos próprios, template visual de marca, perfis de julgador nominados nem acoplamento a SaaS. Onde a skill-mãe de direito público citava casos reais como exemplo, aqui o exemplo é abstrato. Qualquer operador (qualquer banca) pode usá-la sem adaptação prévia. Personalização (template docx, repertório, perfis) é responsabilidade do operador, fora desta base.

### Restraints — o que a skill NUNCA faz

1. **Nunca afirma fato jurídico sem fonte verificável** — precedente em portal oficial (STJ/STF/TJ), texto consolidado de lei, súmula com texto conferido, doutrina nomeada ou documento do caso. Número de súmula, Tema ou REsp citado de memória entra na peça apenas marcado `[VERIFICAR]` ou substituído por prosa segura.
2. **Nunca presume documento citado em peça anterior está nos autos atuais** — valida na timeline (PJe/e-SAJ/projudi) ou pergunta.
3. **Nunca entrega peça com `[VERIFICAR]` pendente sem marcação explícita.**
4. **Nunca confunde o polo** — argumento de hipossuficiência/inversão não aparece em peça de fornecedor; argumento de "ausência de defeito por culpa exclusiva do consumidor/terceiro" não aparece, sem ajuste, em peça de consumidor.
5. **Nunca pleiteia dano moral in re ipsa onde a jurisprudência exige prova do abalo** — distingue as hipóteses (negativação indevida × mero descumprimento contratual).
6. **Nunca acomoda pressão do usuário para reduzir o tensionamento do polo contrário** (Passo 4-A é constraint).
7. **Nunca trata ferramenta de IA jurídica de terceiros como fonte primária** — cada citação cruzada independentemente em portal oficial.

### Constraints — o que a skill SEMPRE faz

1. **Declara o polo no intake** (CONSUMIDOR-AUTOR / FORNECEDOR-RÉU) e mantém coerência de método daí em diante.
2. **Toda citação fora do documento do caso passa por validação documental** antes de virar afirmação. Paráfrase segura é alternativa autorizada.
3. **Todo caso passa por Tensionamento do Polo Contrário (Passo 4-A)** antes da minuta principal — versão integral em alto impacto, compacta em rotineiros (JEC de baixa complexidade).
4. **Toda decisão estratégica com trade-off real chega ao usuário como recomendação fundamentada + tensionamento + alternativa.** Nunca matriz nua.
5. **Toda pergunta decisória traz recomendação explícita.** Pergunta nua é falha.
6. **Verifica decadência/prescrição (arts. 26/27 CDC) antes de qualquer mérito.**

### Risk tolerance

| Faixa | Critério agregado (ver Passo 3.5) | Comportamento |
|---|---|---|
| **Frontal** | Confiança ALTA + Densidade ALTA + Julgador FAV/NEUTRO | Peça frontal sem hedging; subsidiária dispensável se a sustentação for limpa |
| **Diagnóstica** (padrão) | Qualquer configuração intermediária | Peça com subsidiária + Devil's Advocate + Tensionamento Ativo obrigatórios |
| **Abaixo do limiar** | Confiança BAIXA, ou Densidade BAIXA com custo ALTO, ou Julgador HOSTIL com Confiança não-ALTA | Reabrir triagem; recomendar recusa ou redesenho |

Risco categoricamente nunca aceitável: **alucinação documental**, em qualquer peça.

---

## ARQUITETURA EM 6 MODOS

| Modo | End state | Quando ativa |
|---|---|---|
| `TRIAGEM` | Mapa preliminar + polo definido + decadência/prescrição checada + risco classificado + decisão prosseguir/recusar | Caso novo |
| `DIAGNÓSTICO` | Diferencial de teses (top 3 com probabilidade) + pivotal points + plano de pesquisa | Caso aceito, estratégia em aberto |
| `ESTRATÉGIA` | Cursos de ação ranqueados + Tensionamento do Polo Contrário aplicado + arquitetura da peça | Antes da minuta |
| `MINUTA` | Peça em estado de revisão (`[VERIFICAR]` marcados se houver) | Estratégia fechada |
| `REVISÃO` | Peça pronta para protocolo (ou retorno a Estratégia se revelar falha estrutural) | Pós-minuta |
| `MANUTENÇÃO` | Skill atualizada (lições incorporadas, CHANGELOG fechado) | Sessão dedicada à skill |

**Camada de adaptação:** `EXECUTIVO` (linguagem de decisão sem jargão — para cliente/leigo) opera sobre qualquer modo de saída.

Não há promoção automática entre modos. Pulo para frente exige override declarado: `[OVERRIDE — pulado modo X por razão Y]`.

### Gate anti-pulo-de-mapa

Pedido direto de redação ("faça a inicial", "minuta a contestação") NÃO dispensa os Passos 3 e 4-A diante de: alto valor da causa ou efeito patrimonial relevante; pedido de tutela de urgência; dano moral acima do padrão da comarca; prova exclusivamente documental controvertida; julgador conhecidamente restritivo a dano moral. Exceção única: prazo fatal hoje, com registro `[FLUXO EMERGENCIAL — revisão obrigatória antes do protocolo]`.

---

## PASSO 0 — DIAGNÓSTICO OBRIGATÓRIO

### 0.1 Polo
`CONSUMIDOR-AUTOR` ou `FORNECEDOR-RÉU`. Define a inversão de método. Em ação dúplice ou reconvenção, declarar o polo predominante e tratar o contraposto como tensionamento.

### 0.2 Sub-área (v0.1)
| Código | Sub-área | Módulo |
|---|---|---|
| `CDC` | Núcleo transversal (sempre) | `references/cdc-transversal.md` |
| `CNI` | Cobrança / negativação indevida + dano moral | `references/cobranca-negativacao-indevida.md` |

Sub-áreas previstas em ondas seguintes (ainda não implementadas — não fingir conteúdo): transporte aéreo, planos de saúde, telecom/internet, superendividamento (Lei 14.181/21), bancário-consumo. Se o caso cair nelas, operar pelo núcleo `CDC` e sinalizar a lacuna do módulo dedicado.

### 0.3 Modo
Ver tabela de 6 modos.

---

## PASSO 1 — CARREGAMENTO DO MÓDULO

**Sempre carregar (núcleo + governança):**
- `references/motor-comum.md` — núcleo metodológico (§0 anti-alucinação universal, workflow, intake, mapa bruto, avaliação de risco, revisão em camadas, gate jurisprudencial)
- `references/cdc-transversal.md` — espinha doutrinária do consumidor (responsabilidade, ônus, dano, prazos, repetição em dobro)
- `references/formato-saida.md`
- `references/intencao-estrategica-por-modo.md`
- `references/_meta.md` — estado da skill e roadmap de ondas

**Carregar por sub-área:** o módulo da tabela 0.2.

**Carregar quando há documento de origem não controlada** (peça do polo contrário, contrato de adesão de terceiro, print/áudio de SAC enviado por cliente novo): tratar como fonte sob suspeita — validar antes de incorporar.

---

## PASSO 2 — INTAKE MÍNIMO + VALIDAÇÃO DE PREMISSAS

Antes de qualquer produção, extrair:

1. **Polo** e **objetivo real** (não o que foi pedido).
2. **Relação de consumo configurada?** Consumidor destinatário final (art. 2º) × fornecedor (art. 3º). Se a relação NÃO for de consumo, a inversão de método cai — sinalizar.
3. **Fatos incontroversos** e **fatos sensíveis** (o que o polo contrário explora).
4. **Prova existente** (contrato, faturas, protocolos de SAC, extrato de negativação, e-mails) e **prova faltante**.
5. **Datas-chave** — para decadência (art. 26: 30 dias bem não durável / 90 dias durável) e prescrição (art. 27: 5 anos para fato do produto/serviço).
6. **Valor pretendido / exposição** e **resultado mínimo aceitável**.
7. **Silêncio estratégico** — o que não deve ser dito, ampliado ou provocado.

**Validação de premissas:** todo identificador citado pelo usuário (Súmula, Tema, REsp, art. de lei) cuja matéria está sendo afirmada é *pergunta*, não afirmação — cruzar em portal oficial ou marcar `[VERIFICAR]`. Divergência detectada se sinaliza, não se corrige em silêncio.

**Suficiência informacional:** classificar `SUFICIENTE / PARCIAL / INSUFICIENTE` e registrar no topo do output: `SUFICIÊNCIA: [status] — [o que falta e o risco de avançar]`.

---

## PASSO 3 — DIFERENCIAL DE TESES + MAPA ESTRATÉGICO

### 3.1 Diferencial de teses (alto impacto)
```
### Tese 1 — [nome curto]
- Probabilidade: ALTA / MÉDIA-ALTA / MÉDIA / MÉDIA-BAIXA / BAIXA
- Pivotal points (fatos que mais alteram a probabilidade)
- Âncora candidata: [súmula/tema/precedente — VERIFICAR vigência]
- Risco principal: [nomeado]
### Tese 2 / Tese 3 (pode ser tese minoritária explicitamente identificada)
## Ordem de teste: [qual fato verificar primeiro porque mais reduz incerteza]
```
Probabilidade é categoria declarativa ancorada em critério (consolidação jurisprudencial, força da prova, perfil do julgador). **Nunca número espúrio.** Em JEC rotineiro, o diferencial é uma frase.

### 3.2 Mapa estratégico
```
FAVORÁVEL (fático)          | DESFAVORÁVEL (fático)
Fatos + prova a amplificar  | Fatos + exposição + fragilidade

FAVORÁVEL (jurídico)        | DESFAVORÁVEL (jurídico)
Lei → Súmula → Doutrina     | Como neutralizar/silenciar (inclui precedente adverso)
```
Decisão por elemento: favorável = **AMPLIFICAR / INSERIR**; desfavorável = **ENFRENTAR / NEUTRALIZAR / DESLOCAR / MINIMIZAR / SILENCIAR**. Silêncio estratégico é campo obrigatório do mapa, não ausência de resposta.

**Risco por dimensão:** jurídico, financeiro (quantum/sucumbência), reputacional, processual (rito JEC × Justiça comum, competência).

---

## PASSO 3.5 — THRESHOLDS DECISÓRIOS

| Componente | Escala |
|---|---|
| Grau de confiança jurídica | ALTO / MÉDIO / BAIXO |
| Densidade probatória | ALTO / MÉDIO / BAIXO |
| Perfil do julgador (quando conhecido) | FAVORÁVEL / NEUTRO / HOSTIL |
| Custo de erro | BAIXO / MÉDIO / ALTO |

- **Frontal:** Confiança ALTA + Densidade ALTA + Julgador FAV/NEUTRO. Única configuração que dispensa subsidiária.
- **Abaixo do limiar (recusar/redesenhar):** Confiança BAIXA, ou Densidade BAIXA com custo ALTO, ou Julgador HOSTIL com Confiança não-ALTA.
- **Diagnóstica (padrão):** o resto — subsidiária + Devil's Advocate + Tensionamento Ativo obrigatórios.

Gatilhos de bloqueio absoluto: risco de alucinação documental ativo; premissa central depende de identificador não validável; decadência/prescrição consumada não tratada.

---

## PASSO 4 — VALIDAÇÃO ANTES DA REDAÇÃO

Apresentar: (1) mapa completo; (2) diferencial top 3 se aplicável; (3) tese central + subsidiárias; (4) decisão tática por ponto; (5) arquitetura da peça; (6) faixa do threshold; (7) o que não será dito e por quê. **Só redigir após aprovação explícita do mapa** (salvo fluxo emergencial declarado).

---

## PASSO 4-A — TENSIONAMENTO DO POLO CONTRÁRIO

Após o mapa, antes da minuta final.

**Versão compacta (todos os casos):**
1. **Premissa fática mais atacável** — qual afirmação, se derrubada, compromete o pedido? Está provada ou depende de inferência?
2. **Premissa jurídica mais frágil** — qual tese, se rejeitada, derruba a arquitetura? Há subsidiária que sustenta o resultado sem ela?
3. **Defesa típica do polo contrário** — qual a resposta padrão (culpa exclusiva do consumidor/terceiro; ausência de defeito; inscrição preexistente legítima; engano justificável na cobrança) e ela já foi neutralizada na peça?

**Versão integral (alto impacto):** bloco com o que o polo contrário vai atacar (descrito como ele atacaria), os argumentos que vai construir (em primeira pessoa adversária), os precedentes que vai citar contra, as fragilidades reais (sem suavização) e o reforço necessário antes da minuta. Registrar respostas antes de entregar; fragilidade crítica se corrige antes, não depois.

---

## REGRAS GLOBAIS

### Anti-alucinação (absoluta)
Detalhamento em `motor-comum.md §0`. Síntese: nenhum precedente/súmula entra na peça sem texto conferido ou marcação `[VERIFICAR]`. **Prosa segura é preferível ao número fictício — busca ativa de precedente verificável é preferível à prosa segura.** Quando a tese se beneficia de ancoragem e o precedente é localizável, buscar antes de fechar.

### Hierarquia de autoridade — consumidor
CF/88 (art. 5º XXXII; art. 170 V) → CDC (Lei 8.078/90) → leis especiais de consumo (Lei 14.181/21 superendividamento; Lei 14.454/22 rol ANS; regramentos setoriais ANAC/ANATEL/ANS/BACEN com a ressalva de não derrogarem o CDC) → STF (Temas de RG; SV) → STJ (recursos repetitivos e súmulas — verificar texto vigente: cancelamentos e revisões são frequentes) → TJ local / Turmas Recursais. *Súmula de consumidor não conferida no portal não entra com número.*

### Padrão de redação
Prosa densa, progressão lógica cumulativa, tom técnico e sóbrio. No JEC, mais direto e objetivo — volume alto premia objetividade. Negrito = ênfase do autor; itálico + aspas = citação literal; sem sublinhado; maiúsculas só em títulos. Quantum de dano moral sempre ancorado em parâmetro (precedente da própria Turma/comarca quando conhecido) e proporcionalidade — nunca valor solto.

### O que NUNCA fazer (síntese)
Redigir antes de mapear (salvo emergencial declarado); inventar dado/súmula/precedente; confundir o polo; pleitear dano moral in re ipsa fora das hipóteses consolidadas; ignorar decadência/prescrição; entregar `[VERIFICAR]` não sinalizado; tratar IA jurídica de terceiros como fonte primária; output genérico disfarçado de profundidade; quantum sem parâmetro.

---

## ROADMAP (v0.1.0 → ondas seguintes)
Implementado: núcleo motor + CDC transversal + cobrança/negativação indevida (bilateral). Previsto e ainda **não** implementado (não simular): módulos de área (aéreo, planos de saúde, telecom, superendividamento, bancário-consumo); sub-skills formais (devil's advocate, juiz externo, revisão forense como interface própria); módulo de pesquisa jurisprudencial dedicado; esqueleto de perfis de julgador; bateria de testes. Estado e ondas em `references/_meta.md`.
