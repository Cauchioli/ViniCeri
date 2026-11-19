# Lições Aprendidas — Skill Advocacia Tributária

Este arquivo armazena lições abstratas coletadas em casos reais, servindo para prevenir a repetição de erros e solidificar as teses do escritório.

---

## Catálogo de Lições

### L-001: A ilusão da porcentagem de desconto na Transação
- **Contexto**: Cliente chega com passivo tributário querendo "desconto de 65% ou 70%" anunciado nos editais da PGFN.
- **Falha**: Tratar o percentual anunciado como linear sobre toda a dívida.
- **Correção**: O principal da dívida (geralmente ~67% do total) é intocável pela Constituição Federal. O desconto do edital incide exclusivamente sobre a base descontável (juros, multas e encargos — que representam ~33% do total).
- **Regra**: O cálculo do desconto real efetivo deve ser feito sobre a base descontável. Exemplo: $65\% \times 33\% = 21,45\%$ de redução real efetiva sobre o valor bruto consolidado. Nunca prometa descontos diretos sem apurar a composição da CDA.

### L-002: O impacto do histórico de rescisões na Transação
- **Contexto**: Empresa devedora com histórico de vários parcelamentos rescindidos.
- **Falha**: Simular proposta de transação sem aplicar o rebaixamento de desconto.
- **Correção**: A Portaria PGFN e as normas da Lei 14.690/2023 penalizam a reincidência de descumprimento de acordos. O desconto apurado na lição L-001 sofre um redutor de acordo com a faixa (ex: 6 a 9 rescisões reduzem o desconto em 45%).
- **Regra**: Multiplicar o desconto da L-001 pelo fator de histórico. Exemplo: Dívida de R$ 31M da Empresa ABC com 9 rescisões de acordos. Desconto real efetivo = $21,45\% \times 45\% = 9,65\%$ de desconto real sobre a dívida bruta.

### L-003: O risco da classificação como "Devedor Contumaz"
- **Contexto**: Cliente com inadimplência crônica e seguidas rescisões de transações vigentes.
- **Falha**: Ignorar o enquadramento na Lei 14.690/2023.
- **Correção**: Uma nova rescisão ou o descumprimento sistemático pode acionar a classificação formal de "Devedor Contumaz" pela PGFN. Esse status reduz o fator de desconto histórico de 45% para 20%, além de impedir novas adesões a editais facilitados.
- **Regra**: Sinalizar com urgência e classificar na "Below test threshold" qualquer cliente que esteja na iminência de se tornar devedor contumaz, recomendando saídas drásticas como Recuperação Judicial em vez de transações ordinárias.

### L-004: Sucessão e Blindagem em M&A de Empresa Endividada
- **Contexto**: Comprador interessado nos ativos operacionais de empresa com passivo fiscal multimilionário.
- **Falha**: Propor aquisição direta de quotas (Share Deal) ou simples compra de ativos (Asset Deal) presumindo proteção contratual.
- **Correção**: Pelo art. 133 do CTN, a compra de fundo de comércio gera responsabilidade subsidiária automática do adquirente pelas dívidas fiscais dos 2 anos anteriores. A única forma de quebrar essa cadeia de sucessão de forma absoluta é a alienação judicial de Unidade Produtiva Isolada (UPI) em Recuperação Judicial (Lei 11.101/05 art. 60 e Tema 122 do STF).
- **Regra**: Se há passivo insolúvel e comprador com aporte, o Cenário 5 (RJ + leilão de UPI) é a única blindagem 100% segura para o investidor, reduzindo o risco sucessório a zero.
