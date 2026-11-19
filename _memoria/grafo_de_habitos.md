# Grafo de Habitos e Padroes Sequenciais do Escritorio

> Atualizado automaticamente pelo Agente Fixo Preditivo e por `scripts/motor_habitos.py`.
> Sempre que uma transicao `Tarefa A -> Tarefa B` atinge 2x, ela vira a Opcao 1 da Bussola de Antecipacao. Ao atingir 3x, o agente sugere transformar em atalho unico.

## 1. Transicoes Registradas (Contagem e Antecipacao)

| Tarefa Anterior (A) | Proximo Passo Observado (B) | Contagem | Status de Automacao |
|---|---|---|---|
| `Analise / Resumo de Autos ou Caso` | `Minuta no Papel Timbrado + Nota _RACIOCINIO.md` | 2 (padrao base) | Ativo na Opcao 1 da Bussola |
| `Transcrição / Audio de Reuniao com Cliente` | `Ata Comercial + Anamnese CRF + Proposta de Honorarios` | 2 (padrao base) | Ativo na Opcao 1 da Bussola |
| `Minuta de Peca Contenciosa (Inicial/Contestacao/Replica)` | `Auditoria Juiz Externo + Quadros de Visual Law` | 2 (padrao base) | Ativo na Opcao 1 da Bussola |
| `Triagem de Documentos nos Downloads` | `Organizacao na Pasta do Cliente + Checklist ADVBOX/Astrea` | 2 (padrao base) | Ativo na Opcao 1 da Bussola |

## 2. Historico Recente de Sequencias Aprendidas
- *(Novos padroes reais da equipe serao adicionados aqui conforme o uso diario)*
