# EKOM — Diretrizes locais

**Classe da fonte:** Normativa

**Estado da fonte:** Vigente

**Versão do documento:** 2.1

**Versão do modelo EKOM:** 2.1

**Escopo:** Todo o repositório

## 1. Autoridade

O Arquiteto humano tem autoridade final sobre intenção, prioridade, escopo,
arquitetura, risco, autorização, validação e integração. No ciclo funcional, a
ordem recebida por prompt, automação ou pipeline identifica papel e
especificação. O resultado canônico vem do perfil e eventual foco adicional não
reduz a versão normativa integral nem cria autoridade normativa paralela.

Agentes não inventam requisitos nem expandem o escopo normativo. Evidências
factuais permanecem factuais mesmo quando o Arquiteto aceita o risco.

## 2. Fontes

- a especificação é a fonte única da verdade para comportamento, estados e
  aceite e o principal objeto do pipeline;
- estas diretrizes definem regras locais;
- o mapa localiza fontes e lacunas;
- o changelog registra decisões, lacunas, evidências e resultados;
- código e testes implementam e evidenciam;
- relatórios não criam requisitos.

Git registra commits, autoria, diferenças, branches e linhagem. Não duplique
esses dados manualmente nas fontes EKOM.

> **Specifications orchestrate. Code implements.**

## 3. Fluxo

```text
Autor da Especificação
→ Engenheiro Analista
→ Engenheiro Implementador
→ Engenheiro Revisor / Tech Lead
→ decisão humana e integração
```

A especificação orquestra as passagens e recebe os estados e evidências
produzidos em cada etapa.

Cada versão normativa é a unidade atômica dos resultados formais. Autor,
Analista, Implementador e Revisor cobrem integralmente a especificação para
promover seus estados. Um foco adicional orienta atenção, não exclui obrigações;
trabalho parcial explicitamente ordenado não promove estado global.

Implementação exige especificação Implementável [`Implementable`]. Precisa de
esclarecimento [`Needs Clarification`] retorna a decisão ao Arquiteto sem
alteração parcial da implementação.

Critérios obrigatórios devem permitir asserção objetiva de cenário, resultado
observável e evidência. Compilação não substitui execução; critério falho, não
executado ou não verificável impede `Implemented`.

Cada ator atualiza a especificação, promove os estados sustentados pela própria
etapa e entrega o resultado por commit e push. Não existe um ator separado
apenas para reconciliação.

O `AGENTS.md` seleciona as regras comuns e exatamente um perfil oficial do EKOM.
O agente não carrega perfis de outros papéis nem a metodologia completa, salvo
ordem explícita de governança.

O Consultor de Arquitetura atua fora do pipeline, subordinado ao Arquiteto,
somente no recorte e nas operações autorizadas. Antes do commit final, registra
ordem, decisões, resultado e limitações e obtém confirmação explícita do
Arquiteto. Participação anterior impede alegação posterior de independência no
mesmo recorte.

## 4. Contrato Git

Todo fluxo começa em uma branch de trabalho derivada da `main`, nunca
diretamente na `main`. Toda tarefa de agente começa com árvore limpa, produz
resultado material, termina com commit e push e deixa a árvore limpa. Push com
falha significa etapa não entregue.

Antes de promover estado, declarar validação aprovada, criar o commit final,
realizar push ou emitir resposta conclusiva, o agente confirma que toda tarefa,
comando, processo, build, teste, upload ou execução delegada que iniciou chegou
a estado terminal e registra seu resultado ou limitação. Estado não terminal ou
desconhecido bloqueia o encerramento.

A tarefa não autoriza force push, reescrita de histórico, merge, tag, release ou
deploy sem ordem específica.

## 5. Preservação

- Não remover ou enfraquecer decisão vigente silenciosamente.
- Não substituir fonte normativa por resumo incompleto.
- Não resolver conflito normativo por preferência do agente.
- Preservar arquitetura, organização e separação de responsabilidades e usar o
  precedente equivalente mais próximo.
- Não criar camada, pasta estrutural, abstração transversal ou padrão
  arquitetural sem especificação Implementável que identifique o padrão atual,
  a mudança, o alcance e a justificativa ou decisão do Arquiteto.
- Na ausência ou conflito de precedentes, devolver a decisão ao Arquiteto.
- Atualizar conhecimento afetado na mesma mudança.
- Registrar lacunas que precisem sobreviver à tarefa.

## 6. Transações

Novas adoções usam `EKOM-CHG-NNNN` e `EKOM-GAP-NNNN`. Projetos migrados podem
manter `EKM-CHG-NNNN` e `EKM-GAP-NNNN`; o namespace escolhido é declarado no
mapa e não muda identificadores existentes.

Uma transação registra somente objetivo, decisões, lacunas, evidências materiais
e resultado. Ela é concluída quando o resultado aceito foi integrado ou, em
trabalho documental, entregue; o conhecimento está atual; e lacunas restantes
estão explícitas.

## 7. Regras específicas do projeto

`<REFERÊNCIA DE PRODUÇÃO, VALIDAÇÕES OBRIGATÓRIAS E RESTRIÇÕES CONFIRMADAS>`
