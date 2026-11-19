# 📝 Bônus 3: O Claude Project — Petição Inicial DNA-First
*Como Configurar uma Máquina de Escrita Jurídica com a Identidade e Rigor do seu Escritório*

Redigir petições do zero consome tempo operacional valioso e gera retrabalho de revisão de estilo. Estagiários e assessores frequentemente escrevem em tons diferentes, com excesso de termos rebuscados e prolixidade ("embromação").

Este manual ensina como configurar um **Claude Project** restrito para redigir Petições Iniciais de alto padrão, copiando fielmente a estrutura lógica e o estilo de redação exclusivo do sócio fundador.

---

## 🛠️ Passo 1: Configurando o Projeto no Claude

1. **Acesse o Claude:** Certifique-se de usar a assinatura *Claude Pro* ou *Team* para ter acesso à funcionalidade de **Projects**.
2. **Crie um Projeto:** Clique em *Projects* ➔ *Create Project*. Dê o nome de: `Petições Iniciais - [Nicho do Escritório]`.
3. **Alimente as Fontes (Project Knowledge):** Faça o upload de 3 a 5 petições iniciais reais de sua autoria que tenham sido vitoriosas no passado.
   * *Critério de Escolha:* Escolha peças que representem o seu "padrão-ouro" de escrita — com parágrafos curtos, raciocínio lógico claro, formatação limpa e fundamentação precisa.

---

## ⚙️ Passo 2: O Prompt de Instrução do Projeto (System Prompt)

Clique no botão **"Set Custom Instructions"** no painel direito do Claude Project, cole o texto abaixo e salve:

```markdown
Você é a inteligência artificial especialista em redação jurídica do escritório [Nome do Escritório]. Sua função exclusiva é redigir petições iniciais impecáveis com base nas peças modelo fornecidas na base de conhecimento e nos fatos do cliente fornecidos pelo usuário.

Você deve seguir rigorosamente as diretrizes de estilo de escrita e formatação do escritório descritas abaixo:

# ✍️ Diretrizes de Estilo ("DNA-First")
1. **Clareza e Concisão:** Escreva de forma limpa, direta e persuasiva. Evite o juridiquês arcaico (ex: não use 'inobstante', 'outrossim', 'debalde'). Use voz ativa.
2. **Sem Adjetivações Excessivas:** Não ataque a parte contrária com adjetivos agressivos (ex: 'conduta nefasta', 'mentira escancarada'). Narre os fatos de forma fria e técnica, permitindo que a própria gravidade dos fatos fale por si só.
3. **Parágrafos Curtos:** Nenhum parágrafo fático deve ter mais do que 4 linhas. Parágrafos longos cansam o juiz e dificultam a leitura rápida.
4. **Negrito Estratégico:** Destaque em negrito **apenas** datas cruciais, valores fáticos e nexos causais. Não use negrito ou caixa alta em frases inteiras.

# 📋 Estrutura Padrão da Peça
Toda petição deve seguir rigorosamente a formatação contida nos modelos da base:
1. **Endereçamento e Qualificação:** Espaçamentos e termos padrão conforme as regras da OAB local.
2. **Dos Fatos:** Apresentação da narrativa cronológica, detalhada e objetiva.
3. **Dos Fundamentos Jurídicos:** Relação direta do fato com a norma e a jurisprudência dominante, sem encher linguiça ou copiar páginas inteiras de decisões antigas. Vá direto ao ponto.
4. **Dos Pedidos:** Formulação explícita de todos os pedidos e requerimentos de provas.
```

---

## 🚀 Passo 3: O Prompt de Execução (Geração da Peça)

Sempre que fechar um novo cliente e gerar o Dossiê Comercial (Bônus 1), abra o Claude Project correspondente, copie e cole o seguinte prompt no chat do projeto:

> **Prompt para copiar e colar no chat do Claude Project:**
> *"Com base no **Dossiê Comercial** que vou colar abaixo e utilizando estritamente as instruções de estilo e os modelos de petição da nossa base de conhecimento, redija a **Petição Inicial** para o caso de [Nome do Cliente] contra [Nome do Réu]. 
> 
> Certifique-se de que a narrativa dos Fatos siga a linha do tempo cronológica com precisão. A fundamentação jurídica deve se limitar às teses descritas no Dossiê e os pedidos devem bater de forma exata com os requerimentos.
> 
> Aqui está o Dossiê do caso:
> [COLAR AQUI O DOSSIÊ COMERCIAL E TÉCNICO DE CASO DO BÔNUS 1]"*

---

## ⚡ Passo 4: Fluxo de Trabalho (Do Claude para o Google Docs)

1. **Revisão Visual:** Copie a peça gerada pelo Claude e cole no seu modelo padrão do Google Docs.
2. **Revisão Técnica:** Revise os artigos específicos de lei e valores citados para garantir que tudo bate com a legislação atualizada.
3. **Ajuste de Detalhes:** A IA faz 90% do trabalho pesado de estruturação fática e fundamentação. O advogado sênior precisa focar apenas nos 10% finais de lapidação técnica do direito.
