---
name: humanizador-ptbr
description: >
  Detecta e remove marcas de escrita gerada por IA em textos em português brasileiro.
  Use sempre que o usuário pedir para "humanizar", "tirar cara de IA", "deixar mais natural",
  "reescrever sem parecer robô", ou quando o texto soar genérico, repetitivo ou artificial.
  Funciona com qualquer formato: artigo, post de LinkedIn, e-mail, WhatsApp, TCC, relatório, roteiro.
  Versão unificada de SKILL.md + the-humanizer.md, 100% em pt-BR com vícios específicos do português.
---

# Humanizador pt-BR v1.0

Revisor de conteúdo calibrado para detectar textura de IA e reescrever em voz humana autêntica.

---

## Insight central

> "LLMs adivinham estatisticamente o que vem a seguir. O resultado é a média do que se aplica ao maior número de casos."

Essa média é exatamente o que faz o texto de IA parecer artificial. O objetivo é quebrar o padrão.

---

## Pipeline de revisão

1. **Detectar o formato** — artigo, LinkedIn, e-mail, WhatsApp/Slack, trabalho acadêmico
2. **Escanear padrões de IA** — frases, vocabulário, estrutura
3. **Checar originalidade** — o texto poderia ter sido escrito por qualquer pessoa com acesso ao Google?
4. **Pontuar** — AI-Likeness, Autenticidade, Valor para o leitor, Credibilidade de domínio
5. **Reescrever** — sem adicionar ideias novas, sem remover substância
6. **Auditoria** — releia e pergunte: "ainda soa como IA?" Corrija o que sim.

---

## BLOCO 1 — Vocabulário de IA em pt-BR

Palavras que aparecem com frequência anormal em textos gerados por IA. Substitua por palavras mais diretas ou corte.

### Intensificadores ocos
- crucial → importante / decisivo (ou corte)
- fundamental → necessário / básico (ou corte)
- essencial → importante (ou corte)
- significativo → grande / real / concreto
- substancial → grande / relevante
- robusto → sólido / forte / confiável
- abrangente → completo / amplo
- relevante (como enchimento) → corte

### Verbos de IA
- alavancar → usar / aproveitar
- impactar → afetar / mudar / prejudicar / melhorar
- catalisar → acelerar / provocar
- otimizar → melhorar / ajustar
- maximizar → aumentar / elevar ao máximo
- potencializar → aumentar / reforçar
- fomentar → incentivar / estimular
- viabilizar → tornar possível / permitir
- implementar → colocar em prática / aplicar (em contextos informais)
- desenvolver habilidades → aprender / praticar

### Substantivos de IA
- cenário → contexto / situação
- ecossistema → ambiente / mercado / setor
- sinergia → parceria / integração / trabalho conjunto
- paradigma → modelo / padrão / jeito de fazer
- framework → estrutura / modelo / método
- stakeholder → parte interessada / envolvido
- jornada → caminho / processo / trajetória (em contextos banais)
- narrativa → história / argumento (quando usado como eufemismo)
- engajamento → participação / atenção / resposta
- protagonismo → papel ativo / liderança

### Adjetivos de IA
- holístico → amplo / integrado / completo
- multifacetado → complexo / variado / com vários aspectos
- dinâmico (como enchimento) → corte
- inovador (como enchimento) → corte — diga o que é inovador especificamente
- disruptivo → novo / diferente / que muda o mercado
- transformador → que muda / que altera profundamente
- revolucionário → novo (se for apenas novo)
- estratégico (como enchimento) → corte — seja específico sobre qual estratégia

---

## BLOCO 2 — Frases e expressões de IA em pt-BR

### Marcadores de parágrafo — remova e vá direto ao ponto
- "Vale ressaltar que..."
- "Cabe destacar que..."
- "É importante salientar que..."
- "É relevante mencionar que..."
- "Importa mencionar que..."
- "Cabe ressaltar que..."
- "É possível afirmar que..."
- "É necessário destacar que..."
- "É fundamental ressaltar que..."
- "É importante enfatizar que..."
- "Não podemos deixar de mencionar que..."
- "Nesse contexto, é válido ressaltar que..."

### Tropos de autoridade persuasiva — diga o ponto diretamente
- "No fundo, o que importa é..."
- "Em essência..."
- "O ponto central é..."
- "Em última análise..."
- "Em última instância..."
- "No cerne da questão..."
- "A verdade é que..." (quando antecede afirmação óbvia)
- "O que realmente importa é..."

### Anúncios de sinalização — comece com o conteúdo
- "Vamos explorar..."
- "Confira a seguir..."
- "Neste artigo, abordaremos..."
- "A seguir, veremos..."
- "Ao longo deste texto..."
- "Nas próximas linhas..."
- "Como veremos a seguir..."

### Artefatos de chatbot — remova completamente
- "Espero ter ajudado!"
- "Fico à disposição!"
- "Qualquer dúvida, estou aqui!"
- "Conte comigo!"
- "Foi um prazer!"
- "Espero que isso esclareça!"

### Tom sycophantic — responda diretamente
- "Ótima pergunta!"
- "Que reflexão interessante!"
- "Você tocou num ponto muito importante!"
- "Excelente observação!"
- "Que perspectiva rica!"

### Frases de enchimento pt-BR — substitua pela versão curta
- "no sentido de" → para
- "tendo em vista que" → porque / já que
- "em virtude de" → por / por causa de
- "no que tange a" / "no que tange ao" → sobre
- "no âmbito de" / "no âmbito do" → em / dentro de
- "no que diz respeito a" → sobre / quanto a
- "no que se refere a" → sobre
- "diante desse cenário" → por isso / nesse contexto
- "nesse sentido" → por isso (ou corte)
- "sob essa perspectiva" → assim / por essa lógica (ou corte)
- "para tanto" → para isso
- "nesse interim" → enquanto isso / nesse período
- "a priori" → inicialmente / a princípio
- "a posteriori" → depois / em seguida

### Hedging excessivo — seja direto
- "poderia potencialmente" → pode
- "talvez seja possível" → pode ser
- "não seria de todo errado afirmar que" → corte — afirme diretamente
- "de certa forma" → corte na maioria dos casos
- "em certa medida" → corte na maioria dos casos
- "de algum modo" → corte na maioria dos casos

### Conclusões genéricas — fatos concretos ou corte
- "O futuro é promissor"
- "Tempos empolgantes nos aguardam"
- "O caminho está apenas começando"
- "Muito ainda está por vir"
- "O potencial é imenso"
- "As possibilidades são infinitas"

---

## BLOCO 3 — Conectivos formais excessivos (vício grave de IA em pt-BR)

Palavras que ninguém usa na escrita natural moderna. Troque pelas versões simples:

| Palavra de IA | Substituto |
|---|---|
| Outrossim | Também |
| Ademais | Além disso |
| Destarte | Por isso |
| Porquanto | Porque |
| Mister se faz | É preciso |
| Consoante | Segundo / De acordo com |
| Por conseguinte | Por isso / Então |
| Doravante | A partir de agora / Daqui em diante |
| Hodiernamente | Hoje / Atualmente |
| Precipuamente | Principalmente |
| Mormente | Principalmente / Sobretudo |
| Dessarte | Por isso |
| Conquanto | Embora / Mesmo que |
| Outrossim | Também |
| Haja vista | Já que / Porque |
| Em que pese | Embora / Apesar de |
| Não obstante | Apesar disso |

---

## BLOCO 4 — Padrões estruturais de IA

### Gerúndio de abertura (vício exclusivo do pt-BR)
IA abre frases e parágrafos com gerúndio com frequência anormal:
- "Considerando que..." → Como / Dado que
- "Levando em conta..." → Como / Já que
- "Sendo assim..." → Por isso / Então
- "Partindo do pressuposto que..." → Assumindo que
- "Visando a..." → Para / Com o objetivo de
- "Buscando..." (no início de frase) → A ideia é / O objetivo é
- "Analisando o contexto..." → corte — vá direto à análise

### Listas onde deveria haver prosa
IA converte raciocínio em bullets quando o pensamento é contínuo.
Sinal: lista com 2-3 itens que se conectam logicamente. Reescreva como parágrafo.

### Parágrafos de tamanho uniforme
Todo parágrafo com 3-4 frases é assinatura de IA. Varie: um parágrafo de 1 frase, outro de 6.

### Estrutura intro > 3 pontos > conclusão
O template mais previsível de IA. Reescreva com estrutura orgânica.

### Fechamento com resumo do que acabou de ser dito
IA fecha repetindo o que disse. Feche com desafio, pergunta aberta ou princípio novo.

### Três perguntas retóricas de abertura
"Você já se perguntou X? E se Y? Imagine Z." Reescreva como afirmação direta ou história específica.

### Negação antes do ponto real
- "Não se trata apenas de X, mas de Y" → diga Y diretamente
- "Mais do que X, é Y" → diga Y
- "Isso não é X. É Y." → É Y. Ponto.

### Paralelismo de três (Regra dos três artificial)
"inovação, inspiração e resultados" — se o conteúdo não exige três, não use três.

### Fragmentos empilhados como conclusão
"Mais clareza. Mais foco. Mais resultado." — reescreva como frase real.

### Abertura com afirmação genérica
"A tecnologia mudou o mundo." — comece com algo específico: dado, história, fato concreto.

### Cabeçalho + frase óbvia
`## Desempenho` seguido de "O desempenho é importante." — o cabeçalho já diz isso. Corte ou desenvolva.

---

## BLOCO 5 — Padrões exclusivos do português brasileiro

Esses padrões não existem (ou são raros) em IA escrevendo em inglês, mas são marcas claras em pt-BR:

### Registro formal inadequado ao contexto
IA usa linguagem de petição jurídica num e-mail informal, ou tom acadêmico num post de Instagram.
→ Ajuste o registro para o que o contexto pede.

### Voz passiva sem agente
"Foi decidido que...", "Serão tomadas medidas..." — quem decidiu? Quem toma as medidas?
→ Nomeie o agente quando isso ajuda a entender.

### Português de Portugal
IA mistura construções europeias:
- "está a fazer" → está fazendo
- "utilizar" → usar (em contextos informais)
- "habitualmente" → normalmente / geralmente
- "talvez" + subjuntivo onde pt-BR usaria indicativo

### Nominalização excessiva
Transformar verbos em substantivos para soar mais formal:
- "fazer a realização de" → realizar
- "proceder à análise de" → analisar
- "efetuar o pagamento" → pagar
- "dar continuidade" → continuar
- "promover o desenvolvimento" → desenvolver

### Ciclagem de sinônimos forçada
IA usa palavras diferentes para o mesmo conceito tentando "evitar repetição":
- usa "ferramenta", depois "instrumento", depois "recurso" para o mesmo objeto
→ Repita a palavra mais clara. Repetição intencional não é erro.

### Gerundismo do futuro (erro gramatical de IA)
"Estarei enviando o relatório" em vez de "Vou enviar o relatório"
→ Corrija para forma simples.

### Eufemismo corporativo brasileiro
Expressões que soam profissionais mas não dizem nada:
- "construir pontes" (metáfora vazia)
- "pensar fora da caixa"
- "virar a chave"
- "alinhar expectativas"
- "colocar na mesa"
- "trazer para o centro da conversa"
- "mapear o terreno"
→ Diga o que você quer dizer literalmente.

### Fórmula de encerramento acadêmico genérico
"Portanto, conclui-se que a temática abordada é de extrema relevância para o avanço da sociedade."
→ Feche com o argumento real ou com uma implicação concreta.

### Impessoalidade artificial
"O presente trabalho buscou demonstrar que..." em contexto onde "Neste trabalho mostramos que..." é mais claro.
→ Use primeira pessoa quando o contexto permite e fica mais direto.

### Abertura com definição de dicionário
"Segundo o dicionário Michaelis, X é definido como..." — abertura clássica de IA tentando parecer erudita.
→ Comece com o problema real, o caso concreto, a pergunta que motivou o texto.

---

## BLOCO 6 — Padrões de LinkedIn em pt-BR

### Frases-gatilho de LinkedIn (versão pt-BR)
- "Mas aqui está o que ninguém te conta sobre..."
- "E sabe o que aprendi com isso?"
- "Deixa eu te contar uma história."
- "Isso mudou tudo pra mim."
- "Se tem uma coisa que aprendi em X anos de..."
- "A maioria das pessoas faz isso errado."
- "Não é sobre X. É sobre Y."

### Vulnerabilidade performática
"Vou ser honesto aqui." / "Posso ser transparente?" / "Não ia compartilhar isso, mas..."
→ Vulnerabilidade real não anuncia a si mesma.

### Humildade falsa
"Não sou especialista, mas..." / "Pode ser polêmico, mas..." → sempre precede afirmação confiante. Corte o aviso.

### Engajamento mendigo
"Concorda? Comenta aqui." / "Marca alguém que precisa ler isso." / "Compartilha se fez sentido."
→ Se o conteúdo for bom, as pessoas vão engajar. Não peça.

### Um-frase-por-parágrafo
Cada frase em linha separada.
Como essa.
É a assinatura número 1 de ghostwriter/IA no LinkedIn.
→ Agrupe frases relacionadas em parágrafos reais.

### Hook de informação retida
"Fiz uma descoberta que mudou minha empresa. Era sobre uma palavra."
→ Diga qual palavra. Diga a descoberta. Não force o clique.

### Fórmula do post de conquista
(1) palavra de emoção + anúncio + emoji, (2) agradecimento à equipe, (3) lição universal genérica, (4) encerramento entusiasmado.
→ Conte o que foi difícil, específico, ou surpreendente. Corte o template.

---

## BLOCO 7 — Padrões de e-mail em pt-BR

### Saudações de IA
- "Espero que este e-mail te encontre bem."
- "Espero que esteja tendo uma ótima semana."
- "Confio que esteja bem."
→ Vá direto ao ponto.

### Encerramentos de IA
- "Qualquer dúvida, estou à disposição."
- "Fico no aguardo do seu retorno."
- "Agradeço desde já a atenção."
- "Coloco-me à disposição para esclarecimentos."
→ Um "obrigado" basta. Ou corte.

### Pedido enterrado no fim
O real pedido aparece no último parágrafo. Coloque na abertura.

### Formalidade incompatível com o relacionamento
"Prezado senhor" para alguém que você troca mensagens todo dia.
→ Ajuste o tom para o relacionamento real.

---

## BLOCO 8 — Checklist de originalidade

O texto passa nesse teste ou poderia ter sido escrito por qualquer pessoa com acesso ao Google?

- [ ] Tem dado, número ou fato específico que ancora o argumento?
- [ ] Tem experiência de primeira mão — uma situação real, um erro cometido, uma observação concreta?
- [ ] O exemplo é específico (nome, data, valor, resultado) ou genérico ("uma empresa do setor")?
- [ ] O argumento principal poderia aparecer num post de qualquer consultant de LinkedIn?
- [ ] Tem algo que só quem viveu aquilo poderia escrever?

Se a maioria das respostas for negativa, o texto está vazio de substância independente do vocabulário.

---

## BLOCO 9 — Regras de reescrita

1. Nunca adicione ideias que não estavam no original.
2. Nunca remova substância — apenas mude a entrega.
3. Substitua toda frase de IA por linguagem específica do autor.
4. Varie o ritmo: misture frases curtas com frases longas.
5. Substitua aberturas genéricas por algo específico (dado, história, afirmação contrária).
6. Substitua fechamentos-resumo por desafio, princípio ou pergunta aberta.
7. Quebre a uniformidade dos parágrafos — alguns curtos, alguns longos.
8. Se falta exemplo concreto, sinalize com `[ADICIONE UM EXEMPLO REAL AQUI]`.
9. Após reescrever, releia e pergunte: "ainda soa como IA?" Corrija o que sim.

---

## BLOCO 10 — Calibração de voz

Se o usuário fornecer amostra da própria escrita:
- Observe o ritmo das frases (curtas e diretas? longas e analíticas?)
- Observe o nível de vocabulário e palavras recorrentes
- Observe hábitos de pontuação
- Observe o tom (seco? caloroso? irônico? direto?)
- Observe como abre e como fecha
- Observe o que nunca usaria

Aplique essas características na reescrita em vez de produzir "humanidade genérica".

---

## Referências
- SKILL.md (humanizer original — Downloads)
- the-humanizer.md v2.4 (Crazy Marketer — Downloads)
- Wikipedia: Signs of AI writing
- WikiProject AI Cleanup
