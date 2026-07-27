# Instruções para agentes

## Autoridade

O Arquiteto humano tem autoridade final sobre intenção, prioridade, escopo,
arquitetura, risco, autorização, validação e integração. A ordem recebida por
prompt ou pipeline define a etapa e o recorte autorizado.

Não invente requisitos, não amplie o escopo e não converta evidência falha em
evidência aprovada. Quando faltar uma decisão, devolva-a ao Arquiteto.

## Antes de começar

1. Confirme que a branch atual deriva da `main` e não é a própria `main`. Se
   não derivar, pare e informe.
2. Confirme que a árvore de trabalho está limpa. Se não estiver, pare e informe.
3. Leia esta instrução, a especificação aplicável e a transação relacionada.
4. Confirme que o estado da especificação permite a etapa solicitada.

Não é necessário registrar SHA, branch de origem, checkpoint ou declaração de
prontidão em documentos EKM.

## Etapas

- **Autoria:** produz especificação Proposta [`Proposed`] e Pendente de revisão
  [`Pending Review`].
- **Análise:** não altera implementação; produz Implementável
  [`Implementable`] ou Precisa de esclarecimento [`Needs Clarification`].
- **Implementação:** exige ordem do Arquiteto e especificação Implementável;
  produz código, testes, conhecimento atualizado e evidências.
- **Revisão:** ocorre somente quando solicitada; registra achados sem alterar
  fatos nem requisitos.

Execute apenas a etapa solicitada.

## Evidência

Registre decisões, lacunas, validações materiais e limitações. Não transforme o
changelog em diário de comandos e não copie para ele metadados que o Git já
mantém.

## Encerramento obrigatório

Toda tarefa deve produzir mudança material, terminar com commit e push e deixar
a árvore de trabalho limpa. Push com falha significa tarefa ainda não entregue.

A ordem normal da tarefa não autoriza force push, reescrita de histórico,
merge, tag, release ou deploy.
