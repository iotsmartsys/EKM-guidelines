# EKM Guidelines

**Modelo EKM vigente:** 1.8

**Estado:** experimental e utilizável

**Garantia automatizada:** planejada, ainda não definida

Gestão do Conhecimento de Engenharia (*Engineering Knowledge Management* —
EKM) é um modelo de governança da engenharia
assistida por IA para acelerar entregas com qualidade e previsibilidade,
coordenando pessoas, agentes, conhecimento e automações em processos
verificáveis e continuamente evolutivos.

A preservação do conhecimento é uma infraestrutura essencial: permite que execução, manutenção e auditoria operem sobre intenção explícita, em vez de depender de conversas, memória ou inferências. Ela sustenta o objetivo principal, mas não o define isoladamente.

A EKM nasceu de experimentos em projetos reais. Ela não é apresentada como um método concluído ou universal: este repositório reúne o melhor modelo conhecido até agora, os artefatos necessários para adotá-lo e as evidências que explicam sua evolução.

## Objetivo

O principal objetivo da EKM é ampliar a capacidade de uma equipe transformar intenção em software validado, reduzindo o tempo entre especificação e entrega sem perder controle técnico. Para isso, busca:

- governar decisões, responsabilidades, evidências e transições;
- aumentar a confiança na entrega;
- acelerar implementação, validação e evolução;
- aumentar qualidade, consistência e previsibilidade das entregas;
- estabelecer mecanismos e evidências auditáveis para processos, contratos, arquitetura e padrões;
- tornar o trabalho repetível entre pessoas, agentes, sessões e projetos;
- permitir automação progressiva das atividades e controles de engenharia;
- reduzir retrabalho, ambiguidades, perda de contexto e decisões improvisadas;
- evoluir continuamente os próprios mecanismos de especificação, execução, auditoria e integração.

Para viabilizar essa aceleração com segurança, funcionalidades, contratos, decisões e critérios de aceite não podem existir apenas no código, em conversas, relatórios ou memória individual. A EKM organiza esse conhecimento como parte do sistema de engenharia.

A **reconstruibilidade funcional** é uma das capacidades resultantes: uma equipe competente deve conseguir recuperar e reconstruir comportamento equivalente a partir das fontes normativas e evidências, sem depender da implementação existente como única explicação.

## Motivação estratégica

A engenharia de software está se tornando mais orientada a processos nos quais agentes de IA participam continuamente da análise, implementação, manutenção e validação. Para que essa adoção produza valor sustentável, não basta gerar código mais rápido: a IA precisa receber intenção explícita, trabalhar dentro de limites verificáveis e devolver evidências que possam ser auditadas.

A EKM prepara repositórios e processos para esse cenário por meio de fontes de verdade localizáveis, especificações implementáveis, execução rastreável e validações reproduzíveis. Qualidade, aceleração e previsibilidade são resultados pretendidos e hipóteses em validação, não garantias universais. Seu valor deve ser demonstrado por resultados mensuráveis.

## Propósito operacional

A EKM organiza responsabilidades diferentes, sem procurar um único documento que contenha toda a verdade:

```text
Especificação → o que o sistema deve fazer
Diretriz      → como mudanças e conhecimento devem ser tratados
Mapa          → onde está cada fonte de verdade e cada lacuna
Changelog     → como o conhecimento e as entregas evoluíram
Código/testes → implementação e evidência executável
Relatório     → evidência de uma execução; não cria requisitos
```

O método procura aumentar autonomia e produtividade sem transferir ao executor
decisões de produto ou arquitetura que não estejam aprovadas. A autonomia é
governada: participação humana em decisões, aprovações e validações é esperada.
O método busca reduzir retrabalho e coordenação operacional, não extinguir a
interação humana.

## Papel esperado da IA

A EKM foi concebida para permitir que a IA participe de diferentes responsabilidades da engenharia:

- **executora:** implementar especificações aprovadas, produzir código, testes e artefatos;
- **mantenedora:** evoluir o sistema preservando contratos, compatibilidade e conhecimento vigente;
- **analista:** verificar implementabilidade antes do código e identificar decisões ausentes;
- **auditora:** confrontar especificação, implementação, validações e estado de
  referência;
- **garantidora de controles verificáveis:** aplicar regras e padrões automatizáveis e produzir evidências sobre arquitetura, boas práticas e processos.

“Garantidora” não significa que a resposta de um modelo seja prova suficiente. Garantia exige a combinação de fontes normativas, testes, rastreabilidade, revisão humana e controles automatizados. Enquanto o `EKM Gate` não existir, a conformidade depende de verificação explícita; mesmo depois dele, decisões semânticas e responsabilidade permanecem humanas.

## Fluxo vigente no modelo 1.8

```text
Confecção da especificação
    ↓
parecer humano sobre a intenção
    ├─ Revisão necessária [`Revision Required`] → corrigir a especificação
    └─ Intenção aceita [`Accepted`]
    ↓
Revisão de implementabilidade integral
    ├─ Precisa de esclarecimento [`Needs Clarification`] → corrigir, emitir novo parecer e revisar novamente
    └─ Implementável [`Implementable`]
            ↓
      aprovação humana explícita
            ↓
      reconfirmação do estado de referência
            ↓
      implementação atômica
            ↓
      validação e reconciliação EKM
            ↓
      integração à referência de produção
```

O parecer humano da especificação confirma intenção, não implementabilidade. A
EKM não prevê automação da autoria como parte do método: ela governa o artefato
resultante, independentemente da modalidade usada para produzi-lo.

Revisão e implementação acontecem em execuções separadas. Implementável
[`Implementable`]
significa pronto para decisão humana, não autorização automática. Uma lacuna
relevante bloqueia toda a implementação, mas a revisão deve continuar até
classificar cumulativamente todos os requisitos e dimensões obrigatórias.

Versões normativas concluídas [`Done`] são imutáveis. Evoluções posteriores
usam novas especificações relacionadas pelos identificadores `Amends`,
`Supersedes`, `Corrects` ou `Retires`, definidos no vocabulário controlado.

## Estado atual

### O que já está definido e utilizável

- estrutura mínima de fontes normativas;
- especificações incrementais como unidade de comportamento e delegação;
- estados normativo, de implementação e de entrega independentes;
- português do Brasil como idioma normativo e vocabulário controlado com
  identificadores legados explícitos;
- transações `EKM-CHG` e lacunas `EKM-GAP`;
- estado de referência baseado na árvore de trabalho real, não somente em
  `HEAD`;
- proteção contra remoção silenciosa de conhecimento normativo;
- parecer humano da especificação anterior à análise técnica;
- revisão de implementabilidade integral e implementação atômica;
- aprovação humana e reconfirmação antes da implementação;
- adoção incremental em projetos legados por inventário, risco e *specification on touch*;
- modelos para adoção, especificação e auditoria somente leitura.

### O que os experimentos indicaram

- especificações claras reduzem expansão de escopo e retrabalho;
- construção e testes não comprovam preservação da intenção;
- validação em hardware continua indispensável quando faz parte do contrato;
- relatórios de execução podem omitir mudanças semânticas relevantes;
- comparar apenas com o último commit pode ocultar perda de trabalho preexistente;
- agentes podem implementar soluções tecnicamente coerentes, porém não autorizadas, quando a especificação permite inferência;
- instruções operacionais explícitas melhoram bastante a consistência entre modelos diferentes;
- modelos e agentes ainda variam na leitura, classificação e observância das fontes EKM.

Esses resultados sustentam a utilidade da abordagem, mas ainda não demonstram aplicabilidade universal nem conformidade independente do executor.

### O que permanece em aberto

- métricas sistemáticas de produtividade, retrabalho, custo de contexto e manutenção;
- validação em mais tecnologias, equipes e ciclos de vida;
- evolução compatível dos identificadores legados de estados e resultados;
- coordenação entre múltiplos agentes e separação assistida de responsabilidades;
- autenticação e verificação automatizada de pareceres humanos;
- custo sustentável de adoção e evolução em projetos de diferentes portes.

## Planos futuros

### Ponto de controle EKM (`EKM Gate`)

Está previsto um mecanismo automatizado para proteger a integração à produção. Ele poderá verificar aspectos comprováveis, como:

- estrutura e metadados obrigatórios;
- relações e estados das especificações;
- evidência de Technical Readiness e aprovação;
- imutabilidade de versões em produção;
- transações e lacunas abertas;
- rastreabilidade entre requisitos, mudanças e validações;
- reconciliação antes do merge.

O ponto de controle EKM permanece **planejado e não definido**
[`Planned / Not Defined`]. Ainda não existem arquitetura, esquema, ferramenta
ou política de bloqueio aprovados. Mesmo no futuro, automação não substituirá
julgamento humano sobre intenção e relações de ganhos e perdas.

### Evolução experimental

Os próximos ciclos devem priorizar:

1. ampliar auditorias e implementações comparativas entre agentes, modelos e contextos;
2. transformar divergências observadas em regras somente quando houver evidência;
3. ampliar os estudos de caso sem tornar o método específico de uma tecnologia;
4. definir métricas leves e úteis;
5. especificar e experimentar o EKM Gate antes de recomendar sua adoção.

## Conteúdo do repositório

- [`docs/EKM-CONCEPT.md`](docs/EKM-CONCEPT.md): definição, problema, limites e hipóteses.
- [`docs/EKM-METHOD.md`](docs/EKM-METHOD.md): método de referência vigente.
- [`docs/DESIGN-DECISIONS.md`](docs/DESIGN-DECISIONS.md): razões das principais escolhas.
- [`docs/LEGACY-ADOPTION.md`](docs/LEGACY-ADOPTION.md): adoção incremental em projetos existentes.
- [`docs/EXPERIMENT-HISTORY.md`](docs/EXPERIMENT-HISTORY.md): evolução produzida pelos experimentos.
- [`docs/experiments/`](docs/experiments/): protocolos e registros de execuções experimentais não normativos ainda em avaliação.
- [`docs/case-studies/`](docs/case-studies/): evidências e limitações dos casos reais.
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md): regras para evolução da própria EKM.
- [`templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md`](templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md): instrução inicial para adoção em legado.
- [`templates/EKM-READONLY-AUDIT-PROMPT.md`](templates/EKM-READONLY-AUDIT-PROMPT.md): prompt experimental para o Validador de Integridade da EKM.
- [`templates/`](templates/): conjunto mínimo adaptável para um projeto.

## Rotas de leitura

### Compreender ou discutir a EKM

```text
EKM-CONCEPT
→ DESIGN-DECISIONS
→ EXPERIMENT-HISTORY e case studies
→ EKM-METHOD
```

### Adotar em um projeto legado

```text
LEGACY-ADOPTION
→ EKM-LEGACY-ADOPTION-INSTRUCTIONS
→ templates
```

### Evoluir o método

```text
GOVERNANCE
→ DESIGN-DECISIONS
→ experimento e evidência
→ atualização consistente do método e dos templates
```

## Estrutura mínima no projeto adotante

```text
AGENTS.md
docs/
├── rfc/
│   ├── EKM-GUIDELINES.md
│   ├── KNOWLEDGE-MAP.md
│   └── EKM-CHANGELOG.md
└── specs/
    ├── SYSTEM-DOSSIER.md
    └── <especificações incrementais>.md
```

Essa estrutura é um ponto de partida. Novos documentos só devem existir quando possuírem autoridade, escopo ou ciclo de vida próprios.

## Início rápido em um legado

1. Leia [`LEGACY-ADOPTION.md`](docs/LEGACY-ADOPTION.md).
2. Forneça ao executor [`EKM-LEGACY-ADOPTION-INSTRUCTIONS.md`](templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md).
3. Informe caminho, escopo, referência de produção e restrições.
4. Autorize inicialmente apenas levantamento e fundação documental.
5. Responda às perguntas de intenção que o código não pode resolver.
6. Revise e aprove as fontes antes de classificá-las como vigentes.

Exemplo:

```text
Adote a EKM neste repositório seguindo EKM-LEGACY-ADOPTION-INSTRUCTIONS.md.
Nesta etapa, não altere código, build, testes ou automações. Registre o estado
de referência,
mapeie o sistema, produza os ativos mínimos e transforme incertezas em lacunas.
```

## Limites

A EKM não é:

- documentação de cada linha de código;
- substituição de Git, testes, RFCs ou ADRs;
- promessa de autonomia total;
- autorização para transformar código legado em requisito por inferência;
- garantia automática de conformidade;
- processo concluído ou aplicável sem adaptação a qualquer organização.

O agente pode descobrir fatos verificáveis. Intenção, compatibilidade, prioridade
e relações de ganhos e perdas continuam sob responsabilidade humana quando não
houver autoridade normativa inequívoca.

## Licença

Este projeto é distribuído sob a [GNU General Public License v3.0](LICENSE).
