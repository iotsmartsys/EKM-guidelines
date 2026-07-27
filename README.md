# EKM Guidelines

**Modelo EKM vigente:** 1.10

**Estado:** experimental e utilizável

Gestão do Conhecimento de Engenharia (*Engineering Knowledge Management* —
EKM) é um modelo de engenharia assistida por IA para transformar intenção em
software validado, mantendo autoridade humana, conhecimento atual e evidências
suficientes para verificar a entrega.

A EKM deve começar pequena. Governança é útil quando acelera decisões, reduz
retrabalho ou aumenta confiança; não quando apenas multiplica documentos e
passagens operacionais.

## Princípios da versão 1.10

- O Arquiteto humano sempre tem autoridade final sobre decisões dos agentes.
- Cada tarefa nasce de uma ordem do Arquiteto, por prompt ou pipeline.
- O estado da especificação informa se a próxima etapa está pronta.
- Git mantém a linhagem técnica; documentos não repetem SHAs e commits.
- O fluxo começa em uma branch de trabalho derivada da `main`.
- Toda tarefa começa com árvore limpa e termina com commit, push e árvore limpa.
- Revisão e evidência são proporcionais ao risco e ao recorte.
- Decisões, lacunas e conhecimento afetado continuam registrados.
- O fluxo atual não incorpora controles para problemas ainda não adotados.

## Fluxo vigente

```text
especificar
    ↓ ordem do Arquiteto
analisar implementabilidade
    ├─ Precisa de esclarecimento → corrigir a especificação
    └─ Implementável
          ↓ ordem do Arquiteto
       implementar e validar
          ↓ revisão proporcional, quando solicitada
       decisão humana e integração
```

O pipeline representa a ordem lógica das etapas. A EKM 1.10 não define
orquestração, concorrência, locks ou filas, e esses temas não influenciam os
experimentos atuais.

## Responsabilidades das fontes

```text
Especificação → comportamento, limites e aceite
Diretriz      → regras de trabalho e preservação
Mapa          → localização das fontes e lacunas
Changelog     → decisões, lacunas, evidências e resultado
Código/testes → implementação e evidência executável
Git           → commits, autoria, diferenças e linhagem
Relatório     → evidência de uma execução; não cria requisitos
```

## Estrutura inicial recomendada

```text
AGENTS.md
docs/
├── rfc/
│   ├── KNOWLEDGE-MAP.md
│   └── EKM-CHANGELOG.md
└── specs/
    └── SYSTEM-DOSSIER.md
```

Uma diretriz local só é necessária quando não existe referência externa
aplicável ou o projeto possui regras próprias. Especificações são criadas para
decisões confirmadas e funcionalidades tocadas.

## Conteúdo

- [`docs/EKM-CONCEPT.md`](docs/EKM-CONCEPT.md): conceito, problema e limites.
- [`docs/EKM-METHOD.md`](docs/EKM-METHOD.md): método de referência 1.10.
- [`docs/DESIGN-DECISIONS.md`](docs/DESIGN-DECISIONS.md): razões e evolução das decisões.
- [`docs/LEGACY-ADOPTION.md`](docs/LEGACY-ADOPTION.md): adoção incremental.
- [`docs/EXPERIMENT-HISTORY.md`](docs/EXPERIMENT-HISTORY.md): aprendizados dos experimentos.
- [`docs/experiments/COORDINATED-ACTOR-MODEL.md`](docs/experiments/COORDINATED-ACTOR-MODEL.md):
  protocolo experimental 0.8.
- [`docs/experiments/SELF-CONTAINED-IMPLEMENTER-RUN-001.md`](docs/experiments/SELF-CONTAINED-IMPLEMENTER-RUN-001.md):
  execução sequencial com prompt autocontido, Kimi K2.7 Code e Codex.
- [`docs/case-studies/`](docs/case-studies/): evidências históricas, não regras universais.
- [`docs/case-studies/IOTSMARTHOME-MULTI-AGENT-OBSERVATION.md`](docs/case-studies/IOTSMARTHOME-MULTI-AGENT-OBSERVATION.md):
  resultado funcional e conformidade entre agentes no aplicativo Swift.
- [`docs/case-studies/IOTSMARTSYSCORE-GARAGE-CONTROL-SEQUENTIAL-AGENTS.md`](docs/case-studies/IOTSMARTSYSCORE-GARAGE-CONTROL-SEQUENTIAL-AGENTS.md):
  controle de garagem validado após execução sequencial heterogênea.
- [`templates/prompts/ENGENHEIRO-IMPLEMENTADOR.md`](templates/prompts/ENGENHEIRO-IMPLEMENTADOR.md):
  modelo experimental de instrução autocontida para implementação.
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md): como evoluir a EKM.
- [`templates/`](templates/): ativos reutilizáveis.

## Adoção rápida

1. O Arquiteto delimita repositório, escopo e restrições.
2. O agente confirma que está em uma branch derivada da `main` e com a árvore
   limpa.
3. O agente aplica
   [`EKM-LEGACY-ADOPTION-INSTRUCTIONS.md`](templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md).
4. São criados apenas os ativos úteis ao próximo experimento.
5. O agente valida, cria commit, realiza push e termina com árvore limpa.

## Limite

A EKM não substitui testes, revisão, observabilidade ou julgamento humano.
Qualidade e aceleração são hipóteses que devem ser demonstradas em casos reais.
O método evolui quando a evidência mostra utilidade e também quando mostra
burocracia sem retorno.
