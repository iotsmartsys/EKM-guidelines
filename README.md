# EKM Guidelines

**Modelo EKM vigente:** 1.5

Engineering Knowledge Management (EKM) é uma abordagem para preservar o conhecimento necessário para compreender, evoluir, auditar e reconstruir um sistema de software com assistência de pessoas e agentes de IA.

O objetivo não é documentar cada linha de código. É impedir que funcionalidades, contratos, decisões e critérios de aceite existam apenas na implementação, em conversas ou na memória de uma pessoa.

## Ideia central

```text
Especificação → define o que o sistema deve fazer
Diretriz      → define como mudanças e conhecimento devem ser tratados
Mapa          → aponta onde está cada fonte de verdade
Changelog     → registra a evolução do conhecimento
Código/testes → implementam e comprovam o comportamento
Relatório     → registra evidências de uma execução
```

Antes do código, toda especificação passa por uma Technical Readiness Review. O resultado deve ser `Implementable` ou `Needs Clarification`; uma única lacuna relevante bloqueia atomicamente todo o recorte até que a própria especificação seja corrigida e reanalisada.

Versões integradas à referência de produção tornam-se imutáveis. A EKM também prevê um futuro `EKM Gate` para garantias automatizadas, mas essa capacidade permanece planejada e ainda não definida.

O código é evidência do estado atual, mas não deve ser a única fonte da intenção do sistema.

## Conteúdo deste repositório

- [`docs/EKM-CONCEPT.md`](docs/EKM-CONCEPT.md): definição, problema, limites e hipóteses atuais.
- [`docs/EKM-METHOD.md`](docs/EKM-METHOD.md): princípios e regras gerais da EKM.
- [`docs/DESIGN-DECISIONS.md`](docs/DESIGN-DECISIONS.md): razões das principais escolhas do modelo.
- [`docs/LEGACY-ADOPTION.md`](docs/LEGACY-ADOPTION.md): metodologia para adoção em projetos existentes.
- [`docs/EXPERIMENT-HISTORY.md`](docs/EXPERIMENT-HISTORY.md): resumo dos experimentos que originaram o modelo.
- [`docs/case-studies/`](docs/case-studies/): evidências e limitações dos experimentos realizados.
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md): como o próprio método deve evoluir.
- [`templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md`](templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md): instrução inicial para um agente aplicar a EKM em um legado.
- [`templates/`](templates/): arquivos mínimos para copiar ou adaptar em um projeto.

## Rotas de leitura

### Para compreender e discutir o método

```text
EKM-CONCEPT
→ DESIGN-DECISIONS
→ EXPERIMENT-HISTORY e case studies
→ EKM-METHOD
```

### Para adotar em um projeto legado

```text
LEGACY-ADOPTION
→ EKM-LEGACY-ADOPTION-INSTRUCTIONS
→ templates
```

### Para evoluir a EKM

```text
GOVERNANCE
→ DESIGN-DECISIONS
→ novos experimentos e evidências
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

Essa é uma estrutura mínima, não uma obrigação de fragmentar o conhecimento. Novos documentos são criados apenas quando possuem autoridade, ciclo de vida ou escopo próprios.

## Início rápido em um projeto legado

1. Disponibilize ao agente o conteúdo de [`EKM-LEGACY-ADOPTION-INSTRUCTIONS.md`](templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md).
2. Informe o caminho do repositório e as restrições conhecidas.
3. Autorize apenas a fase documental inicial.
4. Responda às questões que o código não consegue resolver, especialmente sobre intenção, compatibilidade e suporte vigente.
5. Revise as especificações propostas antes de classificá-las como `Active`.

Exemplo de solicitação:

```text
Adote a EKM neste repositório seguindo EKM-LEGACY-ADOPTION-INSTRUCTIONS.md.
Nesta etapa, não altere código, build, testes ou automações. Faça o levantamento,
registre lacunas e produza os ativos mínimos de conhecimento.
```

## Limites da autonomia

O agente pode descobrir e documentar fatos verificáveis, como dependências, APIs, fluxos e automações existentes. Ele não deve decidir sozinho se um comportamento observado é requisito, acidente histórico, bug ou funcionalidade obsoleta.

Quando a intenção não puder ser comprovada, a resposta correta é registrar uma lacuna e consultar o responsável humano.

## Estado do projeto

Este repositório representa a primeira consolidação pública do método, construída a partir de experimentos reais em refatoração, preservação de arquitetura, reutilização de componentes e adoção em biblioteca legada.

A EKM está em evolução: já é utilizável para novos experimentos, mas suas hipóteses, métricas e capacidade de generalização ainda precisam ser validadas.

## Licença

Este projeto é distribuído sob a [GNU General Public License v3.0](LICENSE).
