---
name: consulta-cnpj
description: Consulta e qualifica um CNPJ por dados públicos (situação cadastral, sócios/QSA, CNAE, endereço, capital) via API aberta, para due diligence, garantia de crédito ou aceitação de cliente. Use quando o usuário quer levantar dados oficiais públicos de uma empresa a partir do CNPJ.
---

# Consulta de CNPJ (dados públicos)

Você consulta o cadastro público de uma empresa pelo CNPJ e devolve uma ficha qualificada — para o advogado decidir contratar, litigar ou conceder crédito.

## Quando usar
- Due diligence de empresa, garantia de crédito, aceitação de cliente, habilitação em licitação.

## Inputs necessários
- O **CNPJ** (14 dígitos). Se não veio, peça.
- (Opcional) o objetivo (solvência? sócios? regularidade?) — orienta a leitura.

## Passos
1. Consulte a API pública: `https://brasilapi.com.br/api/cnpj/v1/{cnpj}` (aberta, sem chave) [VERIFICAR disponibilidade/limite vigente; alternativa ReceitaWS].
2. Extraia: razão social, nome fantasia, situação cadastral, data de abertura, porte, capital social, CNAE principal e secundários, endereço, e o **QSA (sócios)**.
3. Qualifique para o objetivo: empresa ativa? porte compatível? sócios que cruzam com a parte adversa/cliente? atividade condizente?
4. Para due diligence de litígio, combine com a skill `due-diligence-de-parte`.

## Regras invioláveis
- **Só dado público.** A API não expõe CPF completo dos sócios — não tente obter por outras vias.
- Não tire conclusão difamatória — relate o dado com a fonte (data da consulta).
- É insumo, não certidão oficial — para prova, oriente a emissão da certidão no portal da Receita.

## Saída
Ficha do CNPJ (cadastro + QSA + CNAE) + leitura de qualificação/risco para o objetivo informado.
