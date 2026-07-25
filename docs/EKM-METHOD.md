# Método EKM

**Versão do documento:** 1.6

**Modelo EKM:** 1.9

**Estado:** experimental e utilizável

## 1. Objetivo

A EKM organiza intenção, execução e evidência para acelerar a entrega de
software sem transferir decisões de produto ou arquitetura aos agentes. O
método deve começar com a menor dose de governança capaz de manter:

- conhecimento vigente;
- decisões relevantes registradas;
- execução auditável;
- resultados verificáveis.

Um controle que não melhora essas quatro propriedades ou a velocidade e a
qualidade da entrega não deve ser obrigatório.

## 2. Autoridade

O Arquiteto humano é a autoridade final sobre intenção, prioridade, escopo,
arquitetura, risco aceito, autorização, validação e integração.

Decisões e recomendações de agentes são subordinadas às decisões do Arquiteto.
O agente deve apontar conflitos e consequências observáveis, mas não pode
substituir uma decisão humana nem expandir silenciosamente o escopo recebido.

A autoridade humana não altera fatos. Uma validação que falhou continua
registrada como falha; o Arquiteto pode aceitar o risco ou decidir prosseguir,
mas não converter a evidência em aprovação técnica inexistente. Quando uma
decisão humana muda o comportamento esperado, a especificação deve ser
atualizada.

## 3. Fontes de conhecimento

| Fonte | Responsabilidade |
|---|---|
| Especificação | comportamento, limites e critérios de aceite |
| Diretriz | regras locais de trabalho e preservação |
| Mapa de conhecimento | localização das fontes e lacunas |
| Changelog EKM | decisões, lacunas, evidências e resultado das mudanças |
| Dossiê | visão geral e navegação do sistema |
| Código e testes | implementação e evidência executável |
| Relatório | evidência de uma execução; não cria requisito |

Git registra autoria técnica, commits, diferenças, branches e linhagem. Esses
dados não devem ser copiados manualmente para documentos EKM, salvo quando um
dado Git for necessário para explicar uma decisão ou um desvio material.

## 4. Unidade de trabalho

Uma especificação incremental é a unidade de comportamento e delegação. Ela
deve conter apenas o necessário para executar e verificar o recorte:

- objetivo e contexto;
- escopo e fora de escopo;
- requisitos verificáveis;
- contratos, estados e falhas relevantes;
- critérios de aceite e validações;
- relações normativas e lacunas conhecidas;
- resultado da revisão de implementabilidade.

Versões concluídas da especificação são preservadas. Mudanças posteriores usam
uma nova versão relacionada por `Amends`, `Supersedes`, `Corrects` ou `Retires`.

## 5. Estados

Os estados permanecem independentes:

### 5.1 Estado normativo

- Rascunho [`Draft`]
- Proposta [`Proposed`]
- Aprovada [`Approved`]
- Vigente [`Active`]
- Substituída [`Superseded`]
- Retirada [`Withdrawn`]
- Arquivada [`Archived`]

### 5.2 Estado da implementação

- Não iniciada [`Not Started`]
- Em andamento [`In Progress`]
- Implementada [`Implemented`]
- Validada [`Validated`]
- Regredida [`Regressed`]
- Bloqueada [`Blocked`]
- Descontinuada [`Retired`]

### 5.3 Estado da entrega

- Não pronta [`Not Ready`]
- Pronta para integração [`Ready for Integration`]
- Concluída [`Done`]

### 5.4 Revisão de implementabilidade

- Pendente de revisão [`Pending Review`]
- Implementável [`Implementable`]
- Precisa de esclarecimento [`Needs Clarification`]

O estado declarado na especificação, combinado com a ordem do Arquiteto,
determina se a próxima etapa pode começar. Não é obrigatório registrar
manualmente SHA, branch de origem, checkpoint ou cadeia de commits para
autorizar a transição.

## 6. Ordem do Arquiteto

Cada tarefa de agente é iniciada por uma ação do Arquiteto, diretamente por
prompt ou por comando de pipeline. Essa ação:

- identifica a tarefa e o recorte autorizado;
- seleciona a etapa a executar;
- autoriza apenas as operações normais necessárias àquela etapa;
- não concede liberdade para ampliar requisitos ou tomar decisões reservadas
  ao Arquiteto.

Não é necessário criar um registro adicional de aprovação com nome, data, SHA
ou assinatura para repetir a ordem recebida.

Uma ordem de análise autoriza somente análise e atualização dos artefatos de
conhecimento correspondentes. Uma ordem de implementação autoriza a
implementação somente quando a especificação estiver Implementável
[`Implementable`].

## 7. Pipeline experimental

O pipeline é a ordem lógica das etapas, não uma infraestrutura de orquestração:

```text
especificar
    ↓ ordem do Arquiteto
analisar implementabilidade
    ├─ Precisa de esclarecimento → corrigir a especificação
    └─ Implementável
          ↓ ordem do Arquiteto
       implementar e validar
          ↓ revisão proporcional, quando solicitada
       decisão humana e integração
```

### 7.1 Especificar

O Autor registra comportamento, limites, decisões e critérios de aceite. Ao
terminar, deixa a especificação como Proposta [`Proposed`], Não iniciada
[`Not Started`], Não pronta [`Not Ready`] e Pendente de revisão
[`Pending Review`].

### 7.2 Analisar implementabilidade

O Analista verifica se os requisitos podem ser implementados sem decisão
normativa, de produto ou arquitetura não declarada. A análise deve cobrir o
recorte necessário para sustentar o resultado, sem exigir uma matriz universal.

Se encontrar uma lacuna bloqueante, pode encerrar a análise assim que a decisão
necessária estiver clara. Deve registrar os demais bloqueios materiais já
observados, mas não é obrigado a continuar uma inspeção sem valor para obter uma
lista exaustiva.

O resultado é:

- Implementável [`Implementable`], quando o recorte pode ser executado sem
  inferência relevante; ou
- Precisa de esclarecimento [`Needs Clarification`], quando falta uma decisão
  necessária.

O Analista não altera a implementação.

### 7.3 Implementar e validar

O Implementador segue a especificação Implementável [`Implementable`], atualiza
código, testes e conhecimento afetado e executa validações proporcionais ao
risco. Decisões ausentes interrompem a implementação e retornam ao Arquiteto;
não são preenchidas por conveniência técnica.

Resultado de build, teste, inspeção, hardware ou outra validação deve ser
registrado quando for material para comprovar ou limitar a entrega. Não se
registram comandos de leitura, arquivos temporários ou detalhes operacionais
sem efeito sobre a conclusão.

### 7.4 Revisar, decidir e integrar

Revisões adicionais, inclusive liderança técnica ou integridade EKM, são
executadas quando o Arquiteto as solicitar em razão do recorte ou do risco.
Elas não são etapas universais.

O Arquiteto avalia as evidências, aceita ou rejeita riscos e decide a integração.
A entrega fica Concluída [`Done`] quando o comportamento aceito está integrado,
as fontes de conhecimento afetadas estão atuais e não existe lacuna bloqueante
ocultada.

## 8. Contrato Git de cada tarefa

Toda tarefa de agente deve:

1. começar com a árvore de trabalho limpa;
2. produzir um resultado material e versionável;
3. criar um commit ao fim da etapa;
4. enviar o commit ao repositório remoto por push;
5. terminar com a árvore de trabalho limpa.

Uma tarefa não usa commit vazio para simular entrega. Mesmo quando não houver
mudança de código, a conclusão material da etapa deve atualizar o artefato EKM
apropriado, como a especificação, a transação ou o registro de evidência.

Falha no push significa que a etapa ainda não foi entregue para a próxima
etapa. A ordem da tarefa autoriza commit e push normais na branch indicada, mas
não autoriza force push, reescrita de histórico, merge, tag, release ou deploy
sem ordem correspondente do Arquiteto.

O próprio Git é a evidência desses atos. Não é obrigatório repetir hashes,
branch ou mensagem do commit no `EKM-CHANGELOG.md`.

## 9. Transações e lacunas

`EKM-CHG-NNNN` identifica uma mudança de conhecimento ou implementação.
`EKM-GAP-NNNN` identifica conhecimento ausente que precise sobreviver à tarefa.

Uma transação deve registrar somente:

- objetivo e especificação relacionada;
- decisões que alteram entendimento ou execução;
- lacunas relevantes;
- evidências materiais;
- estado e resultado.

Ela não deve funcionar como diário de comandos, espelho do histórico Git ou
formulário de passagem entre agentes.

Estados recomendados da transação:

- Aberta [`Open`]
- Bloqueada [`Blocked`]
- Substituída [`Superseded`]
- Fechada [`Closed`]

O fechamento ocorre quando o recorte autorizado foi entregue por commit e push,
as fontes afetadas estão atuais, as evidências materiais estão registradas e as
lacunas restantes estão explícitas. Fechar a transação não significa que a
especificação está Concluída [`Done`]; o estado da entrega informa separadamente
se houve integração. Não se exige um commit posterior apenas para copiar
metadados do Git.

## 10. Adoção em legado

A adoção começa pequena:

1. inventariar o sistema e localizar fontes existentes;
2. criar a fundação mínima;
3. registrar lacunas que afetam decisões reais;
4. especificar em profundidade somente o que for tocado;
5. aumentar controles apenas quando a experiência demonstrar valor.

Fundação recomendada:

```text
AGENTS.md
docs/
├── rfc/
│   ├── KNOWLEDGE-MAP.md
│   └── EKM-CHANGELOG.md
└── specs/
    └── SYSTEM-DOSSIER.md
```

`EKM-GUIDELINES.md` local é necessário apenas quando o projeto não referencia
uma diretriz externa aplicável ou precisa declarar regras próprias.

## 11. Limites atuais

A EKM 1.9 não define orquestração, concorrência, locks ou filas. Esses
mecanismos não fazem parte do fluxo nem dos critérios dos experimentos atuais.

O modelo também não afirma que documentação substitui código, testes,
observabilidade ou julgamento humano. Sua utilidade deve ser medida pela
capacidade de entregar e descartar hipóteses mais rapidamente, preservando
conhecimento suficiente para compreender e verificar o resultado.
