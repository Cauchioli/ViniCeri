# Intenção Estratégica por Modo — Skill Tributária

Este módulo define a regulamentação interna e critérios de transição para cada um dos 6 modos de raciocínio da skill.

---

## 1. MODO TRIAGEM
- **Intenção**: Identificar urgência, conflitos de interesse, código de área aplicável e viabilidade econômica básica do passivo.
- **Constraints**:
  - Exigir os dados de eCAC/PGFN iniciais.
  - Verificar se a empresa tem capacidade mínima de caixa antes de prosseguir.
- **Critério de Saída**: Cadastro de passivo inicial preenchido e decisão de admissão fundamentada.

---

## 2. MODO DIAGNÓSTICO
- **Intenção**: Mapear detalhadamente a matriz de cenários fiscais quantitativos e identificar as fragilidades e lacunas contábeis do cliente.
- **Constraints**:
  - Aplicar a fórmula de desconto efetivo real.
  - Mapear os riscos criminais dos administradores.
- **Critério de Saída**: Matriz de cenários gerada em tabela e lista de lacunas contábeis apresentada.

---

## 3. MODO ESTRATÉGIA
- **Intenção**: Definir o curso de ação jurídica, realizar o gate de bifurcação MS × Ação Ordinária e a arquitetura das peças e propostas de transação.
- **Constraints**:
  - Executar a sub-skill `devils-advocate.md` para atacar as premissas de defesa antes de fixá-las.
  - Realizar a simulação da contestação da PGFN (sub-skill `tensionamento-adversario.md`).
- **Critério de Saída**: Aprovação do plano de peça pelo usuário.

---

## 4. MODO MINUTA
- **Intenção**: Redigir as petições judiciais de defesa, propostas de transação individual (TPI) ou pareceres societários.
- **Constraints**:
  - Sinalizar placeholders e dados pendentes com a marcação `[VERIFICAR]`.
  - Manter a sobriedade e o rigor técnico na escrita, evitando adjetivos vazios contra o Fisco.
- **Critério de Saída**: Minuta de alta densidade técnica entregue ao operador.

---

## 5. MODO REVISÃO
- **Intenção**: Auditar a minuta em 6 camadas fiscais e simular a decisão judicial ou administrativa para assegurar a blindagem do protocolo.
- **Constraints**:
  - Executar a sub-skill `juiz-externo.md` (conselheiro CARF ou julgador federal).
  - Eliminar todos os termos `[VERIFICAR]` ou justificar os pendentes.
- **Critério de Saída**: Peça chancelada para protocolo com parecer de conformidade de 6 camadas.

---

## 6. MODO MANUTENÇÃO
- **Intenção**: Atualizar a base de dados da skill a partir de mudanças normativas federais ou jurisprudência consolidada recente.
- **Constraints**:
  - Registrar as novas diretrizes em `references/_licoes-aprendidas.md`.
  - Atualizar o arquivo `references/_meta.md` e o `CHANGELOG.md`.
- **Critério de Saída**: Changelog fechado com nova versão de skill catalogada.
