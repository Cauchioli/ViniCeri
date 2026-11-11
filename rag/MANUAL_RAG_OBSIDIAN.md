# Vértice OS: Segundo Cérebro e RAG Local

Este manual descreve o funcionamento, a estrutura de organização e os comandos operacionais do **Segundo Cérebro e RAG Local** do Vértice OS.

---

## 1. Arquitetura: Memória Curada vs. Acervo Bruto

Para manter o ambiente de trabalho leve e rastreável, o conhecimento opera em duas camadas complementares:

1. **Notas de Contexto e Regras (`AGENTS.md`, `1-contexto/`):** Regras de negócio, identidade da marca, fluxos operacionais e decisões permanentes. Quando o caminho exato desses arquivos é conhecido e eles precisam ser lidos na íntegra ou editados, o assistente realiza **leitura direta**.
2. **RAG Local (`rag/`):** Banco vetorial 100% local (LanceDB + embeddings multilíngues) que indexa milhares de documentos (`.pdf`, `.docx`, `.txt`, `.md`, `.csv`, `.xlsx`) sem enviar dados para fora da máquina (conformidade com LGPD e sigilo profissional).

---

## 2. Instalação e Indexação

### A. Instalação das Dependências
Abra o terminal na pasta `rag` e execute:
```bash
python install_rag.py
```

### B. Indexação Incremental do Acervo
Para indexar novos arquivos ou atualizar arquivos modificados:
```bash
python rag_acervo.py index
```
Para indexar uma pasta específica do servidor ou computador:
```bash
python rag_acervo.py index "C:\caminho\da\pasta"
```

### C. Servidor Residente de Busca Instantânea (Opcional, 0.05s por busca)
Para manter o modelo carregado em memória RAM e responder consultas instantaneamente:
```bash
iniciar_rag.bat
```

---

## 3. Regra de Consulta Otimizada para Agentes de IA

Sempre que o assistente precisar consultar precedentes, modelos de peças, contratos, propostas ou histórico no acervo:

1. **Consulta Unificada em Lote (Multi-Query):** Nunca executar múltiplas chamadas separadas ao terminal. Passar todas as perguntas em um único comando para carregar o modelo apenas uma vez (ou bater no servidor residente na porta `8799`):
   ```bash
   python rag.py "pergunta 1" "pergunta 2" -f "termo_de_filtro" -k 5
   ```
2. **Retorno de Bloco Completo (1.200 caracteres):** O `rag.py` e o `rag_acervo.py` devolvem por padrão o trecho completo de 1.200 caracteres junto com o caminho absoluto da **FONTE**, eliminando a necessidade de abrir arquivos secundários após a busca.
3. **Ancoragem Fática (Grounding):** Toda resposta ou peça gerada a partir do acervo deve citar o caminho do arquivo-fonte retornado pelo RAG.
