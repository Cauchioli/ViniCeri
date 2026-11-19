---
name: humanizador-ptbr
description: >
  Detecta e remove marcas de escrita gerada por IA em textos em português brasileiro.
  Inclui evasão algorítmica contra detectores (Turnitin, GPTZero, CopySpider).
---

# Humanizador pt-BR v3.0 (Anti-Detector)

Revisor de conteúdo calibrado para detectar textura de IA, reescrever em voz humana autêntica e evadir detectores algorítmicos.

---

## Insight central

> "LLMs adivinham estatisticamente o que vem a seguir. O resultado é a média do que se aplica ao maior número de casos."

Essa média é o que os detectores (como Turnitin, GPTZero, etc) medem. Eles avaliam a **Perplexidade** (o quão previsível é a próxima palavra) e a **Explosividade/Burstiness** (a variação no tamanho e estrutura das frases).

---

## BLOCO 1 — Evasão Algorítmica (Anti-Detectores)

Detectores matemáticos de IA não leem o texto, eles medem entropia. Para quebrar a detecção de 60%+ de IA, aplique estas três regras estruturais:

### 1. Injeção de Explosividade (Burstiness)
IA escreve frases com comprimentos muito parecidos (ex: 15-20 palavras por frase).
**Regra:** Force uma variação brutal. Escreva uma frase de 3 palavras. Depois uma de 30 palavras com orações subordinadas. Depois uma de 8 palavras.
*Exemplo prático:* "A inteligência artificial mudou o Direito. [Frase curta]. Essa transformação, embora pareça repentina para muitos escritórios tradicionais, vem sendo desenhada há pelo menos uma década através da automação de pequenos processos repetitivos. [Frase longa]."

### 2. Aumento de Perplexidade (Quebra de N-grams previsíveis)
Detectores buscam combinações de palavras muito comuns (ex: "é importante ressaltar que", "no cenário atual").
**Regra:** Substitua a palavra mais óbvia da frase por um sinônimo menos estatisticamente provável, mas que soe natural para um humano.
*Exemplo:* Em vez de "A IA traz grandes benefícios", use "A IA carrega vantagens expressivas". Em vez de "resolver o problema", use "desatar o nó" ou "solucionar a falha".

### 3. Imperfeição Orgânica (Sintaxe Conversacional)
IA nunca usa parênteses para pensamentos paralelos não planejados, nem frases que começam com conjunções de forma abrupta.
**Regra:** Adicione "pensamentos paralelos" entre travessões ou parênteses. Comece algumas frases com "E", "Mas" ou "Ou".

---

## BLOCO 2 — Vocabulário de IA em pt-BR

Palavras de baixa perplexidade (muito esperadas pelo detector). Substitua:

### Intensificadores e Adjetivos
- crucial → vital / decisivo
- fundamental → básico / incontornável
- significativo → palpável / real
- robusto → sólido / resistente
- abrangente → completo / vasto
- holístico → integrado
- disruptivo → que altera o eixo / inovador

### Verbos de IA
- alavancar → impulsionar / aproveitar
- impactar → atingir / afetar
- catalisar → acelerar
- otimizar → afinar / melhorar
- maximizar → extrair o máximo
- fomentar → nutrir / estimular

### Substantivos de IA
- cenário → contexto / panorama
- ecossistema → ambiente / rede
- sinergia → alinhamento / colaboração
- paradigma → modelo / padrão

---

## BLOCO 3 — Frases e expressões de IA em pt-BR

Remova completamente para aumentar a perplexidade:
- "Vale ressaltar que..."
- "Cabe destacar que..."
- "É importante salientar que..."
- "No fundo, o que importa é..."
- "Em essência..."
- "Nesse sentido..."
- "Diante desse cenário..."

---

## BLOCO 4 — Conectivos formais (Red flags para detectores)

Detectores associam esses conectivos a textos gerados, pois humanos raramente os usam hoje:
- Outrossim → Também / Além do mais
- Ademais → Além disso
- Destarte → Sendo assim / Por isso
- Porquanto → Porque
- Mister se faz → É preciso / Faz-se necessário
- Consoante → De acordo com / Segundo

---

## BLOCO 5 — Padrões estruturais de IA

### Gerúndio de abertura
IA abre frases e parágrafos com gerúndio:
- "Considerando que..." → Dado que
- "Levando em conta..." → Como
- "Analisando o contexto..." → (Vá direto ao ponto)

### Abertura com definição
"Segundo o dicionário, X é..." — O detector identifica isso como um padrão de modelo de linguagem de baixo nível. Corte a definição e comece com o problema prático.

---

## BLOCO 6 — O Fator "Plágio Involuntário" da IA
Modelos de linguagem decoram textos da internet. Se a IA escreve algo genérico, o detector de plágio vai apontar cópia de algum site aleatório.
**Regra:** Se o texto estiver apenas descrevendo um conceito geral (ex: "A LGPD protege dados"), reescreva usando uma analogia própria ou ancorando o conceito na realidade do autor, para que a sequência de palavras seja matematicamente inédita.

---

## Regras de reescrita definitivas (Bypass de IA)
1. **Quebre o ritmo:** Misture frases telegráficas com frases longas e complexas.
2. **Fuja do óbvio:** Se a próxima palavra é muito previsível, troque-a.
3. **Corte as muletas:** Zero "vale ressaltar", zero "ademais".
4. **Ancore na realidade:** Use exemplos específicos que a IA não teria como prever.
5. **Auditoria:** Releia e pergunte: "Isso soa como um robô tentando soar inteligente?"
