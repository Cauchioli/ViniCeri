---
name: visual-law
description: Aplica Visual Law tecnico na peca processual pronta em DOCX sem alterar uma virgula da tese, pedido, valor ou prova. Audita coerencia (valores, datas, IDs de documentos) e gera os 3 quadros escaneaveis no Papel Timbrado.
---

# Skill `/visual-law` : Visual Law na Peca sem Mexer na Tecnica

Inspirada na metodologia forense validada (T.O.G.A. Nov/2026). Funciona para Inicial, Contestacao, Replica, Embargos, Apelacao, Agravo, REsp e RE.

## Passo 1: Auditoria de Coerencia Formal (Antes de diagramar)
Leia a peca pronta (`.docx` ou `.md`) e a lista de documentos dos autos. Aponte imediatamente qualquer pendencia de coerencia:
1. Valor numerico divergente do valor por extenso ou com digitos trocados entre a narrativa e os pedidos;
2. Datas fora de ordem cronologica na narrativa dos fatos;
3. Documento citado no corpo da peca que nao consta na lista de anexos/IDs dos autos.

## Passo 2: Proposta dos 3 Elementos Visuais (Sem mudar a tese)
Monte e apresente para aprovacao do advogado os **3 quadros de navegacao rapida para o magistrado e assessor**:
1. **Quadro-Resumo dos Pedidos (ou Quadro Sinotico de Impugnacao, se for Contestacao):** copiado fielmente dos pedidos da peca, organizado em tabela limpa (`Item | Pedido / Tese | Fundamento Legal`).
2. **Linha do Tempo dos Fatos em Tabela:** (`Data | Evento Fatico | Documento Comprobatorio / ID`).
3. **Tabela Fato x Prova x ID do Documento:** amarrando cada alegacao central ao documento exato dos autos.

## Passo 3: Aplicacao no Papel Timbrado Oficial
Apos o `ok` do advogado, gere uma copia da peca no Papel Timbrado do escritorio inserindo os quadros aprovados e confirme que nenhum argumento, pedido ou valor do texto original foi alterado.
