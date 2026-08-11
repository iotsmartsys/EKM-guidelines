# Método EKOM

**Versão do documento:** 3.2

**Modelo EKOM:** 3.2

**Estado:** aprovado e vigente

## 1. Objetivo operacional

O EKOM permite que uma solução seja especificada, implementada, documentada e
entregue sem que o Arquiteto precise executar diretamente o desenvolvimento.
A especificação governa a execução dos agentes de IA; o Arquiteto mantém
autoridade sobre decisões, riscos, validação e conclusão do workflow.

> **Specifications orchestrate. Code implements.**

O método usa a menor dose de governança capaz de manter conhecimento vigente,
decisões relevantes registradas, execução auditável e resultados verificáveis.
Um controle sem ganho proporcional não é universalizado.

## 2. Autoridade do Arquiteto

O Arquiteto humano é a autoridade final sobre:

- intenção, prioridade e escopo;
- decisões arquiteturais;
- risco aceitável;
- relevância das críticas;
- suficiência das evidências;
- aprovação da solução;
- conclusão ou reabertura do workflow;
- integração, publicação e operação quando aplicável.

O Arquiteto não é um aprovador formal de decisões da IA. Ele confronta
recomendações e fatos, decide e assume responsabilidade pelo risco. Agentes
podem apontar conflitos, consequências e alternativas, mas não substituem essa
decisão nem expandem silenciosamente o escopo.

Autoridade humana não modifica evidência. Uma validação falha continua
registrada como falha. O Arquiteto pode aceitar risco residual, pedir nova
evidência, corrigir a implementação ou evoluir a especificação.

## 3. Especificação e fontes relacionadas

| Fonte | Responsabilidade |
|---|---|
| Especificação | comportamento, limites, estados e critérios de aceite |
| ADR ou RFC | razão de decisão e relação com a especificação afetada |
| Diretriz | regras do método e preservação local |
| Mapa de conhecimento | localização de fontes e lacunas |
| Changelog EKOM | estado resumido da transação e ponteiros para fontes materiais |
| Dossiê | visão factual e navegação do sistema |
| Código e testes | implementação e evidências técnicas |
| Relatório | evidência de uma execução; não cria requisito |

Para cada comportamento existe uma autoridade normativa identificável.
"Fonte da verdade" não exige arquivo monolítico: especificações podem se
relacionar sem duplicar contratos.

Git registra autoria, branches, diferenças e linhagem. Esses dados não são
copiados manualmente para documentos, salvo quando necessários para explicar
decisão ou desvio material.

### 3.1 Preservação arquitetural local

O `AGENTS.md` do projeto localiza arquitetura, padrões e restrições. Por padrão,
toda implementação preserva organização e separação de responsabilidades,
segue o precedente equivalente mais próximo e não cria nova camada, estrutura
ou abstração transversal por preferência do agente.

Uma evolução arquitetural identifica o padrão atual, a mudança, o alcance e a
decisão do Arquiteto. Ausência ou conflito de precedentes é incerteza a
registrar, não autorização implícita.

### 3.2 Unidade de trabalho

A especificação incremental é a unidade de comportamento, delegação e
orquestração. Ela contém o necessário para executar e avaliar o recorte:

- objetivo, contexto, escopo e fora de escopo;
- requisitos, contratos, estados e falhas relevantes;
- critérios de aceite e evidências esperadas;
- impactos, restrições, incertezas e experimentos necessários;
- referência ao relatório de análise e estado vigente dos bloqueadores.

Versões concluídas são preservadas. Mudanças posteriores usam nova versão
relacionada por `Amends`, `Supersedes`, `Corrects` ou `Retires`, ou reabertura
explícita pelo Arquiteto quando a convenção local assim determinar.

### 3.3 Critérios assertáveis sem fetichizar testes

Cada requisito obrigatório deve permitir distinguir sucesso, falha e ausência
de evidência. Na forma mínima adequada ao risco, o critério identifica cenário,
ação, resultado observável e meio de validação. `Dado / Quando / Então` é uma
linguagem útil, não obrigação de Gherkin ou ferramenta BDD.

Critérios como "adicionar testes", "validar o fluxo" ou "build aprovado" são
insuficientes quando não declaram o comportamento observado. Doubles preservam
a semântica material da integração substituída. Compilação comprova
compilabilidade, não execução; zero casos não comprova comportamento.

Isso não transforma teste em prova absoluta nem exige um teste por requisito.
O oráculo orienta a investigação e a evidência; o Arquiteto decide se o
conjunto produzido é suficiente para aceitar o risco.

### 3.4 Objetivos multi-contexto

Quando um objetivo atravessa repositórios, serviços, aplicativos ou
infraestrutura, uma especificação coordenadora preserva o objetivo ponta a
ponta e cada contexto mantém seu contrato local. A conclusão coordenada exige
evidências materiais dos recortes e da integração; estados locais não a
comprovam automaticamente.

### 3.5 Roteamento documental

Responsabilidade conceitual exige destino operacional. Projetos EKOM 3.1
declaram no `AGENTS.md` e no mapa caminhos distintos para especificações,
ADRs/RFCs, relatórios, changelog e mapa.

```text
Especificação → contrato vigente e evidências exigidas
ADR/RFC       → decisão arquitetural durável e suas consequências
Relatório     → fatos, achados e evidências de uma atuação
Mapa          → localização, autoridade, relações e lacunas
Changelog     → estado resumido da transação e referências
Git           → autoria, diferenças e linhagem técnica
```

Análise, implementação, challenge e validação produzem relatórios separados.
Esses relatórios podem recomendar mudança normativa, mas somente o Arquiteto a
incorpora à especificação ou aceita uma ADR. Relatórios concluídos são
históricos; correção factual usa adendo ou novo relatório relacionado.

ADR é obrigatória quando a decisão cruza especificações ou componentes,
estabelece fronteira ou direção de dependência, impõe restrição durável,
envolve trade-offs relevantes ou substitui decisão arquitetural anterior.
Comportamento local permanece na especificação; escolha local de execução,
no relatório.

O roteamento, os ciclos de vida e a migração estão definidos na
[`ADR-0003`](adr/ADR-0003-DOCUMENT-ROUTING-AND-EVIDENCE-SEPARATION.md).

### 3.6 Visões do mapa de conhecimento

O mapa combina três perguntas sem duplicar contratos:

| Visão | Pergunta |
|---|---|
| Índice tabular | Onde está a fonte e qual sua autoridade? |
| Árvore | Como alvos, domínios e responsabilidades se organizam? |
| Diagrama | Como elementos separados se conectam ou dependem entre si? |

O índice de autoridade é obrigatório. A árvore é obrigatória quando contenção,
composição ou responsabilidade for material, especialmente com múltiplos
runtime targets ou três ou mais domínios relacionados. Mermaid é obrigatório
quando alvos implantáveis separadamente se conectarem por protocolo, API,
eventos ou dados, ou quando um fluxo cruzar três ou mais fronteiras.

Uma visão não aplicável permanece declarada com justificativa curta. Visuais
devem ser pequenos, estáveis e navegacionais; comportamento detalhado continua
na especificação ou ADR apontada pelo mapa. A regra completa está na
[`ADR-0004`](adr/ADR-0004-KNOWLEDGE-MAP-VISUAL-STRUCTURE.md).

## 4. Ciclo de vida e workflow

O workflow usa no máximo cinco estados principais de leitura operacional:

```mermaid
flowchart LR
    A["Rascunho e análise"] -->|"Arquiteto considera suficiente"| P["Pronta"]
    P --> I["Implementação"]
    I --> V["Validação"]
    V -->|"somente o Arquiteto conclui"| C["Concluída"]

    A -->|"lacunas: permanece"| A
    I -->|"restrição ou ambiguidade"| A
    V -->|"defeito de implementação"| I
    V -->|"problema na especificação"| A
    C -->|"nova necessidade ou evidência material; Arquiteto reabre"| A
```

- **Rascunho e análise:** intenção, investigação e análise de
  implementabilidade evoluem juntas; lacunas mantêm ou devolvem o trabalho a
  este estado.
- **Pronta:** o Arquiteto considera o contrato suficiente para implementar,
  conhecendo incertezas e experimentos ainda necessários.
- **Implementação:** agentes executam, verificam tecnicamente e registram
  decisões locais, dúvidas, limitações e desvios. Restrição ou ambiguidade
  normativa retorna à análise.
- **Validação:** evidências são confrontadas com a especificação e o ambiente.
  Defeito retorna à implementação; problema no contrato retorna ao rascunho.
- **Concluída:** somente o Arquiteto determina que evidência e risco residual
  são suficientes. Nova necessidade, regressão ou evidência pode motivar
  reabertura pelo próprio Arquiteto.

Retornos não são necessariamente fracasso. São aprendizado e evolução
controlada da especificação. Projetos que precisem de estados técnicos mais
granulares podem mantê-los, desde que não transfiram a autoridade de conclusão.

## 5. Funções e papéis

Função necessária não implica pessoa, sessão ou agente separado. A segregação
é uma decisão proporcional a risco, incerteza, especialização e valor da
independência real.

### 5.1 Autor da Especificação

O Autor transforma a intenção em solução proposta, implementável e verificável.
Consulta repositório, arquitetura, conhecimento e precedentes. Pode usar IA
para localizar impactos, restrições e incertezas.

Ele diferencia fatos observados, decisões confirmadas, recomendações e
pendências. Não transforma comportamento legado em requisito nem preferência
técnica em decisão.

### 5.2 Análise de implementabilidade

A análise é obrigatória antes da implementação. Pode ser executada:

- pelo próprio Autor;
- pelo Autor apoiado por IA;
- por agente especializado;
- por especialista separado quando risco ou incerteza justificarem segregação.

Seu relatório registra:

- evidências encontradas no repositório;
- componentes e fontes impactados;
- restrições conhecidas;
- incertezas;
- experimentos necessários;
- bloqueadores identificados.

Leitura de código não certifica comportamento que só pode ser confirmado por
build, protótipo, API, banco, infraestrutura ou hardware. Esses pontos são
registrados como experimentos necessários. A especificação fica Pronta apenas
quando o Arquiteto considerar a análise suficiente para autorizar execução.

### 5.3 Implementador

O Implementador:

- implementa conforme a especificação autorizada;
- realiza verificações técnicas proporcionais ao risco;
- registra decisões locais no relatório de implementação;
- produz relatório e evidências sem anexá-los à especificação;
- declara dúvidas, limitações e desvios;
- devolve ambiguidade normativa ao rascunho/análise.

Ele não usa testes escolhidos ou escritos durante a própria implementação como
argumento autorreferente de correção. Testes compõem a evidência disponível e
podem ser fortes, insuficientes ou até semanticamente enganosos.

### 5.4 Crítico ou Revisor

Challenge é capacidade consultiva, não gate universal. Pode ser acionado:

- pelo Arquiteto;
- pelo risco da mudança;
- por falha recorrente;
- por segurança, autorização, corrupção de dados, concorrência ou operação
  irreversível;
- quando uma segunda perspectiva tiver valor justificável.

O crítico levanta riscos, inconsistências e pontos cegos e pode concluir que
não encontrou risco adicional relevante. Não substitui o Arquiteto, não aprova
ou reprova o workflow, não redefine critérios unilateralmente, não obriga o
Implementador a satisfazer narrativa de testes e não reabre decisão registrada
sem nova evidência.

Múltiplos agentes com capacidades, contexto e vieses semelhantes não equivalem
necessariamente a revisão independente. Quando independência for material, o
Arquiteto define como obtê-la e quais conflitos de participação invalidam a
alegação.

### 5.5 Consultor de Arquitetura

O Consultor apoia investigação, desenho, governança, especificação, análise,
implementação, revisão e coordenação dentro do recorte autorizado. Não recebe
autoridade humana e não alega independência no trabalho de que participou.

## 6. Validação proporcional

Testes automatizados são evidências, não prova absoluta. Não são descartados:
são particularmente valiosos para regressões, regras complexas, casos
limítrofes, segurança e contratos estáveis.

Aplicam-se as regras:

1. testes não são alterados apenas para produzir resultado verde;
2. teste verde não comprova sozinho correção funcional ou arquitetural;
3. a exigência de testes é proporcional ao risco e ao valor;
4. falha, ausência de execução e limitação de ambiente permanecem explícitas;
5. execução em dispositivo, API, banco ou infraestrutura real pode ter
   precedência para aceitação funcional;
6. evidência real não elimina automaticamente a necessidade de regressão,
   segurança ou observabilidade;
7. o Arquiteto decide a suficiência do conjunto de evidências.

Evidências materiais podem incluir código e diffs, builds, execução real, logs,
testes, integrações, relatórios, decisões humanas e defeitos posteriores.

## 7. Ordem e execução dos agentes

Cada atuação começa por ordem do Arquiteto, diretamente ou por automação
autorizada. A ordem seleciona objetivo, especificação, função, recorte e
operações; não cria requisito concorrente.

Antes de agir, o agente lê o `AGENTS.md`, as regras comuns, o perfil aplicável,
a especificação e somente as fontes pertinentes. Uma mesma atuação pode
combinar autoria e análise quando isso estiver autorizado. Segregação de papéis
é registrada quando exigida por risco.

O Arquiteto decide transições relevantes. Agentes atualizam fatos, estados e
evidências sustentados por sua execução, mas não declaram aprovação ou
conclusão em nome próprio.

## 8. Contrato Git

Cada tarefa material deve:

1. começar em branch de trabalho derivada da `main`, nunca diretamente nela;
2. preservar alterações preexistentes e começar com árvore limpa;
3. produzir resultado material e versionável;
4. criar commit ao fim da etapa autorizada;
5. realizar push quando a ordem e as regras locais autorizarem;
6. terminar com árvore limpa.

A ordem normal não autoriza force push, reescrita, merge, tag, release ou
deploy. Git é a evidência desses atos; documentos não repetem hashes sem motivo
material.

### 8.1 Encerramento de execuções iniciadas

Antes de promover estado, registrar validação como aprovada, criar commit,
realizar push ou responder conclusivamente, o agente confirma o estado terminal
de toda tarefa, build, teste, upload ou execução delegada que iniciou. Estado
pendente ou desconhecido bloqueia conclusão; cancelamento não fabrica sucesso.

## 9. Transações e lacunas

`EKOM-CHG-NNNN` identifica mudança; `EKOM-GAP-NNNN`, conhecimento ausente que
precisa sobreviver. Projetos migrados podem manter namespaces EKM históricos.

Uma transação registra objetivo, especificação relacionada, estado, lacunas,
resultado e referências para ADRs ou relatórios materiais. Não é relatório,
diário de comandos ou espelho do Git.
Fechamento documental não substitui a decisão do Arquiteto de concluir a
especificação.

## 10. Adoção em legado

A adoção começa pequena:

1. inventariar sistema e fontes existentes;
2. criar fundação mínima;
3. registrar lacunas que afetam decisões reais;
4. especificar em profundidade somente o que será tocado;
5. aumentar controles apenas quando a experiência demonstrar valor.

Fundação recomendada:

```text
AGENTS.md
docs/
├── adr/
├── reports/
├── rfc/
│   ├── KNOWLEDGE-MAP.md
│   └── EKOM-CHANGELOG.md
└── specs/
    └── SYSTEM-DOSSIER.md
```

## 11. Aprendizado experimental

O EKOM registra código, diffs, builds, execução real, logs, testes, integrações,
relatórios, decisões e defeitos posteriores para confrontar tanto a solução
quanto o próprio método. Hipóteses podem ser sustentadas, revisadas ou
refutadas. Mudanças do modelo recebem versionamento e decisão rastreável.

Avaliação de perfil executor permanece instrumento experimental opcional. Ela
não é gate universal nem substitui avaliação da solução e decisão do Arquiteto.

## 12. Limites atuais

O EKOM 3.2 não define infraestrutura distribuída de agentes e não promete
autonomia completa de julgamento. O modelo atual não substitui Arquiteto,
testes, revisão, observabilidade ou CI/CD. Autonomia completa permanece
horizonte evolutivo condicionado a evidências futuras.
