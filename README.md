# EKOM Guidelines

**Modelo EKOM vigente:** 2.1

**Estado:** aprovado e vigente

Engineering Knowledge Orchestration Model (EKOM) é um framework de
orquestração *specification-first* no qual o conhecimento de engenharia atua
como plano de controle da engenharia de software. A especificação é a fonte
única da verdade para o comportamento pretendido e o principal objeto do
pipeline: ela coordena humanos, agentes de IA, automações, implementação,
validação, evidências e evolução.

> **Specifications orchestrate. Code implements.**

O EKOM sucede a formulação Engineering Knowledge Model (EKM) 1.x. O nome EKM,
os identificadores `EKM-CHG` e `EKM-GAP` e os registros de experimentos
anteriores são preservados como história e compatibilidade; eles não expressam
mais o nome oficial do modelo vigente. A decisão está registrada em
[`ADR-0001`](docs/adr/ADR-0001-EKM-TO-EKOM.md).

O EKOM deve começar pequeno. Governança é útil quando acelera decisões, reduz
retrabalho ou aumenta confiança; não quando apenas multiplica documentos e
passagens operacionais.

## Princípios da versão 2.1

- Specification First: nenhuma implementação precede um contrato suficiente.
- Single Source of Truth: a especificação governa o comportamento pretendido;
  as demais fontes a explicam, implementam, verificam ou registram sua evolução.
- Atomic Specification: a versão normativa inteira é a unidade dos resultados
  formais; foco adicional não autoriza promoção por cobertura parcial.
- Knowledge over Code: intenção e decisão não são inferidas do código quando
  existe autoridade normativa aplicável.
- Humans and AI as First-class Collaborators: ambos atuam sobre a mesma
  especificação, com responsabilidades e autoridade explícitas.
- Traceability by Design: requisitos, decisões, implementação e evidências
  permanecem conectados.
- Evidence-based Validation: conclusão depende de evidência terminal e
  proporcional ao risco.
- Continuous Knowledge Evolution: mudanças atualizam a especificação e os
  registros afetados sem reescrever a história.
- O Arquiteto humano mantém autoridade final sobre intenção, arquitetura,
  risco, aprovação e integração.
- Implementações preservam arquitetura e precedente local por padrão; desvios
  exigem decisão consciente e delimitada na especificação.
- Git mantém a linhagem técnica; documentos não repetem SHAs e commits.
- Toda tarefa começa em branch de trabalho limpa e termina com commit, push e
  árvore limpa.

Os princípios normativos completos estão em
[`docs/PRINCIPLES.md`](docs/PRINCIPLES.md).

## Pipeline orientado pela especificação

```text
                         Especificação
                    fonte única da verdade
                               │
        ┌──────────────┬───────┼────────┬──────────────┐
        │              │       │        │              │
     Humanos      Agentes IA  Automação Implementação Validação
        │              │       │        │              │
        └──────────────┴───────┼────────┴──────────────┘
                               │
                         Evidências
                               │
                    Evolução da especificação
```

A especificação determina o recorte, os estados, as passagens permitidas e os
critérios de aceite. Papel e especificação bastam para acionar o resultado
canônico da etapa; focos adicionais não reduzem a cobertura normativa. Prompts,
comandos e automações acionam etapas autorizadas;
não se tornam fontes normativas paralelas. Código e testes implementam e
demonstram o contrato. Evidências promovem estados e alimentam a próxima
evolução da especificação.

## Modelo de atores

```text
                   Especificação EKOM
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
     Humanos           Agentes IA        Automações
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
 Autor → Analista → Implementador → Revisor/Tech Lead
                           │
                  evidência e evolução
```

Os atores oficiais são Autor da Especificação, Engenheiro Analista, Engenheiro
Implementador e Engenheiro Revisor. O Consultor de Arquitetura é um papel
institucional subordinado ao Arquiteto, não um quinto ator nem autoridade
paralela. O EKOM define a orquestração lógica por especificações; mecanismos de
execução distribuída como filas, locks e escalonadores continuam opcionais e
fora do núcleo normativo.

## Responsabilidades das fontes

```text
Especificação → fonte normativa do comportamento, limites, estados e aceite
ADR/RFC       → razão de decisões; referencia a especificação afetada
Diretriz      → regras do método e de preservação
Mapa          → localização das especificações, fontes derivadas e lacunas
Changelog     → evolução, decisões, lacunas, evidências e resultado
Código/testes → implementação e evidência executável
Git           → commits, autoria, diferenças e linhagem
Relatório     → evidência de uma execução; não cria requisitos
```

"Fonte única da verdade" não significa "arquivo único". Uma especificação
pode referenciar outras especificações e decisões sem absorver seu conteúdo.
Significa que, para cada comportamento, existe uma autoridade normativa
identificável; fontes derivadas não competem com ela.

## Estrutura inicial recomendada

```text
AGENTS.md
docs/
├── rfc/
│   ├── KNOWLEDGE-MAP.md
│   └── EKOM-CHANGELOG.md
└── specs/
    └── SYSTEM-DOSSIER.md
```

Uma diretriz local só é necessária quando não existe referência externa
aplicável ou o projeto possui regras próprias. Especificações são criadas para
decisões confirmadas e funcionalidades tocadas.

## Conteúdo

- [`docs/EKOM-CONCEPT.md`](docs/EKOM-CONCEPT.md): definição, visão, problema e limites.
- [`docs/EKOM-METHOD.md`](docs/EKOM-METHOD.md): método de referência 2.1.
- [`docs/VISION.md`](docs/VISION.md): estado futuro orientado por especificações.
- [`docs/PRINCIPLES.md`](docs/PRINCIPLES.md): princípios normativos do EKOM.
- [`docs/GLOSSARY.md`](docs/GLOSSARY.md): vocabulário canônico e termos legados.
- [`docs/adr/ADR-0001-EKM-TO-EKOM.md`](docs/adr/ADR-0001-EKM-TO-EKOM.md): decisão de evolução de EKM para EKOM.
- [`docs/ACTOR-EVALUATION.md`](docs/ACTOR-EVALUATION.md): avaliação experimental dos atores.
- [`docs/DESIGN-DECISIONS.md`](docs/DESIGN-DECISIONS.md): razões e evolução das decisões.
- [`docs/LEGACY-ADOPTION.md`](docs/LEGACY-ADOPTION.md): adoção incremental.
- [`docs/EXPERIMENT-HISTORY.md`](docs/EXPERIMENT-HISTORY.md): história EKM 1.x e aprendizados.
- [`docs/case-studies/`](docs/case-studies/): evidências históricas, não regras universais.
- [`roles/`](roles/): regras comuns e perfis oficiais separados por responsabilidade.
- [`templates/AGENTS.md`](templates/AGENTS.md): roteador oficial para projetos adotantes.
- [`templates/`](templates/): ativos reutilizáveis.

## Adoção rápida

1. O Arquiteto delimita repositório, escopo e restrições.
2. O agente confirma branch de trabalho e árvore limpa.
3. O agente aplica
   [`EKOM-LEGACY-ADOPTION-INSTRUCTIONS.md`](templates/EKOM-LEGACY-ADOPTION-INSTRUCTIONS.md).
4. A fundação instala o roteador `AGENTS.md` e aponta para os perfis EKOM.
5. A especificação aplicável torna-se a autoridade do pipeline.
6. Cada ator promove somente estados sustentados por sua etapa e registra as
   evidências correspondentes.
7. A entrega termina com fontes reconciliadas, commit, push e árvore limpa.

## Limite

O EKOM não substitui testes, revisão, observabilidade, infraestrutura de CI/CD
ou julgamento humano. Orquestração é a coordenação normativa do trabalho pela
especificação, não uma alegação de automação total. Qualidade e aceleração
continuam hipóteses a demonstrar em casos reais.
