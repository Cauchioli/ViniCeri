# -*- coding: utf-8 -*-
"""
Instalador automatizado do RAG Local Vértice OS.
"""
import sys
import subprocess

def install_packages():
    packages = [
        "lancedb",
        "sentence-transformers",
        "torch",
        "pdfplumber",
        "python-docx",
        "openpyxl"
    ]
    print("[Vertice OS] Instalando dependencias do RAG local...")
    for pkg in packages:
        print(f"-> Instalando {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "--quiet"])
    print("\n[Vertice OS] Todas as dependencias do RAG local foram instaladas com sucesso!")

if __name__ == "__main__":
    install_packages()
