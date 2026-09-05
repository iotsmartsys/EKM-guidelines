# Repository Engineering Contract e Repository Readiness

**Modelo EKOM:** 5.0

**Estado:** aprovado e vigente

## 1. Pré-requisito de adoção

A EKOM não assume implementação em repositório que não declare explicitamente
suas regras de construção. Repository Engineering Contract é a fonte normativa
local dessas regras. Repository Readiness é a avaliação de suficiência e
conformidade que habilita a adoção para implementação no escopo declarado.
Instalar os templates ou concluir a fundação documental não habilita agentes
implementadores. Levantamento, proposta de contrato, análise e documentação
podem ocorrer antes da habilitação, dentro da ordem recebida.

Esta capacidade antecede os quatro estágios do workflow; não é um quinto
estágio nem uma promoção documental da especificação. Aplica-se também à via
curta do Consultor, correções e preparações arquiteturais. Experimentos que
alterem código no repositório adotante também exigem habilitação; simulação
somente documental não implementa produto.

## 2. Conteúdo mínimo do contrato

O contrato deve declarar regras explícitas e imperativas, com alcance e meios
de verificar conformidade. Não basta recomendar boas práticas ou mandar o
Implementador descobrir a arquitetura. Deve conter:

| Área obrigatória | Conteúdo suficiente |
|---|---|
| Arquitetura | padrão adotado, módulos/camadas e seus limites e responsabilidades |
| Organização | destinos de arquivos e responsabilidade de pastas |
| Nomenclatura e estilo | convenções de nomes, formatação e estilo de código |
| Dependências | direções permitidas e proibidas, fronteiras e integrações |
| Implementação | padrões obrigatórios para interfaces, serviços, DTOs e demais elementos aplicáveis |
| Dados | persistência, acesso a dados e ownership das operações |
| Falhas e observabilidade | tratamento de erros, propagação, logging e dados que não podem ser registrados |
| Tecnologias | tecnologias e abstrações autorizadas e proibidas |
| Verificação | estratégia de testes, build canônico e critérios de conformidade |
| Precedentes oficiais | exemplos por tipo de alteração, caminho/símbolo e regra exemplificada |
| Evolução | critérios para novas abstrações, exceções e alterações arquiteturais |

Cada área precisa de conteúdo aplicável ou de `Não se aplica` com justificativa
aprovada. Ausência de exemplo em projeto novo pode ser suprida por exemplo
mínimo aprovado; código ainda não existente não deve ser inventado como
precedente real. Referências a normas locais são permitidas se inequívocas,
acessíveis e vinculadas à versão aprovada. Não se exige documentar todo o legado.
A estratégia de testes não amplia por si só o recorte ou as permissões de uma
tarefa; requisitos de teste aplicáveis devem ser incorporados à especificação.

## 3. Autoridade e precedência

A ordem de aplicação é:

```text
Especificação da tarefa
    ↓
Repository Engineering Contract aprovado
    ↓
Precedentes oficiais indicados
    ↓
Demais código existente
    ↓
Preferência do implementador
```

A especificação governa comportamento e o contrato governa construção.
A precedência resolve escolhas dentro da autoridade de cada fonte; não
permite à tarefa revogar silenciosamente uma regra arquitetural. Uma exceção
na especificação só prevalece quando o Arquiteto/responsável técnico a aprovar
explicitamente, identificando regra, motivo, alcance e duração ou condição de
encerramento. Conflito sem resolução explícita bloqueia a obrigação afetada.

As diretrizes declaradas são imperativas. Precedentes exemplificam e
complementam; não substituem nem contradizem o contrato. Código legado em
conflito é desvio, não padrão a copiar. Preferência local só decide o que as
fontes superiores deixarem livre. Ausência de precedente não bloqueia se a
regra aprovada já for suficiente; lacuna normativa material bloqueia.

## 4. Proposta, aprovação e vigência

A IA pode inspecionar código e sugerir um contrato, distinguindo fatos,
inferências, desvios e decisões pendentes. O resultado começa como `Draft` ou
`Proposed`; frequência de um padrão no código não o torna norma.
Somente um Arquiteto ou responsável técnico humano designado pode aprovar o
contrato e suas revisões. Registre identidade, papel, data, versão/escopo
aprovados e referência à decisão humana. O agente pode transcrever uma decisão
explícita, mas não inventar aprovação nem aprovar sua própria proposta.
A ordem genérica de adoção ou implementação não aprova o contrato inferido.

Alteração material do contrato, de fonte normativa referenciada ou da baseline
arquitetural exige nova avaliação do alcance afetado antes de implementar.
Revisão proposta não substitui a aprovada. Se houver dúvida sobre aplicabilidade,
aprovação revogada, referência inacessível ou evidência superada, a habilitação
não pode ser presumida. Revisões anteriores e avaliações permanecem rastreáveis.
Uma edição ordinária conforme não exige reaprovação universal.

## 5. Estados do repositório

| Estado | Critério | Operação permitida |
|---|---|---|
| Not Ready | contrato ausente, não aprovado, insuficiente, avaliação ausente/inválida ou bloqueador material no alcance | levantamento, proposta, análise e documentação autorizados; implementação bloqueada |
| Conditionally Ready | contrato aprovado e avaliação existente, com lacunas ou desvios conhecidos e alcance delimitado | implementação somente em escopos explicitamente avaliados como Ready e habilitados pelo humano; demais áreas bloqueadas |
| Ready | contrato aprovado, conteúdo mínimo suficiente e conformidade avaliada sem bloqueador material no escopo declarado | elegível à implementação, respeitadas análise da tarefa e ordem explícita |

`Conditionally Ready` não é autorização genérica para ignorar requisitos. Sem
escopo Ready explicitamente identificado, permanece bloqueada toda implementação.
Se a tarefa atravessar fronteiras, todas as áreas e dependências materiais
precisam estar cobertas. Escopo desconhecido ou parcialmente coberto bloqueia.
Débito aceito não transforma violação normativa em conformidade; exige correção
ou exceção normativa explícita antes da habilitação do recorte.

Esses estados pertencem ao repositório. O `Ready` da análise de implementabilidade
continua pertencendo à versão de uma especificação. Nenhum substitui o outro;
`Conditionally Ready` continua proibido como resultado final da análise da tarefa.

## 6. Avaliação e guarda operacional

1. Identificar repositório, escopo, contrato e revisão aplicável.
2. Verificar aprovação humana rastreável e conteúdo mínimo por área.
3. Confrontar regras, precedentes e baseline de forma dirigida ao alcance;
   registrar evidência, lacunas, desvios, impacto e condição de resolução.
4. Registrar uma avaliação nova em
   `docs/reports/repository-readiness/<identificador-unico>.md`.
5. O Arquiteto/responsável técnico confirma a habilitação e seu alcance.
   `docs/rfc/REPOSITORY-READINESS.md` aponta para contrato, avaliação e decisão.
6. Antes de mutação de implementação, cada executor confirma validade, cobertura
   integral do recorte e ausência de bloqueadores. Se falhar, não inicia código,
   testes, configuração ou build e informa requisito ausente e condição de retomada.

Não se repete a aprovação a cada tarefa quando a mesma decisão continua válida.
Durante a execução, nova lacuna material suspende a obrigação dependente e exige
reavaliação do alcance; trabalho independente válido pode ser preservado.
A revisão confronta tanto comportamento quanto construção e registra desvios
com referência à regra. O mapa localiza essas fontes, sem copiar seu conteúdo.

A guarda é uma obrigação dos perfis e do roteador. O validador documental é
apenas estrutural: não autentica decisão humana nem certifica conformidade
arquitetural. A EKOM não oferece neste repositório um bloqueio de CI ou controle
de acesso automatizado; eficácia da obediência pelos agentes será experimentada.

## 7. Migração e experimento

EKOM 5.0 introduz pré-requisito incompatível com habilitação implícita em 4.x.
Projetos existentes migram deliberadamente, mantendo sua história sob a versão
original. Ao adotar 5.0, sem qualificação válida são `Not Ready`; não há aprovação
retroativa automática. Fundação documental pode terminar com pendências abertas.

Use os templates de contrato, estado e avaliação e o roteiro
[Repository Readiness — experimento](experiments/REPOSITORY-READINESS-RUN-001.md).
A aprovação desta regra do método não aprova nenhum contrato de um adotante.
