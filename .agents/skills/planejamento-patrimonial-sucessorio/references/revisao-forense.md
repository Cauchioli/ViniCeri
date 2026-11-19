# Revisão Forense — Sub-skill de Revisão Multicamada

*Carregar quando modo = REVISÃO ou ao final de qualquer minuta. Opera em 6 camadas sequenciais. As 4 primeiras correspondem ao checklist transversal do motor §7; as camadas 5 e 6 são próprias da revisão de alto impacto.*

---

## PROPÓSITO

Submeter o ato/parecer pronto a seis passagens distintas, cada uma com lente própria, produzindo avaliação global IRREFUTÁVEL → FORTE → ADEQUADA → FRACA → REPROVAR + correções priorizadas. Cada camada é uma passagem completa.

---

## CAMADA 1 — FÁTICA/DOCUMENTAL
- Patrimônio, herdeiros e regime de bens confirmados em documento (não presumidos)?
- Documento disponível não utilizado (matrícula, contrato social, certidão de credores)?
- Valores dos bens com lastro (avaliação/parâmetro), não de memória?
- Datas corretas (ato, casamento/pacto, eventual passivo)?

## CAMADA 2 — JURÍDICA
- A estrutura se sustenta sozinha (objeto real, propósito negocial)?
- A norma/alíquota corresponde ao ente competente e à data do ato? Redação vigente conferida?
- A imunidade do ITBI está corretamente limitada (Tema 796 — excedente ao capital)?
- Cada Tema/EC/LC/lei estadual com número foi verificado ou marcado [VERIFICAR]? (Atenção a tese pendente — Tema 1.348.)
- Contradição interna entre os atos (contrato × doação × acordo × testamento)?

## CAMADA 3 — ESTRATÉGICA
- A estrutura entrega o objetivo dominante sem trair os demais?
- A legítima foi medida e respeitada (sem inoficiosidade)?
- A proteção está dentro dos limites (sem configurar fraude/simulação; com propósito negocial)?
- A promessa ao cliente foi calibrada (sem "blindagem absoluta" / "economia garantida")?

## CAMADA 4 — FORMAL/REGISTRAL
- Atos consistentes entre si e com o parecer?
- Descrição dos bens conforme matrícula; alcance das cláusulas (usufruto, incomunicabilidade) inequívoco?
- Remissões legais corretas (CC, Lei 6.404, lei estadual de ITCMD)?
- Atos de registro mapeados (junta comercial, RI, cartório de notas)?
- **Vestígio de texto conversacional de IA** ("Claro!", "Aqui está...") — varrer e eliminar.

## CAMADA 5 — TENSIONAMENTO ATIVO DE PREMISSAS
*(Distinta da sub-skill tensionamento-adversario, que opera em ESTRATÉGIA/MINUTA simulando as arenas. Aqui a operação é interna: testar cada premissa que o ato/parecer pronto assume como dada.)*
- Qual premissa a estrutura trata como dada e poderia ser falsa? (presume que a doação cabe na metade disponível sem ter medido; presume imunidade total de ITBI sem checar o excedente; presume ausência de credores)
- Qual premissa jurídica é tratada como pacífica e é controvertida/pendente? (ex.: imunidade de ITBI para atividade preponderante imobiliária — Tema 1.348 pendente)
- Se a premissa cair, a estrutura sobrevive (ajuste da integralização, reserva da legítima)? Se não, há risco estrutural.

## CAMADA 6 — ANCORAGEM JURISPRUDENCIAL/NORMATIVA
- Cada norma/precedente citado existe, está vigente (ou pendente) e diz o que o parecer afirma? (cruzar via pesquisa-jurisprudencial)
- A estrutura se beneficiaria de ancoragem não feita por pesquisa não realizada? (Gate de Enriquecimento)
- Há risco adverso previsível não enfrentado? (Devil's Advocate — ex.: excedente tributável de ITBI; simulação/Carf; inoficiosidade)

---

## SAÍDA ESTRUTURADA
Output no formato do MODO: REVISÃO de `formato-saida.md` — falhas por camada com gravidade, vulnerabilidades para os adversários, avaliação global, correções priorizadas.

## CRITÉRIO DE SAÍDA
As 6 camadas percorridas + avaliação global + correções ordenadas (críticas primeiro).

## ANTI-PADRÕES
- Revisar só a forma (Camada 4) e declarar pronto — omite as camadas 1-3, 5-6.
- Confirmar o que se esperava ("parece boa") sem percorrer cada camada.
- Aprovar com falha crítica porque a janela aperta — registrar a falha e a janela, não suavizar a avaliação.
