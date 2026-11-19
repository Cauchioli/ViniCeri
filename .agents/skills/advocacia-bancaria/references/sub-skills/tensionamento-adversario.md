# Sub-skill: Tensionamento Adversário

## 1. PROPÓSITO
Simular a peça que a instituição financeira construirá **em resposta** à tese da casa, em primeira pessoa adversária e frontal, produzindo os ataques previsíveis para que sejam antecipados e desmontados dentro da própria peça.

## 2. QUANDO ACIONAR
- **Modos:** ESTRATÉGIA (Passo 4-A, após o mapa) e MINUTA (antes da versão final).
- **Condições de entrada:** existe tese central + arquitetura definida.
- **Anti-gatilhos:** não acionar antes de haver tese (use devils-advocate); não acionar para revisar peça pronta sob a ótica do juiz (use juiz-externo).

## 3. ENTRADA ESTRUTURADA
- Obrigatório: tese central + teses subsidiárias + os pontos do quadrante DESFAVORÁVEL.
- Opcional: contestação padrão do banco na matéria, se disponível.
- Validação: rejeita operar se a tese ainda não passou por mapa.

## 4. PROCESSAMENTO
**Versão mínima (todos os casos):**
1. Premissa fática mais atacável — qual afirmação (inexistência de pactuação, ausência de mora, ausência de notificação, nexo da fraude), se desconstruída, derruba o pedido? Está provada ou depende de inferência?
2. Premissa jurídica mais frágil — qual tese, se rejeitada, compromete a arquitetura? Há subsidiária (expurgo parcial, depósito do incontroverso) que salva o resultado?
3. Premissa normativa — alguma norma/súmula usada além do alcance? O banco arguirá pactuação expressa (capitalização — Súmulas 539/541), legalidade da taxa (Súmula 596) ou culpa exclusiva da vítima?

**Versão integral (alto impacto):**
- O que a instituição vai atacar (fática, jurídica, probatória — descrito como ela atacaria).
- Argumentos que construirá (primeira pessoa adversária, frontal: "a taxa praticada situa-se na média de mercado; a capitalização foi expressamente pactuada na cláusula X; o autor encontrava-se em mora").
- Precedentes que citará contra (repetitivos/Súmulas reconhecidamente usáveis a favor do banco — verificar via pesquisa-jurisprudencial).
- Fragilidades reais (sem suavização).
- Reforço necessário ao CoA antes da minuta.

**Quando há planilha/laudo contábil:** acrescentar as três perguntas de `pericia-contabil-impugnacao.md` (a planilha explicita taxa, amortização e capitalização? o recálculo parte de premissa válida? a peça resiste se o juízo acolher a planilha do banco?).

## 5. SAÍDA ESTRUTURADA
```
TENSIONAMENTO ADVERSÁRIO — [versão mínima / integral]
Ataque 1 (fático): [como o banco argumenta] → Resposta a embutir na peça: [...]
Ataque 2 (jurídico): [...] → Resposta: [...]
Ataque 3 (normativo/pactuação): [...] → Resposta: [...]
[integral] Precedentes adversos previsíveis: [verificados]
Fragilidades reais: [nomeadas]
REFORÇO ANTES DA MINUTA: [modificações ao CoA]
```

## 6. RESTRIÇÕES
- Não inventa precedente adverso — se citar Súmula/repetitivo contra, verifica. Não suaviza a fragilidade real. Não redige a peça final.

## 7. ARTICULAÇÃO
Sucede `devils-advocate`. Alimenta a Camada 5 da `revisao-forense` (que opera depois, sobre a peça pronta). Precede a redação final.

## 8. CRITÉRIO DE SAÍDA
Três ataques (mínima) ou bloco integral (alto impacto) + reforços registrados antes da minuta.

## 9. ANTI-PADRÕES
- Ataque genérico ("o banco vai contestar") sem nomear a premissa específica.
- Citar precedente adverso de memória.
- Registrar o ataque e não embutir a resposta na peça → o tensionamento vira teatro.

## 10. NOTA DE MANUTENÇÃO
v1.0 — criação.
