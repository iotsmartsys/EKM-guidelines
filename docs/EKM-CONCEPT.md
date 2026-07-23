# O que é a EKM

## Definição

Engineering Knowledge Management (EKM) é uma abordagem para manter alinhados o comportamento desejado, as decisões de engenharia, a implementação e suas evidências.

Seu objetivo é tornar o conhecimento do sistema localizável, auditável e reutilizável por pessoas e agentes de IA.

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

O agente pode localizar fatos, comparar fontes, implementar especificações e produzir evidências. O responsável humano continua decidindo intenção, prioridade, compatibilidade e trade-offs quando as fontes não forem inequívocas.

O ganho esperado é deslocar o esforço humano do trabalho repetitivo para decisões de maior impacto.

## Hipóteses atuais

A EKM parte de hipóteses ainda em validação:

1. especificações autocontidas aumentam a autonomia segura do executor;
2. fontes normativas reduzem perda de conhecimento e regressões silenciosas;
3. transações e lacunas melhoram a auditabilidade;
4. adoção incremental é mais sustentável que documentação exaustiva;
5. melhor contexto deve se converter em produtividade mensurável.
6. análise técnica anterior à implementação reduz inferências, interrupções e retrabalho durante a execução.
7. imutabilidade de versões em produção preserva a linhagem entre intenção e entrega.
8. garantias automatizadas podem aumentar conformidade em aspectos verificáveis sem substituir decisão humana.

Os experimentos atuais sustentam essas hipóteses parcialmente, mas não demonstram aplicabilidade universal.

## Estado do método

A EKM está em evolução. O modelo atual é utilizável para novos experimentos e adoção inicial, mas deve mudar quando evidências mostrarem lacunas, excesso de custo ou regras inadequadas.
