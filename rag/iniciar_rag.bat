@echo off
title RAG Local - Vertice OS
cd /d "%~dp0"

echo [+] Iniciando Servidor Residente RAG (Porta 8799)...
set RAG_DEVICE=cpu
if exist ".venv\Scripts\python.exe" (
    start "RAG Server" /min .venv\Scripts\python.exe rag_server.py
) else (
    start "RAG Server" /min python rag_server.py
)

echo [OK] Servidor RAG local disparado em background!
timeout /t 3
