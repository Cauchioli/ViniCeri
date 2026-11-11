@echo off
chcp 65001 >nul
title Vértice OS - Setup Inicial (Dr. Vinícius Cerineo)
echo ============================================================================
echo   VÉRTICE OS : SEGUNDO CÉREBRO JURÍDICO E OPERACIONAL
echo   Escritório Dr. Vinícius Cerineo
echo ============================================================================
echo.
echo [1/4] Absorvendo arquivos e skills da pasta CLAUDIO + Historicos ChatGPT/Claude...
python scripts\ingerir_pasta_claudio_e_historico.py
echo.
echo [2/4] Detectando OneDrive do escritorio e configurando o buscador RAG...
python scripts\scanner_onedrive.py
echo.
echo [3/4] Verificando dependencias do motor RAG local...
python rag\install_rag.py
echo.
echo [4/4] Indexando Segundo Cerebro e OneDrive no RAG local...
python rag\rag_acervo.py index
echo.
echo ============================================================================
echo   SETUP TÉCNICO BASE CONCLUÍDO!
echo   Agora abra esta pasta no Claude Code e digite: /instalar
echo   para concluir a entrevista guiada passo a passo.
echo ============================================================================
pause
