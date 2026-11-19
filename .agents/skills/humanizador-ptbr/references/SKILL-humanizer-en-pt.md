---
name: humanizer
description: >
  Remove marcas de texto gerado por IA, deixando a escrita mais natural e humana.
  Use esta skill sempre que o usuário pedir para "humanizar", "tirar cara de IA",
  "deixar mais natural", "reescrever sem parecer robô", ou colar um texto que soa
  genérico ou artificial. Também acione quando o usuário mencionar problemas como
  tom sycophantic, travessões em excesso, listas que deveriam ser prosa, gerúndios
  de abertura, conectivos formais demais, ou frases de chatbot no final. Mesmo que
  o usuário não diga "humanizar", use esta skill sempre que o pedido for claramente
  sobre fazer um texto com cara de IA soar como escrito por uma pessoa real.
  Funciona com textos em português (pt-BR) e inglês.
---

# Humanizer

Reescreve texto para remover marcas de geração por IA — em português (pt-BR) ou inglês.

Baseado no guia [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), com padrões adicionais específicos para o português brasileiro.

---

## Insight central

> "LLMs usam algoritmos estatísticos para adivinhar o que vem a seguir. O resultado tende para o resultado mais estatisticamente provável que se aplica ao maior número de casos."

Essa média estatística é exatamente o que faz o texto de IA parecer artificial. O objetivo é quebrar esse padrão.

---

## Processo

1. Leia o texto e identifique quais padrões abaixo estão presentes.
2. Reescreva removendo esses padrões. Seja direto. Corte enchimento. Use palavras simples.
3. Passagem de auditoria: releia sua própria saída perguntando "isso ainda soa como IA?" Corrija o que sim.
4. Segunda reescrita se necessário: se a auditoria encontrar problemas, revise novamente.

Se o usuário fornecer uma amostra da própria escrita para calibração de voz, analise o ritmo das frases, as escolhas de palavras e os hábitos — e aplique isso na reescrita em vez de produzir uma saída humana genérica.

---

## Padrões a remover

### Padrões de conteúdo
1. **Inflação de importância** — "momento crucial", "potencial transformador", "revolucionário" → diga o fato diretamente
2. **Name-dropping de notoriedade** — listar veículos (Folha, Globo, BBC) sem citação real → cite especificamente ou corte
3. **Análises superficiais com gerúndio** — "simbolizando...", "refletindo...", "demonstrando..." → remova ou substitua por fontes reais
4. **Linguagem promocional** — "situada no coração do vibrante..." → "fica na região de..."
5. **Atribuições vagas** — "especialistas acreditam", "estudos mostram" → cite uma fonte específica ou corte
6. **Desafios formulaicos** — "Apesar dos desafios, continua crescendo" → use fatos concretos sobre os desafios reais

### Padrões de linguagem
7. **Vocabulário de IA em pt-BR** — "crucial", "fundamental", "ressaltar", "cenário", "ecossistema", "sinergia", "robusto", "holístico", "impactar", "alavancar", "paradigma", "catalisar" → corte ou use palavras mais simples
8. **Evitação de cópula** — "serve como", "apresenta", "conta com", "destaca-se por" → "é", "tem"
9. **Paralelismos negativos** — "Não se trata apenas de X, mas de Y", "Mais do que X, é Y" → diga o ponto diretamente
10. **Regra dos três** — "inovação, inspiração e resultados" → use o número natural de itens que o conteúdo exige
11. **Ciclagem de sinônimos** — usar palavras diferentes para o mesmo conceito para evitar repetição → repita a palavra mais clara
12. **Falsos intervalos** — "do Big Bang à matéria escura" → liste os tópicos diretamente
13. **Voz passiva / fragmentos sem sujeito** — "Nenhuma configuração necessária" → nomeie o agente quando ajuda na clareza

### Padrões de estilo
14. **Abuso de travessão** — múltiplos travessões por parágrafo → prefira vírgulas ou pontos
15. **Abuso de negrito** — negritar todo termo ou substantivo → remova negrito a menos que seja genuinamente crítico
16. **Listas com cabeçalho inline** — **Desempenho:** O desempenho melhorou → converta em prosa
17. **Title Case indevido** — "Negociações Estratégicas E Parcerias" → "Negociações estratégicas e parcerias" (em pt-BR só a primeira palavra é maiúscula)
18. **Emojis** — 🚀💡✅ → remova completamente
19. **Aspas curvas** — `"aspas inteligentes"` → `"aspas retas"` (padrão digital pt-BR)
20. **Jargão corporativo hifenizado** — não é problema de hífen como em inglês, mas de expressões: "orientado a dados", "centrado no cliente", "focado em resultados" → simplifique ou corte
21. **Tropos de autoridade persuasiva** — "No fundo, o que importa é...", "Em essência...", "O ponto central é..." → diga o ponto diretamente
22. **Anúncios de sinalização** — "Vamos explorar", "Confira a seguir", "Neste artigo, abordaremos" → comece com o conteúdo
23. **Cabeçalhos fragmentados** — `## Desempenho` seguido de "Velocidade importa." → deixe o cabeçalho fazer o trabalho ou mescle

### Padrões de comunicação
24. **Artefatos de chatbot** — "Espero ter ajudado!", "Fico à disposição!", "Qualquer dúvida, estou aqui!" → remova completamente
25. **Isenções de corte de conhecimento** — "Com base nas informações disponíveis..." → encontre fontes ou corte
26. **Tom sycophantic** — "Ótima pergunta!", "Que reflexão interessante!", "Você tocou num ponto muito importante!" → responda diretamente

### Enchimento e hedging
27. **Frases de enchimento pt-BR** — "no sentido de", "tendo em vista que", "em virtude de", "no que tange a", "no âmbito de", "no que diz respeito a" → "para", "porque", "sobre"
28. **Hedging excessivo** — "poderia potencialmente talvez" → "pode"
29. **Conclusões genéricas** — "O futuro é promissor", "Tempos empolgantes nos aguardam" → fatos concretos ou corte

---

## Padrões exclusivos do português brasileiro

Esses padrões não existem na referência original em inglês mas são muito característicos de IAs escrevendo em pt-BR:

### 30. Gerúndio de abertura
IA abre frases e parágrafos com gerúndio com frequência anormal:
- "Considerando que...", "Levando em conta...", "Sendo assim...", "Partindo do pressuposto que..."
→ Comece com sujeito direto.

### 31. Conectivos formais em excesso
Palavras que ninguém usa na escrita natural moderna:
- "Outrossim", "Ademais", "Destarte", "Porquanto", "Mister se faz", "Consoante"
→ Substitua por "Também", "Além disso", "Por isso", "Segundo".

### 32. "Vale ressaltar / cabe destacar"
Muleta muito frequente de IA no início de parágrafos:
- "Vale ressaltar que...", "Cabe destacar que...", "É importante salientar que...", "Importa mencionar que..."
→ Corte e vá direto ao ponto.

### 33. Registro formal inadequado
IA tende ao registro culto formal mesmo em contextos casuais — e-mail para amigo, post de blog, mensagem de WhatsApp.
→ Ajuste o registro para o que o contexto pede. Informal pode usar contrações, gírias, frases curtas.

### 34. Português de Portugal
IA às vezes usa construções do português europeu:
- "está a fazer" em vez de "está fazendo"
- "utilizar" quando o contexto pede "usar"
- "habitualmente" em vez de "normalmente"
- "talvez" + subjuntivo onde pt-BR usaria indicativo
→ Verifique e ajuste para pt-BR.

---

## Calibração de voz (opcional)

Se o usuário fornecer uma amostra da própria escrita, antes de reescrever:
- Observe o ritmo das frases (curtas e diretas? longas e elaboradas?)
- Observe o nível de vocabulário e palavras recorrentes
- Observe hábitos de pontuação
- Observe o tom (seco? caloroso? direto?)

Aplique essas características na saída humanizada.

---

## Exemplo em português

**Antes (com cara de IA):**
> Ótima pergunta! A IA generativa serve como um testemunho duradouro do potencial transformador dos modelos de linguagem, marcando um momento crucial na evolução do desenvolvimento de software. Ademais, vale ressaltar que, considerando o cenário atual, as ferramentas de codificação assistida por IA — situadas na interseção entre pesquisa e prática — estão remodelando como engenheiros idealizam, iteram e entregam. 💡 **Velocidade:** A geração de código é significativamente mais rápida. 🚀 **Qualidade:** A qualidade do output foi aprimorada. Não se trata apenas de autocomplete; trata-se de desbloquear a criatividade em escala. Espero ter ajudado! Qualquer dúvida, fico à disposição.

**Depois (humanizado):**
> Assistentes de código de IA são úteis para as partes chatas do trabalho. São bons em boilerplate: arquivos de config e aquele código de cola que você não quer escrever. O problema é o quanto as sugestões parecem certas. Já aceitei código que compilou, passou no lint e só percebi depois que estava errado porque parei de prestar atenção. Se você tratar como autocomplete e revisar cada linha, funciona. Se usar para não pensar, vai só entregar bugs mais rápido.

---

## Exemplo em inglês

**Antes:**
> Great question! AI-assisted coding serves as an enduring testament to the transformative potential of large language models. At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. 💡 **Speed:** Code generation is significantly faster. The future looks bright!

**Depois:**
> AI coding assistants speed up the boring parts. They're great at boilerplate — config files and the glue code you don't want to write. The dangerous part is how confident the suggestions look. Treat it like autocomplete and review every line: useful. Use it to avoid thinking: you'll just ship bugs faster.

---

## Referências
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)
