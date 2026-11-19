# Pesquisa Jurisprudencial e Protocolo VersionRAG

Este módulo orienta a pesquisa e a validação de precedentes do STF, STJ, TRFs e CARF aplicáveis às demandas tributárias federais, implementando o protocolo anti-alucinação jurisprudencial.

---

## 1. O PROTOCOLO VERSIONRAG TRIBUTÁRIO

O Direito Tributário brasileiro é altamente dinâmico e sujeito a mutações constitucionais (como a Reforma Tributária da EC 132/23). Um precedente antigo pode estar formalmente ativo nos buscadores jurídicos por IA, mas materialmente revogado por uma nova Lei Complementar ou Tema Vinculante do STF.

Para mitigar a alucinação jurisprudencial, a skill deve aplicar a verificação de data-base de precedentes:

1. **Checagem de Anterioridade**: Antes de citar qualquer tese jurisprudencial, verificar a data do julgado e confrontá-la com marcos legislativos (ex: alterações da Lei 11.101/05 em 2020; nova lei de transações em 2022; devedor contumaz em 2023).
2. **Validação de Súmulas e Repetitivos**:
   - Para Súmulas do STJ (ex: Súmula 430): Confirmar no portal oficial se não há proposta de revisão ou cancelamento ativa.
   - Para Temas do STF (ex: Tema 122 ou Tema 796): Checar se houve modulação de efeitos temporal pendente ou embargos de declaração julgados recentemente.
3. **Prosa Segura**: Se o operador solicitar a aplicação de um Tema do qual a skill não tem o inteiro teor validado na base de dados oficial, a skill deve redigir em prosa segura (ex: *"A jurisprudência pacificada do Supremo Tribunal Federal, sob a sistemática de repercussão geral, orienta no sentido de afastar a sucessão..."*), incluindo a marcação `[VERIFICAR inteiro teor do Tema X]`.

---

## 2. PORTAIS E FONTES DE PESQUISA HOMOLOGADOS

A skill prioriza a busca de jurisprudência e normas nos seguintes portais oficiais:

- **STF**: `portal.stf.jus.br` (Temas de Repercussão Geral, ADIs, Súmulas Vinculantes).
- **STJ**: `www.stj.jus.br` (Temas Repetitivos, Súmulas ordinárias).
- **PGFN**: `www.pgfn.fazenda.gov.br` (Pareceres vinculantes da PGFN, portarias regulamentadoras de transações).
- **CARF**: `carf.economia.gov.br` (Súmulas do CARF, Acórdãos das Câmaras Superiores de Recursos Fiscais).
- **Planalto**: `www.planalto.gov.br` (Texto compilado e vigente das Leis Federais e Constituição).
