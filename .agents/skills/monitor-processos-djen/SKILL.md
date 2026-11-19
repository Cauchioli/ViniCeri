---
name: monitor-processos-djen
description: Faz triagem de publicações processuais cruzando DJen e Gmail por OAB, remove duplicatas, classifica por urgência de prazo e gera relatório PDF. Use para monitoramento processual recorrente no Cowork.
---

# Monitor de Processos (DJen + Gmail)

Triagem processual recorrente para advocacia. Quando acionada — manualmente ou por tarefa agendada — esta skill cruza as publicações do DJen com os e-mails de tribunais, deduplica, classifica por urgência de prazo e entrega um relatório em PDF.

## Configuração obrigatória

Antes de usar, preencha o valor abaixo e mantenha-o no corpo desta skill:

- **OAB monitorada:** `[NÚMERO]/[SECCIONAL]`

Se nenhuma OAB estiver preenchida aqui nem informada na tarefa, **pergunte antes de prosseguir** — nunca presuma um número.

## Pré-requisitos de acesso (verifique antes de executar)

- **Gmail conectado** no menu de Conectores.
- **Um caminho real de acesso ao DJen.** Não existe ferramenta "DJen" nativa. O acesso a `comunica.pje.jus.br` depende de **Claude in Chrome** ativo (navegação da página de consulta) ou de um **conector/MCP** que consuma a API pública de comunicações do CNJ.
- Se **nenhum** caminho de acesso ao DJen estiver disponível, **não simule a consulta**: gere o relatório apenas com a fonte Gmail e registre no topo, em destaque, que a fonte DJen ficou indisponível nesta execução.

## Procedimento

Considere sempre a **data de hoje** (o dia em que esta execução está rodando — cada rodada agendada abre uma sessão nova, então a data corrente é a do dia).

1. **DJen.** Acesse `comunica.pje.jus.br` e consulte as publicações disponibilizadas **nos últimos 5 dias corridos até hoje**, filtrando pela OAB configurada, em todo o território nacional.
2. **Gmail.** Identifique os e-mails recebidos **nos últimos 5 dias** contendo publicações, intimações ou comunicações de tribunais.
3. **Consolidação.** Una as duas fontes removendo duplicatas — mesmo processo + mesma data + mesmo teor contam como um único item.
4. **Classificação por prazo.** Calcule o prazo pela regra do DJen — a publicação considera-se feita no primeiro dia útil seguinte à disponibilização, e o prazo corre do primeiro dia útil seguinte à publicação:
   - **URGENTE** — vence em até 3 dias úteis
   - **ATENÇÃO** — vence em até 7 dias úteis
   - **MONITORANDO** — sem prazo imediato ou apenas ciência
5. **Relatório.** Gere um PDF estruturado por urgência. Para cada item: número do processo, tribunal, data de disponibilização, prazo estimado e teor resumido. **Marque explicitamente** qualquer item cujo prazo não tenha sido calculado com segurança.
6. **Salvaguarda de varredura.** Ao final, liste quais dias dentro da janela de 5 dias **não** retornaram nenhuma publicação, para permitir identificar falhas de varredura.

## Regras de segurança (não negociáveis)

- A janela de **5 dias com dedupe** é proposital: a tarefa agendada do Cowork só roda com o computador ligado e o app aberto, então a varredura precisa recuperar dias eventualmente pulados. Não reduza para D-1/D.
- Este relatório é **triagem, não substituto da conferência oficial**. A responsabilidade pelo prazo permanece do advogado. Registre essa ressalva no rodapé do PDF.
- Diante de qualquer dúvida no cálculo de prazo, classifique o item no nível **mais urgente** plausível e sinalize a incerteza — nunca subestime um prazo.

## Base normativa

Regra de contagem do art. 224 do CPC c/c Resolução CNJ nº 455/2022 (DJen como canal oficial de publicação). Confirme a regra vigente antes de confiar no cálculo automático.
