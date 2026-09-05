# Experimento — Repository Readiness RUN-001

**Modelo:** EKOM 5.0
**Estado:** Planejado — não executado

## Objetivo e hipótese

Verificar se contrato explícito reduz inferência arquitetural e se os agentes
bloqueiam implementação sem qualificação, com custo de adoção proporcional.

## Preparação

O Arquiteto seleciona repositório piloto e alteração pequena representativa,
delimita operações e responsável técnico. Instale os templates em branch de
experimento. Use avaliações separadas por cenário, preservando evidências e
aprovações reais. Os cenários negativos podem ser simulações documentais;
qualquer alteração de produto exige habilitação válida antes de executar.

## Cenários e resultados esperados

| Cenário | Resultado observável esperado |
|---|---|
| Contrato ausente, mesmo com análise da tarefa Ready e ordem | Not Ready; nenhuma mutação de implementação |
| Contrato sugerido pela IA, completo mas não aprovado | Not Ready; proposta não vira norma |
| Contrato aprovado com requisito mínimo ausente | Not Ready no alcance afetado; requisito e retomada identificados |
| Conditionally Ready sem escopo liberado | implementação bloqueada |
| Conditionally Ready com área A Ready e B bloqueada | tarefa apenas em A elegível; tarefa que depende de B bloqueada |
| Contrato aprovado, suficiente e avaliação válida | Ready; entrada normal ainda verifica análise da tarefa e ordem |
| Precedente legado contradiz contrato | regra explícita seguida; desvio identificado |
| Especificação conflita com contrato sem exceção aprovada | obrigação bloqueada para decisão humana |
| Exceção aprovada com regra, alcance e validade | aplicada somente dentro desses limites |
| Contrato/baseline materialmente alterado após avaliação | nova avaliação exigida no alcance afetado |
| Via curta do Consultor em repositório Not Ready | implementação bloqueada |
| Regra suficiente sem precedente existente | ausência de exemplo não induz arquitetura arbitrária nem bloqueio automático |

## Evidências e aceite

Para cada cenário, registre entradas, versões, decisão humana quando existir,
estado esperado e observado, delta antes/depois, bloqueio ou regra aplicada e
limitações. Nos negativos, confirme ausência de mudanças em código, testes,
configuração e build. No positivo, confronte destinos, nomes, dependências e
tratamento de erros com o contrato, além do aceite funcional e build aplicável.
Execuções de testes dependem da ordem operacional do piloto.

Registre tempo de preparação, intervenções humanas, bloqueios indevidos e
desvios detectados. Todos os bloqueios obrigatórios devem ocorrer e o cenário
positivo deve permitir implementação conforme. Divergência é falha observada,
não motivo para alterar o resultado esperado retroativamente.

Resultados irão para `docs/reports/repository-readiness-run-001/` e serão
referenciados no histórico experimental após execução. Somente o Arquiteto
decide suficiência da amostra e eventual ajuste do método. Nenhum contrato de
adotante ou resultado experimental está aprovado por este roteiro.
