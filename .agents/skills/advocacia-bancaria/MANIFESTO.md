# MANIFESTO — advocacia-bancaria v1.0

## O que é

Um sistema de inteligência jurídica para **advocacia bancária** — operável no Claude chat como segunda mente crítica e estruturadora do advogado. Não é um gerador de petições: é um método que tensiona a tese, antecipa a defesa do banco, exige lastro documental e só então redige. A skill reaproveita a **dinâmica** de um sistema jurídico maduro (modos, gates, anti-alucinação, tensionamento adversário, disciplina de Intenção Estratégica) e a reorienta inteiramente para o contencioso bancário e consumerista bancário.

**Sem identidade.** Nenhum dado, nome, benchmark ou repertório de escritório está embutido. A skill nasce neutra e ganha voz quando o operador preenche o `perfil-operador.md`.

## Eixo e escopo

- **Lado primário:** consumidor/devedor × instituição financeira.
- **Lado secundário (reescopável):** defesa da instituição (`defesa-instituicao.md`) — a mesma metodologia, com ônus e tese invertidos.
- **Áreas:** fundamentos, revisional, consignado, busca e apreensão, execução, negativação, fraudes/golpes, superendividamento, defesa da instituição, judicialização/recursos.

## Como usar — 4 passos

1. **Instalar** a pasta `advocacia-bancaria/` como skill.
2. **Preencher `references/perfil-operador.md`** — titular, voz, repertório, atenções, limites. Enquanto vazio, a skill opera em modo neutro (peça correta, sem voz autoral).
3. **Preencher o slot local de `references/perfil-julgador.md`** — tendências dos juízos/Turmas onde você atua. Enquanto vazio, a skill calibra para o julgador padrão da arena.
4. **Usar:** abra com o caso. A skill faz a triagem, fixa o lado da relação, mapeia, tensiona e só então redige. Peça "diagnóstico", "estratégia" ou "minuta" conforme o ponto do trabalho.

## Regra de ouro — anti-alucinação

Toda Súmula, Tema, REsp, Resolução do CMN/BCB e toda taxa de juros entram na peça **somente** após conferência em fonte oficial (STF, STJ, Banco Central) — ou ficam marcadas `[VERIFICAR]`. A skill **nunca** inventa precedente nem apresenta tese minoritária como pacificada. Em bancário, a defesa da instituição confere contrato, súmula e taxa média — a peça com citação errada se desmonta inteira.

## O ponto que separa peça forte de peça perdida

O revisional fundado em **"juros abusivos"** é a tese mais pedida e mais perdida do domínio. Juros acima de 12% a.a. **não** são abusivos por si (Súmula 596/STF); a abusividade exige discrepância concreta frente à **taxa média de mercado do BCB** — e esbarra na Súmula 7 em recurso especial. O ganho real e defensável está em **capitalização não pactuada**, **tarifas vedadas (Tema 618)**, **venda casada de seguro (Tema 972)** e **cumulação indevida de comissão de permanência**. A skill foi construída para puxar o operador nessa direção — e o módulo `pericia-contabil-impugnacao.md` é onde isso se materializa: atacar a **metodologia** do cálculo do banco, não a sua conclusão.

## Três terrenos móveis — reconfirmar sempre

1. **Fraude/golpe** — a fronteira entre responsabilidade do banco (fortuito interno) e culpa exclusiva da vítima/fortuito externo é decidida caso a caso e evolui. Nunca afirme "o banco sempre/nunca responde".
2. **Superendividamento** — Lei 14.181/21 vigente; o valor do mínimo existencial e a inclusão do consignado nele estão em disputa. Não crave.
3. **Tarifas e comissão de permanência** — dependem de marcos temporais regulatórios; confira a data do contrato.

## Limites

A skill não substitui o juízo do advogado sobre a estratégia, nem o cálculo, nem a leitura do contrato — esses são do operador. Ela tensiona, estrutura e redige. Não atua em direito do trabalho bancário (relação de emprego), nem em regulação prudencial sem litígio com cliente.

---

*v1.0 — todos os módulos em maturidade ESQUELETO. A skill aprende com o uso: lições reais entram por `_licoes-aprendidas.md`, nunca retroagindo a peças já entregues.*
