@echo off
title Atualizacao Segura Vertice OS v2.0 (Sem Perda de Dados Locais)
cd /d "%~dp0"

echo [1/3] Guardando suas alteracoes locais em seguranca (git stash)...
git stash push -m "salvando-nuances-locais-antes-do-upgrade-v2"

echo [2/3] Baixando as novas skills, Curso Vivo e Agente Preditivo do GitHub...
git pull origin main

echo [3/3] Restaurando suas alteracoes locais e acoplando o Agente Preditivo...
git stash pop
python scripts\aplicar_upgrade_v2.py

echo.
echo [OK] Sistema atualizado para a v2.0 com todas as suas customizacoes preservadas!
pause
