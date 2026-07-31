# EKM Guidelines

**Modelo EKM vigente:** 1.18

**Estado:** aprovado e vigente

Gestão do Conhecimento de Engenharia (*Engineering Knowledge Management* —
EKM) é um modelo de engenharia assistida por IA para transformar intenção em
software validado, mantendo autoridade humana, conhecimento atual e evidências
suficientes para verificar a entrega.

A EKM deve começar pequena. Governança é útil quando acelera decisões, reduz
retrabalho ou aumenta confiança; não quando apenas multiplica documentos e
passagens operacionais.

## Princípios da versão 1.18

- O Arquiteto humano sempre tem autoridade final sobre decisões dos agentes.
- Cada etapa de uma especificação nasce de uma ordem que identifica papel,
  especificação e recorte.
- O agente lê regras comuns, exatamente um perfil e somente as fontes
  pertinentes à sua atuação.
- Implementações preservam a arquitetura e o precedente local por padrão;
  desvios exigem determinação consciente e delimitada na especificação.
- O Autor pode investigar o problema e propor uma solução; o Analista valida
  sua implementabilidade em atuação independente.
- Critérios de aceite obrigatórios devem permitir uma asserção objetiva:
  cenário, resultado observável e evidência suficiente para distinguir
  aprovação, reprovação e ausência de execução.
- O estado da especificação informa se a próxima etapa está pronta.
- Cada ator promove e registra os estados sustentados por sua própria etapa.
- Git mantém a linhagem técnica; documentos não repetem SHAs e commits.
- O fluxo começa em uma branch de trabalho derivada da `main`.
- Toda tarefa começa com árvore limpa e termina com commit, push e árvore limpa.
- Nenhum agente conclui a etapa enquanto execução iniciada por ele permanecer
  em estado não terminal ou desconhecido.
- A adequação de um ator é avaliada por perfil executor e papel, com evidência
  de múltiplas execuções, não pelo nome isolado do modelo.
- Revisão e evidência são proporcionais ao risco e ao recorte.
- Decisões, lacunas e conhecimento afetado continuam registrados.
- Objetivos que atravessam repositórios ou serviços usam uma especificação
  coordenadora e recortes executáveis junto a cada fonte responsável.
- A conclusão local não comprova o objetivo multi-contexto sem evidência de
  integração ponta a ponta.
- O Consultor de Arquitetura apoia transversalmente o Arquiteto e o Tech Lead
  somente sob ordem, recorte e confirmação humana explícitos.
- O fluxo atual não incorpora controles para problemas ainda não adotados.

## Fluxo vigente

```text
Autor → Analista → Implementador → Revisor/Tech Lead
  ↑         │             │                │
  └─ decisão do Arquiteto ┴────────────────┘
                                    ↓
                         decisão humana e integração
```

Os atores oficiais são Autor da Especificação, Engenheiro Analista, Engenheiro
Implementador e Engenheiro Revisor. O fluxo representa a ordem lógica das
etapas. O Consultor de Arquitetura é um papel institucional subordinado ao
Arquiteto, não um quinto ator nem uma autoridade paralela. A EKM 1.18 não
define orquestração, concorrência, locks ou filas, e
esses temas não influenciam os trabalhos atuais.

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
- [`docs/EKM-METHOD.md`](docs/EKM-METHOD.md): método de referência 1.18.
- [`docs/ACTOR-EVALUATION.md`](docs/ACTOR-EVALUATION.md): métrica experimental
  de adequação de perfis executores por papel.
- [`docs/DESIGN-DECISIONS.md`](docs/DESIGN-DECISIONS.md): razões e evolução das decisões.
- [`docs/LEGACY-ADOPTION.md`](docs/LEGACY-ADOPTION.md): adoção incremental.
- [`docs/EXPERIMENT-HISTORY.md`](docs/EXPERIMENT-HISTORY.md): aprendizados dos experimentos.
- [`docs/experiments/COORDINATED-ACTOR-MODEL.md`](docs/experiments/COORDINATED-ACTOR-MODEL.md):
  protocolo experimental 0.8.
- [`docs/experiments/SELF-CONTAINED-IMPLEMENTER-RUN-001.md`](docs/experiments/SELF-CONTAINED-IMPLEMENTER-RUN-001.md):
  execução sequencial com prompt autocontido, Kimi K2.7 Code e Codex.
- [`docs/experiments/REFERENCED-ROLE-PROFILES.md`](docs/experiments/REFERENCED-ROLE-PROFILES.md):
  protocolo 0.2 concluído que originou os perfis oficiais.
- [`docs/case-studies/`](docs/case-studies/): evidências históricas, não regras universais.
- [`docs/case-studies/IOTSMARTHOME-MULTI-AGENT-OBSERVATION.md`](docs/case-studies/IOTSMARTHOME-MULTI-AGENT-OBSERVATION.md):
  resultado funcional e conformidade entre agentes no aplicativo Swift.
- [`docs/case-studies/IOTSMARTSYSCORE-GARAGE-CONTROL-SEQUENTIAL-AGENTS.md`](docs/case-studies/IOTSMARTSYSCORE-GARAGE-CONTROL-SEQUENTIAL-AGENTS.md):
  controle de garagem validado após execução sequencial heterogênea.
- [`docs/case-studies/IOTSMARTHOME-REFERENCED-ACTORS-LIFECYCLE.md`](docs/case-studies/IOTSMARTHOME-REFERENCED-ACTORS-LIFECYCLE.md):
  ciclo completo que sustentou a aprovação do modelo de atores.
- [`templates/prompts/ENGENHEIRO-IMPLEMENTADOR.md`](templates/prompts/ENGENHEIRO-IMPLEMENTADOR.md):
  modelo experimental de instrução autocontida para implementação.
- [`roles/CONSULTOR-DE-ARQUITETURA.md`](roles/CONSULTOR-DE-ARQUITETURA.md):
  papel institucional de apoio transversal ao Arquiteto e ao Tech Lead.
- [`templates/prompts/CONSULTOR-DE-ARQUITETURA.md`](templates/prompts/CONSULTOR-DE-ARQUITETURA.md):
  ordem e registro mínimo para a atuação do Consultor.
- [`roles/`](roles/): regras comuns e perfis oficiais separados por
  responsabilidade.
- [`templates/AGENTS.md`](templates/AGENTS.md):
  roteador oficial para instalar o modelo de atores em um projeto.
- [`templates/prompts/COMANDO-POR-PERFIL.md`](templates/prompts/COMANDO-POR-PERFIL.md):
  ordem mínima para selecionar um perfil fixo.
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md): como evoluir a EKM.
- [`templates/`](templates/): ativos reutilizáveis.

## Adoção rápida

1. O Arquiteto delimita repositório, escopo e restrições.
2. O agente confirma que está em uma branch derivada da `main` e com a árvore
   limpa.
3. O agente aplica
   [`EKM-LEGACY-ADOPTION-INSTRUCTIONS.md`](templates/EKM-LEGACY-ADOPTION-INSTRUCTIONS.md).
4. A fundação instala o roteador `AGENTS.md` e aponta para os perfis EKM.
5. São criados apenas os demais ativos úteis ao próximo trabalho.
6. Cada tarefa identifica papel e especificação, promove seu resultado, cria
   commit, realiza push e termina com árvore limpa.

## Limite

A EKM não substitui testes, revisão, observabilidade ou julgamento humano.
Qualidade e aceleração são hipóteses que devem ser demonstradas em casos reais.
O método evolui quando a evidência mostra utilidade e também quando mostra
burocracia sem retorno.
