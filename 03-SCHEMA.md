# Especificação de Schema YAML: Vértice OS (Dr. Vinícius Cerineo)

Toda nota gerada no Segundo Cérebro (seja resumo de caso, nota de raciocínio `_RACIOCINIO.md`, ata comercial ou conversa importada do ChatGPT/Claude) segue o cabeçalho YAML abaixo para indexação precisa no RAG local:

```yaml
---
tipo: caso | raciocinio_peca | modelo | tese | comercial | administrativo | historico_ia | skill
cliente: "Nome do Cliente ou Empresa"
processo_ou_caso: "Número CNJ ou Identificador no ADVBOX"
pilar: juridico | comercial | administrativo | financeiro
responsavel: "Dr. Vinícius Cerineo | André | Beatriz | Danilo | Fernando | Gabi"
caminho_onedrive: "Caminho relativo na pasta do OneDrive"
atualizado_em: "AAAA-MM-DD"
status: ativo | aguardando_revisao | concluido
---
```
