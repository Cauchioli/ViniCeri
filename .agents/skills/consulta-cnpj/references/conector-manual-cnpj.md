# Consulta de CNPJ (dados públicos)

Conectores Jurídicos BR · Novato · CONECTOR

## Objetivo
Consulta e qualifica um CNPJ por dados públicos (situação cadastral, sócios/QSA, CNAE, endereço, capital) via API aberta, para due diligence, garantia de crédito ou aceitação de cliente. Use quando o usuário quer levantar dados oficiais públicos de uma empresa a partir do CNPJ.

## Quando usar
- Due diligence de empresa pelo CNPJ
- Checar situação/sócios antes de contratar ou litigar

## Como usar
- Baixe o arquivo SKILL.md aqui
- Crie a pasta .claude/skills/<nome-do-conector>/ e salve dentro como SKILL.md
- Abra o Claude Code (que tem acesso à internet) na pasta do seu caso
- Peça em linguagem natural — ex.: 'consulte o CNPJ X' / 'busque o processo Y no DataJud'

## Prompt

```
COMO USAR — consulta um CNPJ por dados públicos (situação cadastral, sócios/QSA, CNAE, endereço, capital).

1) Use um assistente COM acesso à internet (claude.ai no navegador com a busca ativada, ou Claude Desktop com conector web). Peça:
   "Consulte o CNPJ <NÚMERO> e me traga razão social, situação cadastral, CNAE principal, sócios (QSA), endereço e capital social."

2) Endpoint público (sem cadastro, gratuito):
   https://brasilapi.com.br/api/cnpj/v1/<CNPJ_SO_NUMEROS>
   Alternativa: https://publica.cnpj.ws/cnpj/<CNPJ_SO_NUMEROS>

3) Análise: "Com base nesses dados, aponte riscos para aceitação de cliente / garantia de crédito — a empresa está ativa? CNAE compatível? quadro societário?"

⚠️ Se aparecer "a API não permite o acesso", o problema NÃO é a API (ela é pública e está no ar) — é o assistente SEM ferramenta de navegação. Use o claude.ai no navegador com a busca ligada, ou o Claude Desktop com acesso à web.
```

## Exemplo
**Entrada:** 

**Saída:** 

_Cláudio Figueiredo Academy · Método T.O.G.A._