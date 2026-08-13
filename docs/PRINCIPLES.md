# Princípios do EKOM

## Specification First

A especificação antecede e governa a implementação e possui ciclo de vida
próprio. Exploração pode produzir conhecimento para especificá-la, mas não
transforma inferência em requisito vigente.

## Single Source of Truth

Para cada comportamento existe uma especificação com autoridade normativa
identificável. Fontes relacionadas explicam, implementam, verificam ou
registram a evolução; não criam contratos concorrentes.

## Normative Authority Confrontation

Antes da prontidão, toda mudança é confrontada com as autoridades normativas
dos elementos que afeta. Relações de preservação, alteração, substituição,
correção ou descontinuação permanecem explícitas; conflito ou autoridade
omitida retorna à decisão do Arquiteto.

## Functional Scope Containment

Uma especificação funcional não absorve silenciosamente uma evolução
arquitetural independente. Capacidade ausente, transversal e validável por si
própria bloqueia a funcionalidade na baseline vigente e exige decisão do
Arquiteto sobre análise arquitetural e especificação preparatória.

## Knowledge over Code

Código preserva a implementação atual, não necessariamente a intenção.
Conhecimento, decisões e evidências permanecem persistentes, rastreáveis e
evolutivos. Conflitos são resolvidos por implementação corrigida ou evolução
autorizada da especificação.

## Delegated Execution, Human Authority

Agentes podem assumir amplamente investigação, implementação, verificação e
documentação. O Arquiteto mantém julgamento, prioridade, responsabilidade e
autoridade sobre arquitetura, risco, relevância das críticas, suficiência das
evidências, aprovação, conclusão e reabertura. A IA amplia sua capacidade; não
o substitui.

## Implementability before Implementation

Toda especificação é analisada antes de implementar. A função é obrigatória; um
Engenheiro Analista separado não é. Segregação é escolhida quando risco,
incerteza ou necessidade de especialização justificarem seu custo.

## Simple Explicit Transitions

O workflow possui Autoria, Análise, Implementação e Revisão. Análise `Ready` da
versão corrente e ordem explícita do Arquiteto são condições suficientes para
iniciar implementação; não existe promoção ou autorização documental
intermediária. A ordem não substitui análise e uma análise antiga não cobre
mudança normativa posterior.

## Review and Consultative Challenge

Revisão é o quarto estágio; sua profundidade e independência são proporcionais
ao risco. Outro agente não constitui automaticamente validação independente. O
challenge informa a decisão do Arquiteto e não recebe autoridade para redefinir
aceite, concluir ou integrar.

## Evidence-based Validation

Testes automatizados, builds, inspeções, logs e execução real são evidências,
não provas absolutas. Evidência deve ser terminal, observável e proporcional ao
risco; sua suficiência é decidida pelo Arquiteto. Testes não são alterados
apenas para produzir verde nem usados como argumento autorreferente.

A especificação decide explicitamente se criar ou alterar testes integra o
recorte e os vincula a critérios de aceite. O Implementador não inventa suíte,
matriz ou cobertura. A criação autorizada não autoriza execução; validações só
são executadas sob a permissão operacional correspondente.

## Build Is Part of Implementation

Implementação autorizada de artefato construível inclui seu build canônico e
proporcional. A especificação funcional não repete essa permissão. Build falho
ou não executado não sustenta conclusão; testes, hardware e operações externas
continuam sujeitos a autorização própria.

## Material Work Ends Delivered

Toda atuação autorizada que altera materialmente o repositório inclui commit e
push da branch de trabalho corrente e termina com árvore limpa. Esses atos são
parte da entrega, não um estágio ou gate adicional. Operações que integram,
publicam, reescrevem ou removem história continuam fora dessa autorização.

## Continuous Knowledge Evolution

Novas decisões emendam ou substituem versões anteriores sem reescrever
especificações concluídas nem registros históricos. Nova necessidade, defeito
posterior ou evidência material pode justificar reabertura pelo Arquiteto.

## Experimental Learning

As hipóteses do próprio EKOM são confrontadas com experimentos reais. Papéis,
teorias e mecanismos podem ser sustentados, ajustados ou refutados; não são
dogmas.

## Governança proporcional

O EKOM usa o menor conjunto de controles capaz de preservar autoridade,
conhecimento, rastreabilidade e verificabilidade. Obrigações sem ganho
demonstrável devem ser reduzidas.

## Formulação operacional

> **Specifications orchestrate. Code implements.**
