# EKM — Diretrizes locais

**Classe da fonte:** Normativa

**Estado da fonte:** Vigente

**Versão do documento:** 1.6

**Versão do modelo EKM:** 1.9

**Escopo:** Todo o repositório

## 1. Autoridade

O Arquiteto humano tem autoridade final sobre intenção, prioridade, escopo,
arquitetura, risco, autorização, validação e integração. A ordem recebida por
prompt ou pipeline define a etapa autorizada.

Agentes não inventam requisitos nem expandem o recorte. Evidências factuais
permanecem factuais mesmo quando o Arquiteto aceita o risco.

## 2. Fontes

- especificações definem comportamento e aceite;
- estas diretrizes definem regras locais;
- o mapa localiza fontes e lacunas;
- o changelog registra decisões, lacunas, evidências e resultados;
- código e testes implementam e evidenciam;
- relatórios não criam requisitos.

Git registra commits, autoria, diferenças, branches e linhagem. Não duplique
esses dados manualmente nas fontes EKM.

## 3. Fluxo

```text
especificação
→ ordem do Arquiteto
→ análise de implementabilidade
→ ordem do Arquiteto
→ implementação e validação
→ decisão humana e integração
```

Implementação exige especificação Implementável [`Implementable`]. Precisa de
esclarecimento [`Needs Clarification`] retorna a decisão ao Arquiteto sem
alteração parcial da implementação.

Revisões adicionais acontecem somente quando solicitadas.

## 4. Contrato Git

Toda tarefa de agente começa com árvore limpa, produz resultado material,
termina com commit e push e deixa a árvore limpa. Push com falha significa etapa
não entregue.

A tarefa não autoriza force push, reescrita de histórico, merge, tag, release ou
deploy sem ordem específica.

## 5. Preservação

- Não remover ou enfraquecer decisão vigente silenciosamente.
- Não substituir fonte normativa por resumo incompleto.
- Não resolver conflito normativo por preferência do agente.
- Atualizar conhecimento afetado na mesma mudança.
- Registrar lacunas que precisem sobreviver à tarefa.

## 6. Transações

Mudanças usam `EKM-CHG-NNNN`; lacunas usam `EKM-GAP-NNNN`.

Uma transação registra somente objetivo, decisões, lacunas, evidências materiais
e resultado. Ela é concluída quando o resultado aceito foi integrado ou, em
trabalho documental, entregue; o conhecimento está atual; e lacunas restantes
estão explícitas.

## 7. Regras específicas do projeto

`<REFERÊNCIA DE PRODUÇÃO, VALIDAÇÕES OBRIGATÓRIAS E RESTRIÇÕES CONFIRMADAS>`
