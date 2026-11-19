---
name: organizador-de-documentos
description: Organiza e renomeia uma pasta de documentos jurídicos (PDF, DOCX, imagens) — lê o conteúdo de cada arquivo, propõe nomes padronizados (data_tipo_parte_assunto) e gera um índice navegável. Use quando o usuário tem uma pasta bagunçada de documentos de um processo, caso ou cliente e quer padronizar e indexar antes de trabalhar.
---

# Organizador de Documentos Jurídicos

Você organiza uma pasta de documentos de um caso/processo: lê o que cada arquivo é, propõe um nome padronizado e monta um índice. O objetivo é transformar uma pasta caótica em um acervo navegável — sem perder nada.

## Quando usar
- O usuário aponta uma pasta com PDFs/DOCX/imagens de um processo ou cliente.
- Pede para "organizar", "renomear", "indexar" ou "dar um jeito nessa bagunça".

## Inputs necessários
- O **caminho da pasta**. Se não foi dado, pergunte antes de qualquer coisa.
- (Opcional) convenção de nome preferida do escritório. Se não houver, use a padrão abaixo.

## Passos
1. Liste todos os arquivos da pasta (e subpastas, se o usuário pedir).
2. Para cada arquivo, leia/escaneie o conteúdo o suficiente para classificar: **tipo** (petição, decisão, contrato, procuração, comprovante, intimação, parecer, etc.), **data** do documento, **parte/autor** quando houver.
3. Proponha um nome no padrão: `AAAA-MM-DD_tipo_parte_assunto` (ex.: `2026-03-14_peticao-inicial_silva_danos-morais.pdf`). Sem espaços, sem acento, minúsculas.
4. **Apresente a tabela de "nome atual → nome proposto" e PEÇA CONFIRMAÇÃO antes de renomear em lote.**
5. Após o ok, renomeie. Em caso de nome duplicado, acrescente sufixo `_2`, `_3` (nunca sobrescreva).
6. Gere um `_INDICE.md` na pasta: tabela com nome final, tipo, data, 1 linha de resumo e link relativo.

## Convenção de nome padrão
`AAAA-MM-DD_tipo_parte_assunto.ext` — data do documento (não a de hoje), tipo em uma palavra, parte principal, assunto curto.

## Regras invioláveis
- **Nunca apague** arquivo. Em dúvida, mova para uma subpasta `_revisar/` e avise.
- **Nunca renomeie em lote sem confirmação** explícita do usuário.
- Se um arquivo for ilegível/escaneado sem texto, sinalize "precisa de OCR" em vez de adivinhar o conteúdo.
- Preserve a extensão original.

## Saída
Pasta renomeada + `_INDICE.md` + um resumo do que foi feito (quantos arquivos, quantos pendentes de OCR/revisão).
