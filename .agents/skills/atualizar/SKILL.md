---
name: atualizar
description: Executa a atualizacao nao-destrutiva do Vertice OS v2.0 na maquina do escritorio, preservando todas as alteracoes locais feitas pelas advogadas e acoplando o Agente Fixo Preditivo, o Motor de Habitos e o Curso Vivo.
---

# Skill `/atualizar` : Upgrade Seguro sem Perder Customizacoes Locais

Quando o usuario digitar `/atualizar`:
1. Execute `python scripts/aplicar_upgrade_v2.py` para fazer backup dos arquivos locais em `_backups_locais/` e acoplar o bloco do Agente Fixo Preditivo ao final do `AGENTS.md`, `CLAUDE.md` e `GEMINI.md` locais sem apagar nenhuma regra existente do escritorio.
2. Leia `00_MANIFESTO_MODULOS_INSTALADOS.md` e apresente um resumo em 6 linhas das novidades ativas (`/treinar`, `/visual-law`, `/audiencia`, Motor de Habitos Sequenciais e Bussola de Antecipacao), encerrando ja com a **Bussola de Antecipacao (opcoes 1, 2 ou 3)**.
