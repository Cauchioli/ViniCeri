# Revisão Forense — Sub-skill de Revisão Multicamada

*Carregar quando modo = REVISÃO ou ao final de qualquer minuta. Opera em 6 camadas sequenciais. As 4 primeiras correspondem ao checklist transversal do motor §7; as camadas 5 e 6 são próprias da revisão de alto impacto.*

---

## PROPÓSITO

Submeter a peça pronta a seis passagens distintas, cada uma com lente própria, produzindo uma avaliação global na escala IRREFUTÁVEL → FORTE → ADEQUADA → FRACA → REPROVAR + lista de correções priorizadas. Cada camada é uma passagem completa pelo texto — não um olhar simultâneo.

---

## CAMADA 1 — FÁTICA
- Afirmação sem prova nos autos? (quitação sem comprovante, pactuação negada sem o contrato, ausência de notificação não demonstrada)
- Prova disponível não utilizada? (cláusula do contrato, extrato, print do golpe)
- Cronologia correta e completa? (contratação → vigência → vencimento/mora → negativação/apreensão/operação fraudulenta)
- Fato amplificado além do que a prova sustenta?

## CAMADA 2 — JURÍDICA
- A tese central se sustenta sozinha?
- A norma/taxa corresponde à data da contratação? Redação vigente conferida?
- A abusividade está ancorada em cotejo com a taxa média BCB (não em 12% a.a.)?
- Cada Tema/Súmula/REsp com número foi verificado ou marcado [VERIFICAR]?
- Contradição interna entre seções? Fundamentos servem ao pedido sem excesso nem lacuna?

## CAMADA 3 — ESTRATÉGICA
- A peça convence este juízo/Turma específico (perfil-julgador)?
- Algum pedido superdimensionado frente ao risco real (ex.: dano moral inflado; revisional sem tese sólida)?
- O silêncio estratégico foi mantido (ex.: não abrir discussão de mora quando o pedido é só expurgo de tarifa)?
- A peça abre flanco que a instituição pode explorar e que poderia ter sido fechado?

## CAMADA 4 — PROTOCOLAR
- Pedidos consistentes com o corpo (revisão + repetição de indébito + exclusão de negativação + dano moral + tutela + honorários)?
- Dados do contrato corretos (nº, data, valor, partes)?
- Frase truncada, pontuação dupla, salto de numeração de seção?
- **Vestígio de texto conversacional de IA** ("Claro!", "Aqui está...", "Você está certo...") — varrer e eliminar.
- Citações literais (cláusula, ementa) entre aspas e atribuídas a documento verificado?

## CAMADA 5 — TENSIONAMENTO ATIVO DE PREMISSAS
*(Distinta da sub-skill tensionamento-adversario, que opera em ESTRATÉGIA/MINUTA simulando a instituição. Aqui a operação é interna: testar cada premissa que a peça pronta assume como dada.)*
- Qual premissa fática a peça trata como dada e poderia ser falsa? (ex.: presume não pactuada a capitalização sem ter lido a cláusula que a pactua; presume inexistente a mora)
- Qual premissa jurídica a peça trata como pacífica e é, na verdade, controvertida ou minoritária? (ex.: abusividade por superar a média)
- Se a premissa cair, a arquitetura sobrevive pela subsidiária (expurgo parcial, depósito do incontroverso)? Se não, a peça está em risco estrutural.

## CAMADA 6 — ANCORAGEM JURISPRUDENCIAL
- Cada precedente citado existe, está vigente e diz o que a peça afirma que diz? (cruzar via pesquisa-jurisprudencial)
- A tese se beneficiaria de ancoragem que não foi feita por pesquisa não realizada? (Gate de Enriquecimento)
- Há precedente contrário previsível não enfrentado? (Devil's Advocate Jurisprudencial — ex.: repetitivo que valida a capitalização pactuada)

---

## SAÍDA ESTRUTURADA
Output no formato do MODO: REVISÃO de `formato-saida.md` — falhas por camada com gravidade, vulnerabilidades para o adversário, avaliação global, correções priorizadas.

## CRITÉRIO DE SAÍDA
As 6 camadas percorridas + avaliação global atribuída + correções ordenadas (críticas primeiro).

## ANTI-PADRÕES
- Revisar só a forma (Camada 4) e declarar a peça pronta — falha por omissão das camadas 1-3, 5-6.
- Confirmar o que se esperava encontrar (a peça "parece boa") sem percorrer cada camada.
- Aprovar peça com falha crítica porque o prazo aperta — nesse caso, registrar FLUXO EMERGENCIAL e a falha, não suavizar a avaliação.
