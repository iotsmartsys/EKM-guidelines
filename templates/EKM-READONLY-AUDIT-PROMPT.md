# Prompt experimental — Auditoria EKM read-only

**Status:** Experimental

Use este prompt para comparar agentes e modelos. Ele não substitui as fontes normativas do projeto.

```text
Você está executando uma auditoria isolada em um repositório governado pela EKM.

## Isolamento obrigatório

- Use exclusivamente este prompt e os arquivos do repositório.
- Não leia nem grave memórias do agente, Copilot, IDE ou conversas anteriores.
- Não crie arquivos de memória, notas ou cache fora do repositório.
- Não instale ferramentas, pacotes ou dependências.
- Não acesse rede ou serviços externos sem autorização explícita.
- Ferramenta ausente deve ser registrada como `Blocked`, nunca instalada por iniciativa própria.

## Preparação permitida

Antes da leitura normativa, execute somente comandos Git de leitura necessários para registrar:

- raiz do repositório;
- branch;
- commit;
- estado inicial do worktree.

Depois, leia integralmente e nesta ordem:

1. AGENTS.md
2. docs/rfc/EKM-GUIDELINES.md
3. docs/rfc/KNOWLEDGE-MAP.md
4. docs/rfc/EKM-CHANGELOG.md
5. docs/specs/EXECUTABLE-HARDWARE-EXAMPLES.md

Essas fontes são obrigatórias. Não substitua a leitura por resumo, memória ou resultado anterior.

## Modo read-only

Não altere nenhum arquivo, incluindo código, configuração, teste, automação, especificação ou registro EKM. São permitidas buscas, comandos Git de leitura e validações que utilizem ferramentas já disponíveis e gerem somente artefatos ignorados previstos pelo projeto.

## Fase 1 — Technical Readiness Review

Analise integralmente requisitos, decisões, contratos, critérios de aceite, validações, relações normativas e baseline.

Resultado permitido:

- `Implementable`; ou
- `Needs Clarification`.

Conflito entre fontes, ambiguidade ou decisão ausente exige `Needs Clarification` e encerra a execução sem auditoria de conformidade. Não resolva o conflito por inferência.

## Fase 2 — Auditoria integral

Execute somente após `Implementable`.

Classifique individualmente todos os requisitos, decisões e critérios de aceite usando exatamente:

- `Compliant`;
- `Non-compliant`;
- `Not verifiable`;
- `Blocked`.

Não combine estados nem use qualificadores como “parcial” ou “estrutural”. Requisito dependente de validação não executada não pode ser declarado `Compliant` quando a evidência executável fizer parte de seu contrato.

Para cada item, informe evidência direta e justificativa. Estado anterior, changelog ou relatório não constitui prova de conformidade.

## Relatório

1. Fontes lidas e ordem real
2. Baseline
3. Technical Readiness Review
4. Matriz integral de requisitos
5. Matriz integral de decisões
6. Matriz integral de critérios de aceite
7. Validações executadas
8. Não conformidades
9. Itens `Not verifiable` ou `Blocked`
10. Estados EKM recomendados, sem aplicá-los
11. Comparação do worktree inicial e final
12. Todas as operações Git, externas e artefatos temporários

Não declare comando, leitura ou validação que não apareça na execução real.

## Tarefa

Valide a conformidade integral da implementação com docs/specs/EXECUTABLE-HARDWARE-EXAMPLES.md.
Não implemente correções e não atualize documentos EKM.
```

## Limite

Este template melhora descoberta e comparabilidade, mas não garante conformidade do executor. Resultados ainda exigem revisão enquanto o `EKM Gate` permanecer `Planned / Not Defined`.
