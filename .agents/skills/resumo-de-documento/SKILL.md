---
name: resumo-de-documento
description: Lê uma decisão judicial, petição, contrato ou parecer e devolve um resumo executivo estruturado (partes, objeto, fundamentos, dispositivo, prazos e próximos passos). Use quando o usuário precisa entender rápido um documento jurídico longo sem ler tudo.
---

# Resumo Executivo de Documento Jurídico

Você lê um documento jurídico e devolve um resumo executivo que cabe em uma tela — fiel ao texto, sem inventar nada.

## Quando usar
- O usuário fornece um documento (decisão, sentença, acórdão, petição, contrato, parecer, intimação) e quer o essencial rápido.

## Inputs necessários
- O **documento** (arquivo ou texto colado). Se não veio, peça.
- (Opcional) o que o usuário mais quer saber (prazo? risco? fundamento?). Se disser, priorize isso.

## Passos
1. Leia o documento inteiro antes de resumir.
2. Identifique o tipo de documento — o resumo muda conforme seja decisão, contrato ou petição.
3. Extraia os elementos do template abaixo. **Só inclua o que está no documento.**
4. Marque prazos em destaque e calcule a data final quando a contagem for clara (sinalize a regra usada).

## Template de saída
- **Tipo e origem:** (ex.: Sentença, 3ª Vara Cível de BH)
- **Partes:** autor × réu (ou contratantes)
- **Objeto / pedido:** o que se discute
- **Fundamentos principais:** os pilares da argumentação/decisão
- **Dispositivo / conclusão:** o que ficou decidido/acordado
- **Prazos:** ⏰ com data final quando calculável
- **Próximos passos sugeridos:** (marcados como sugestão, não obrigação)

## Regras invioláveis
- **Não invente.** Se algo (valor, prazo, fundamento) não consta, escreva "não consta no documento".
- Não dê opinião jurídica definitiva — o resumo é insumo, não parecer.
- Cite o trecho/página quando a informação for sensível (valor, prazo, condenação).

## Saída
O resumo no template acima, em prosa enxuta, pronto para colar no caso.
