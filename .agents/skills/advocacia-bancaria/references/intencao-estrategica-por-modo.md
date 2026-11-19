# Intenção Estratégica por Modo (Auftragstaktik)

*Fonte normativa da disciplina de modo. Carregar o modo ativo e os de transição prevista. Em conflito com o resumo do SKILL.md em matéria de disciplina de modo, este módulo vence.*

> Cada modo é uma ordem de missão: declara o **end state** (o que deve estar verdadeiro ao final), os **restraints** (o que nunca fazer no modo), os **constraints** (o que sempre fazer), o **critério de saída** e os **pivots** de retorno. O operador executa com iniciativa dentro desses limites — não segue script.

---

## TRIAGEM

**End state:** mapa preliminar + risco central classificado + decisão fundamentada de prosseguir / declinar / redesenhar / tentar via administrativa-Procon primeiro.
**Restraints:** não diagnosticar a fundo; não redigir; não afirmar viabilidade de revisional sem identificar se há tese real além de "juros altos"; não declinar sem nomear o vício insanável.
**Constraints:** sempre fixar o lado (consumidor × instituição); sempre classificar suficiência informacional; sempre checar prazo recursal/prescrição e estado de liminar (BAF); sempre entregar recomendação explícita.
**Módulos:** motor-comum, formato-saida, perfil-julgador (se a viabilidade depender do juízo), módulo da área.
**Critério de saída:** recomendação dada + perguntas críticas listadas.
**Pivot:** se SUFICIÊNCIA = INSUFICIENTE → parar e solicitar.

---

## DIAGNÓSTICO

**End state:** diferential de teses (top 3 com probabilidade declarativa) + pivotal points nomeados (mora, pactuação da cláusula, taxa vs média BCB, notificação, nexo da fraude) + status por ponto + plano de prova. Sem redação.
**Restraints:** não redigir peça; não fixar tese única antes de testar alternativas; não afirmar abusividade sem cotejo com a taxa média BCB; não afirmar indevida a negativação sem checar preexistência e notificação.
**Constraints:** sempre montar o quadrante; sempre fixar as datas-chave; sempre avaliar risco por dimensão (incl. indébito em dobro contra o cliente); sempre invocar `devils-advocate` antes de fechar o diferential em caso de alto impacto.
**Módulos:** motor-comum, formato-saida, perfil-julgador, prova-e-documentos, módulo da área, sub-skills/devils-advocate; pesquisa-jurisprudencial se a tese for majoritariamente jurisprudencial.
**Critério de saída:** diferential fechado + pivotal points + plano de prova.
**Pivot:** descoberta de vício insanável → retorno a TRIAGEM.

---

## ESTRATÉGIA

**End state:** Curso de Ação Primário + Secundário ranqueados; Tensionamento Adversário aplicado; decisão tática por ponto; arquitetura da peça; pedidos em rascunho; faixa do threshold declarada.
**Restraints:** não pular o Tensionamento Adversário (Passo 4-A); não classificar precedente adverso como SILENCIAR sem testar distinguishing (ex.: repetitivo que valida a capitalização pactuada); não fechar arquitetura sem definir a ordem dos encargos atacados.
**Constraints:** sempre rodar `tensionamento-adversario`; sempre registrar o silêncio estratégico categorizado; sempre apresentar trade-off + recomendação.
**Módulos:** motor-comum, formato-saida, perfil-julgador, padroes-argumentativos, sub-skills/tensionamento-adversario; precedentes-distinguishing-overruling se houver precedente adverso; pericia-contabil-impugnacao se houver planilha/laudo.
**Critério de saída:** mapa aprovado pelo usuário (Passo 4).
**Pivot:** o tensionamento revela fragilidade crítica → retorno a DIAGNÓSTICO.

---

## MINUTA

**End state:** peça redigida por extenso, pronta para revisão, com `[VERIFICAR]` marcados.
**Restraints:** nunca redigir antes do mapa aprovado (salvo emergencial declarado); nunca tópico no lugar de tese desenvolvida; nunca número de Tema/Súmula não verificado sem marcação; nunca taxa/norma fora da data da contratação.
**Constraints:** sempre cadeia do motor §6.1 em cada tese; sempre evidência no corpo (cláusula transcrita, planilha, cronologia); sempre antecipar contra-argumento da instituição; sempre listar itens a verificar ao final.
**Módulos:** motor-comum, formato-saida, padroes-argumentativos, pesquisa-jurisprudencial, módulo da área, perfil-operador (voz), pericia-contabil-impugnacao se aplicável.
**Critério de saída:** todas as seções da arquitetura escritas + protocolo pós-minuta preenchido.
**Pivot:** lacuna estrutural ao redigir → retorno a ESTRATÉGIA.

---

## REVISÃO

**End state:** peça pronta para protocolo (ou retorno a Estratégia se houver falha estrutural). Avaliação global na escala irrefutável→reprovar.
**Restraints:** não aprovar peça com falha crítica; não deixar `[VERIFICAR]` não sinalizado; não revisar só a forma ignorando a substância.
**Constraints:** sempre rodar as 6 camadas de `revisao-forense`; sempre rodar `juiz-externo` (leitura adversária do julgador); sempre conferir contrato/datas/cálculo e a taxa média BCB contra a fonte; sempre varrer vestígio de texto de IA.
**Módulos:** motor-comum, formato-saida, revisao-forense, sub-skills/juiz-externo, pesquisa-jurisprudencial, _licoes-aprendidas (integral).
**Critério de saída:** avaliação global + correções priorizadas.
**Pivot:** falha crítica estrutural → retorno a ESTRATÉGIA.

---

## MANUTENÇÃO

**End state:** skill atualizada — lições incorporadas, módulos sincronizados, CHANGELOG fechado, _meta atualizado.
**Restraints:** não alterar documento de caso ativo a partir de aprendizado (lição entra na skill, nunca retroage ao caso); não bumpar versão sem registrar no CHANGELOG; não criar módulo com overlap a existente.
**Constraints:** sempre inventariar arquivos antes de editar; sempre entregar ZIP completo (todos os módulos + CHANGELOG); sempre registrar a lição em `_licoes-aprendidas.md`.
**Módulos:** _meta, _licoes-aprendidas (integral), CHANGELOG, sub-skills/_schema (se mexer em sub-skill).
**Critério de saída:** CHANGELOG fechado + ZIP regenerado.
