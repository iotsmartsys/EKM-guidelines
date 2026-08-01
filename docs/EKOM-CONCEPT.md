# O que é o EKOM

## Definição

Engineering Knowledge Orchestration Model (EKOM) é um framework de
orquestração *specification-first* no qual o conhecimento de engenharia atua
como plano de controle da engenharia de software, coordenando humanos, agentes
de IA, automações, implementação, validação, evidências e evolução a partir de
uma única fonte da verdade.

> **Specifications orchestrate. Code implements.**

A especificação é a autoridade normativa do comportamento pretendido e o
principal objeto do pipeline. Seu objetivo é acelerar entregas confiáveis,
preservando autoridade humana, responsabilidades delimitadas e conhecimento
localizável, auditável e reutilizável.

O EKOM sucede o Engineering Knowledge Model (EKM) 1.x. A formulação anterior
organizou o conhecimento e estabeleceu as bases do método; a versão 2.0 torna
explícita a função de orquestração revelada por sua evolução. O histórico e os
experimentos EKM permanecem válidos no contexto em que foram realizados.

## Problema tratado

Projetos frequentemente preservam o código, mas perdem:

- por que uma funcionalidade existe;
- quais contratos não podem mudar;
- se uma limitação é intencional;
- quais decisões foram substituídas;
- quem ou o que pode promover a próxima etapa;
- como comprovar que o comportamento continua correto.

Git recupera versões de arquivos, mas não garante a recuperação da intenção.
Conversas, prompts, pipelines e relatórios ajudam, porém não são fontes
normativas estáveis. Código mostra o que existe; não decide sozinho o que deve
existir.

## Especificação como plano de controle

A especificação governa o ciclo ao declarar:

- comportamento, escopo, limites e critérios de aceite;
- decisões confirmadas e lacunas ainda abertas;
- atores e recortes autorizados;
- estados atuais e condições para transição;
- relações com outras especificações e fontes derivadas;
- evidências necessárias para implementação, validação e integração;
- como uma mudança futura emenda, substitui ou retira o contrato.

Ordens humanas, prompts e automações acionam etapas. Código e testes implementam
e comprovam o contrato. Evidências sustentam as promoções de estado. Nenhuma
dessas fontes cria silenciosamente um requisito concorrente.

## Uma única verdade, várias fontes responsáveis

"Fonte única da verdade" não significa armazenar todo o conhecimento em um
documento monolítico. Significa que cada comportamento possui uma especificação
normativa identificável. Os demais ativos têm responsabilidades derivadas ou
complementares:

| Ativo | Responsabilidade |
|---|---|
| Especificação | O que deve ser verdade, quem pode avançar e como verificar? |
| RFC ou ADR | Por que uma decisão foi tomada e qual especificação afeta? |
| Diretriz | Como o método e o conhecimento devem ser tratados? |
| Mapa | Onde estão a especificação, suas fontes derivadas e lacunas? |
| Changelog EKOM | Como o conhecimento e o resultado da mudança evoluíram? |
| Código e testes | Como o contrato está implementado e comprovado? |
| Git | Qual é a linhagem técnica da alteração? |
| Relatório | O que ocorreu nesta execução, sem criar requisito? |

Especificações podem se relacionar e se coordenar sem copiar contratos. Para
cada responsabilidade normativa, a autoridade continua inequívoca.

## Reconstruibilidade

O objetivo mais forte do EKOM é permitir que uma equipe competente reconstrua
uma implementação funcionalmente equivalente usando as especificações e fontes
relacionadas, sem depender do código atual como única explicação.

Isso inclui recuperar comportamentos, contratos, limites, decisões, falhas
esperadas e critérios de aceite. Não significa reproduzir a mesma estrutura
interna ou o mesmo binário.

Critérios de aceite devem permitir uma asserção objetiva do resultado. Um
executor precisa distinguir sucesso, falha e ausência de evidência a partir do
cenário, do resultado observável e do meio de validação, sem criar o oráculo
durante a implementação.

## Relação entre humanos, agentes e automações

Todos trabalham sobre a mesma especificação, mas não possuem a mesma
autoridade. Agentes podem localizar fatos, comparar fontes, apoiar a autoria,
implementar contratos aprovados e produzir evidências. Automações podem
executar validações e gates derivados. O Arquiteto humano continua decidindo
intenção, prioridade, arquitetura, risco aceito, autorização, aprovação e
integração.

Quando houver conflito entre recomendação de agente e decisão do Arquiteto,
prevalece o Arquiteto. Quando houver conflito entre implementação e
especificação vigente, a divergência é explícita: corrige-se a implementação ou
evolui-se a especificação mediante decisão autorizada. Autoridade humana não
converte evidência falha em aprovação técnica inexistente.

O EKOM busca autonomia governada, não autonomia máxima. Interação humana em
decisões e aprovações é parte do funcionamento esperado.

## Modelo de atores

O EKOM organiza a execução por quatro atores oficiais:

| Ator | Responsabilidade perante a especificação |
|---|---|
| Autor da Especificação | transformar intenção confirmada em solução proposta e contrato verificável |
| Engenheiro Analista | determinar implementabilidade sem inventar decisões |
| Engenheiro Implementador | implementar, validar e registrar o estado sustentado |
| Engenheiro Revisor | confrontar contrato, implementação e evidências e registrar decisões humanas recebidas |

Uma ordem funcional curta identifica papel e especificação. O perfil e o estado
vigente determinam o resultado canônico; um foco adicional é opcional e não
reduz a versão normativa integral. O `AGENTS.md` encaminha o agente para regras
comuns e exatamente um perfil. Cada ator encerra a etapa atualizando o
conhecimento afetado e promovendo somente os estados sustentados por sua
atuação sobre a especificação inteira.

Não existe um ator dedicado a comandar os demais. A especificação orquestra as
passagens; o Arquiteto mantém a autoridade. Validação, aprovação e integração
continuam decisões humanas, registradas pelo Revisor quando fornecidas.

O Consultor de Arquitetura é um papel institucional de apoio transversal. Ele
não integra a sequência dos quatro atores, não recebe autoridade humana e não
transforma participação em independência.

## O que o EKOM não é

- documentação de cada linha de código;
- geração indiscriminada de arquivos Markdown;
- substituição de Git, testes, RFCs, ADRs, observabilidade ou julgamento humano;
- autorização para agentes decidirem requisitos;
- motor universal de workflow, fila ou escalonador;
- promessa de autonomia ou automação total;
- processo rígido ou completo.

## Hipóteses e evidências

O EKOM preserva as hipóteses verificadas e ainda abertas da EKM 1.x: que
especificações autocontidas aumentam autonomia segura; fontes normativas reduzem
perda de conhecimento; análise anterior à implementação reduz inferências;
perfis delimitados sustentam continuidade entre agentes; coordenação por
especificações preserva objetivos multi-contexto; e critérios assertáveis
reduzem falso sucesso.

A versão 2.0 adicionou a hipótese explícita de que tratar a especificação como
plano de controle reduz divergência entre humanos, agentes, automações, código
e evidências sem introduzir uma plataforma central obrigatória. A versão 2.1
torna a versão normativa integral a unidade atômica dos resultados formais e
trata recortes recebidos como focos adicionais, salvo atuação parcial
explicitamente ordenada e sem promoção global.

Os casos de estudo sustentam decisões específicas, mas não demonstram
aplicabilidade universal nem garantem obediência de qualquer agente.

## Estado do método

O EKOM 2.1 está aprovado e vigente para adoção. A transição desde a EKM está
registrada em [`ADR-0001`](adr/ADR-0001-EKM-TO-EKOM.md). O método continua
evoluindo quando evidências mostrarem lacunas, excesso de custo ou regras
inadequadas.
