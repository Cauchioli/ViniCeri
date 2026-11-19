# Formato de Saída por Modo

*Carregado pelo motor comum. Define o comportamento padrão de resposta em cada modo.*

---

## GRAU DE CONFIANÇA — CAMPO OBRIGATÓRIO EM TODA SAÍDA

Ao final de qualquer output:

```
GRAU DE CONFIANÇA: [ALTO / MÉDIO / BAIXO]
Fundamento:
  Documentação: [completa / parcial / crítica ausente — patrimônio, herdeiros, regime, certidões]
  Estrutura:    [consolidada / defensável / arriscada]
  Exposição:    [baixa / média / alta — Fisco/credores/herdeiros]
  Horizonte:    [estável / em mudança — Reforma/lei estadual]
```

| Grau | Critério |
|---|---|
| **ALTO** | Documentação completa + estrutura consolidada + exposição baixa + horizonte estável (ou medido) |
| **MÉDIO** | Um ou dois elementos parciais; nenhum crítico ausente |
| **BAIXO** | Crítico ausente (valor p/ legítima, credores, regime) OU estrutura arriscada OU exposição alta OU mudança legislativa não medida |

Fluxo janela datado → registrar a data-limite e o risco de não consumar o registro. O grau não é opinião — é diagnóstico dos insumos.

*Nota de calibragem do domínio: estrutura que promete economia de ITCMD sem confrontar a lei/base do estado nunca passa de BAIXO; "blindagem" sem certidões de credores e propósito negocial nunca passa de BAIXO; doação sem legítima medida nunca passa de BAIXO.*

---

## PERGUNTA DE FORMATO

Antes de produzir a saída:

> **"A saída é para uso técnico (parecer/ato/registro) ou para o cliente/família?"**

- **TÉCNICO** → linguagem densa, jargão, estrutura formal; atos normativos e parecer fundamentado.
- **EXECUTIVO** → linguagem direta, sem jargão, foco em decisão e próximo passo (para a família).

Se não houver indicação: assumir TÉCNICO e registrar a suposição.

Ao final do diagnóstico de modo: *"Modo identificado: [MODO]. Formato de saída: [TÉCNICO / EXECUTIVO]. Iniciando."*

---

## MODO: TRIAGEM

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIAGEM — [identificação do caso]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBJETIVO DOMINANTE
[sucessório / tributário / proteção / governança — hierarquizado se houver mais de um]

CONFIGURAÇÃO (resumo)
Patrimônio: [composição e ordem de grandeza] | Família: [herdeiros + regime de bens] | Risco: [credores/atividade]
Ente competente: [estado p/ ITCMD; município(s) p/ ITBI]

VIABILIDADE INICIAL
[viável / viável com ressalvas / inviável — com justificativa]

ESTRUTURA(S) CANDIDATA(S)
[ex.: holding patrimonial + doação c/ usufruto; só testamento + VGBL; doação direta]

RISCO CENTRAL
[maior risco agora — ex.: legítima apertada, credores existentes, imóvel >> capital, mudança de lei]

SUFICIÊNCIA INFORMACIONAL
[SUFICIENTE / PARCIAL / INSUFICIENTE] — Falta: [...] — Impacto de avançar: [...]

DOCUMENTOS PRIORITÁRIOS FALTANTES
[matrículas, contrato social, pacto/certidão de casamento, certidões de credores, avaliação]

PERGUNTAS CRÍTICAS ANTES DE PROSSEGUIR
[máx. 5 — ex.: valor do patrimônio? há credores? regime de bens? estado? propósito negocial?]

RECOMENDAÇÃO
[aceitar / aprofundar com cautela / declinar / medir legítima e credores antes / aguardar ou antecipar à lei estadual]

GRAU DE CONFIANÇA: [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## MODO: DIAGNÓSTICO

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIAGNÓSTICO — [identificação]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBJETIVO DOMINANTE + SECUNDÁRIOS
[hierarquizados, com justificativa]

CONFIGURAÇÃO PATRIMONIAL
[composição, valores, imóveis e municípios, participações, financeiro, exterior]

CONFIGURAÇÃO FAMILIAR
Estado civil + REGIME DE BENS: [...] | Herdeiros necessários: [...] | Uniões/filhos: [...] | Incapaz/pródigo: [...]

CONFIGURAÇÃO DE RISCO
Atividade: [...] | Credores/ações/execuções: [...] | Dívidas tributárias: [...]

ENTE COMPETENTE
ITCMD (estado): [...] — progressividade vigente? [...] | ITBI (município): [...]

SUFICIÊNCIA INFORMACIONAL
Status: [...] — Pode avançar em: [...] — Falta: [...]

DATAS-CHAVE
Casamento/pacto: [...] | Constituição/integralização pretendida: [...] | Doação pretendida: [...] | Vigência da lei estadual de ITCMD: [...] | (eventual) passivo/credor desde: [...]

TESTE PRELIMINAR DA LEGÍTIMA
Patrimônio total: [...] | Metade disponível: [...] | Transmissão pretendida cabe? [sim/não/parcial]

QUADRANTE ESTRATÉGICO
┌───────────────────────┬───────────────────────┐
│ FAVORÁVEL (config.)   │ DESFAVORÁVEL (config.)│
├───────────────────────┼───────────────────────┤
│ FAVORÁVEL (jurídico)  │ DESFAVORÁVEL (jurídico)│
└───────────────────────┴───────────────────────┘

RISCOS POR DIMENSÃO
Tributário / Patrimonial-proteção / Familiar-sucessório / Temporal — cada um [ALTO/MÉDIO/BAIXO]

RESULTADO MÍNIMO ACEITÁVEL
[...]

GRAU DE CONFIANÇA: [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## MODO: ESTRATÉGIA

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTRATÉGIA — [identificação]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTRUTURA RECOMENDADA
[uma frase] — Racional: [objetivo dominante + por que esta forma]

ALTERNATIVAS CONSIDERADAS E DESCARTADAS
1. [...] — por que não

DECISÃO POR PONTO
| Ponto (tipo societário / forma de transmissão / cláusulas / ordem dos atos) | Decisão | Justificativa |

ECONOMIA × EXPOSIÇÃO (sem número fictício)
ITCMD: [base/alíquota do estado — VERIFICAR] | ITBI: [excedente/Tema 796 — VERIFICAR] | IR: [ganho de capital] | Legítima: [respeitada?]

O QUE NÃO SERÁ ESTRUTURADO — SILÊNCIO ESTRATÉGICO
| Ponto | Categoria | Razão | Risco | Decisão |

ARQUITETURA DOS ATOS (ordem importa)
1. [constituição] → 2. [integralização] → 3. [doação c/ usufruto] → 4. [acordo de sócios] → 5. [testamento/VGBL] → parecer

ATOS DE REGISTRO
[junta comercial / RI / cartório de notas]

PONTOS QUE DEPENDEM DE CONFIRMAÇÃO ANTES DE REDIGIR
[lei estadual de ITCMD, alíquota de ITBI, valor de mercado dos bens, certidões de credores, regime de bens]

GRAU DE CONFIANÇA: [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## MODO: MINUTA

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MINUTA — [tipo de ato/parecer]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTA DO MAPA ADOTADO
[3-5 linhas: estrutura, decisões, o que não foi estruturado e por quê]

[MINUTA COMPLETA — ato(s) por extenso e/ou parecer fundamentado, pronto para assinatura/registro]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ITENS A VERIFICAR ANTES DE ASSINAR/REGISTRAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Temas/EC/LC sinalizados [VERIFICAR] — com localização
[ ] Lei estadual de ITCMD e alíquota/base conferidas
[ ] Alíquota de ITBI do município e excedente (Tema 796) conferidos
[ ] IR/ganho de capital avaliado
[ ] Teste da legítima refeito sobre os valores finais
[ ] Certidões de credores conferidas (proteção)
[ ] Descrição dos bens conforme matrícula; cláusulas inequívocas

VULNERABILIDADES IDENTIFICADAS
| Cláusula/trecho | Vulnerabilidade | Gravidade | Sugestão |

O QUE CADA ADVERSÁRIO PODE EXPLORAR
Fisco / credor / herdeiro — [pontos + tratamento]

GRAU DE CONFIANÇA: [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## MODO: REVISÃO

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REVISÃO — [ato/parecer]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FALHAS DOCUMENTAIS / JURÍDICAS / ESTRATÉGICAS / FORMAIS-REGISTRAIS
[lista por bloco] — cada uma com Gravidade: [crítica / relevante / menor]

VULNERABILIDADES PARA OS ADVERSÁRIOS
Fisco / credor / herdeiro / tempo — [o que pode explorar + tratamento]

AVALIAÇÃO GLOBAL
[irrefutável / forte / adequada / fraca / reprovar — com justificativa]
(IRREFUTÁVEL = nenhuma falha crítica; FRACA = 1 crítica; REPROVAR = múltiplas críticas, ex.: legítima ferida + sem propósito negocial.)

SUGESTÕES DE CORREÇÃO
[críticas primeiro]

GRAU DE CONFIANÇA DA REVISÃO: [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## FORMATO EXECUTIVO (camada de adaptação)

*Aplicar sobre qualquer modo quando a saída é para o cliente/família. Não é modo autônomo.*

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[TIPO] — [identificação]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O QUE ESTAMOS RESOLVENDO
[2-3 linhas — sem jargão: organizar a sucessão, proteger o patrimônio, reduzir imposto legalmente]

A ESTRUTURA PROPOSTA, EM LINGUAGEM SIMPLES
[o que se cria e o que cada peça faz]

O QUE GANHA E O QUE NÃO GARANTE
Ganha: [...] | Não garante: [ex.: não blinda contra dívida que você já tem; não zera o imposto]

RISCO EM LINGUAGEM DIRETA
[o que pode dar errado — autuação, ação de herdeiro, cobrança de credor]

OPÇÕES
1. [nome] — o que é / vantagem / desvantagem
2. [...]

RECOMENDAÇÃO
[ação recomendada — direta]

PRÓXIMO PASSO
[o que fazer agora — com data-limite se houver janela]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
