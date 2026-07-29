# O que é a EKM

## Definição

Gestão do Conhecimento de Engenharia (*Engineering Knowledge Management* —
EKM) é uma abordagem de governança da
engenharia assistida por IA para manter alinhados o comportamento desejado, as
decisões de engenharia, a implementação e suas evidências.

Seu objetivo é acelerar entregas confiáveis, preservando autoridade humana,
responsabilidades delimitadas e conhecimento localizável, auditável e
reutilizável por pessoas e agentes de IA.

## Problema tratado

Projetos frequentemente preservam o código, mas perdem:

- por que uma funcionalidade existe;
- quais contratos não podem mudar;
- se uma limitação é intencional;
- quais decisões foram substituídas;
- como comprovar que o comportamento continua correto.

Git recupera versões de arquivos, mas não garante a recuperação da intenção. Conversas e relatórios ajudam, porém não são fontes normativas estáveis.

## Proposta

A EKM organiza o conhecimento em papéis distintos:

| Ativo | Pergunta respondida |
|---|---|
| Especificação | O que o sistema deve fazer? |
| RFC ou ADR | Por que esta decisão foi tomada? |
| Diretriz | Como mudanças e conhecimento devem ser tratados? |
| Mapa | Onde está a fonte de verdade? |
| Changelog EKM | Como o conhecimento evoluiu? |
| Código e testes | Como está implementado e comprovado? |
| Relatório | O que ocorreu nesta execução? |

Esses ativos cooperam; nenhum deles substitui todos os demais.

## Reconstruibilidade

O objetivo mais forte da EKM é permitir que uma equipe competente reconstrua uma implementação funcionalmente equivalente usando as fontes do repositório, sem depender do código atual como única explicação.

Isso inclui recuperar comportamentos, contratos, limites, decisões, falhas esperadas e critérios de aceite. Não significa reproduzir a mesma estrutura interna ou o mesmo binário.

## O que a EKM não é

- documentação de cada linha de código;
- geração indiscriminada de arquivos Markdown;
- substituição de Git, testes, RFCs ou ADRs;
- autorização para agentes decidirem requisitos;
- promessa de autonomia total;
- processo rígido ou completo.

## Relação entre humano e agente

O agente pode localizar fatos, comparar fontes, apoiar a especificação,
implementar contratos aprovados e produzir evidências. O responsável humano
continua decidindo intenção, prioridade, compatibilidade, relações de ganhos e
perdas, arquitetura, risco aceito, autorização e decisão final de entrega.
Quando houver conflito entre uma decisão do agente e uma decisão do Arquiteto,
prevalece o Arquiteto.

A EKM busca autonomia governada, não autonomia máxima. Interação humana em
decisões, aprovações e validações é parte do funcionamento esperado do método,
não uma falha a ser eliminada.

O ganho esperado é deslocar o esforço humano do trabalho repetitivo e da
coordenação operacional para decisões de maior impacto. Reduzir interação é
desejável quando ela representa retrabalho, ambiguidade ou operação repetitiva;
não quando ela exerce governança.

## Especificação, estado e ordem humana

A EKM não determina como a especificação é confeccionada. Seu contrato começa
no artefato resultante.

Cada tarefa de agente nasce de uma ordem do Arquiteto, por prompt ou pipeline.
Essa ordem autoriza a etapa solicitada, enquanto o estado da especificação
indica se ela está pronta para a etapa. Não é necessário repetir a ordem em um
parecer documental com metadados Git.

Git preserva autoria técnica, diferenças e linhagem. As fontes EKM preservam o
que Git não explica sozinho: intenção, decisão, lacuna, evidência material e
resultado.

## Modelo de atores

A EKM organiza a execução por quatro atores:

| Ator | Responsabilidade |
|---|---|
| Autor da Especificação | investigar o problema e transformar intenção confirmada em solução proposta e contrato verificável |
| Engenheiro Analista | determinar implementabilidade sem inventar decisões |
| Engenheiro Implementador | implementar, validar e registrar o estado sustentado |
| Engenheiro Revisor | revisar evidências e registrar decisões humanas recebidas |

Uma ordem curta identifica papel, resultado, recorte e, no ciclo funcional,
especificação. O `AGENTS.md` do projeto encaminha o agente para regras comuns e
exatamente um perfil. Cada ator encerra a própria etapa atualizando
conhecimento, promovendo estados, criando commit e realizando push.

Não existe um ator dedicado apenas a reconciliar o resultado dos demais.
Validação, aprovação e integração continuam decisões humanas; o Revisor apenas
as registra quando fornecidas explicitamente.

A EKM também possui o Consultor de Arquitetura como papel institucional de
apoio transversal. Ele pode investigar, propor e executar o recorte
explicitamente solicitado pelo Arquiteto, mas não integra a sequência dos
quatro atores, não recebe autoridade humana e não transforma participação em
independência. Sua atuação termina com registro e confirmação explícita do
Arquiteto antes do commit.

## Hipóteses e evidências

A EKM parte de hipóteses ainda em validação:

1. especificações autocontidas aumentam a autonomia segura do executor;
2. fontes normativas reduzem perda de conhecimento e regressões silenciosas;
3. transações e lacunas melhoram a auditabilidade;
4. adoção incremental é mais sustentável que documentação exaustiva;
5. melhor contexto deve se converter em produtividade mensurável.
6. análise técnica anterior à implementação reduz inferências, interrupções e retrabalho durante a execução.
7. imutabilidade de versões em produção preserva a linhagem entre intenção e entrega.
8. governança explícita aumenta confiança e velocidade sem exigir redução da
   participação humana decisória.
9. usar o estado da especificação e a ordem do Arquiteto reduz passagens
   documentais sem perder autoridade.
10. manter a linhagem no Git reduz duplicação sem perder auditabilidade.
11. perfis específicos por ator reduzem a necessidade de carregar e interpretar
    a metodologia completa em cada tarefa.
12. especificação, estados e Git permitem continuidade entre modelos e
    ambientes diferentes.
13. permitir que o Autor investigue e proponha solução, preservando análise de
    implementabilidade independente, reduz handoffs sem criar autoaprovação.
14. coordenar especificações junto a fontes de implementação independentes
    preserva objetivos arquiteturais multi-contexto sem ampliar silenciosamente
    a autoridade de uma tarefa local.
15. institucionalizar a consultoria arquitetural por IA torna a colaboração
    transversal auditável sem transferir a autoridade principal do Arquiteto.
16. preservar o precedente arquitetural local por padrão e exigir autorização
    explícita para desvios reduz reorganizações incidentais e violações de
    responsabilidade sem impedir evolução deliberada.
17. impedir conclusão com execuções próprias ainda pendentes reduz evidência
    prematura sem introduzir coordenação entre atores.

O ciclo completo no aplicativo iotsmarthome sustentou a adoção do modelo de
atores na EKM 1.11. Os experimentos não demonstram aplicabilidade universal nem
garantem obediência de qualquer agente.

## Estado do método

A EKM 1.16 está aprovada e vigente para adoção. O método continua evoluindo
quando evidências mostrarem lacunas, excesso de custo ou regras inadequadas.
