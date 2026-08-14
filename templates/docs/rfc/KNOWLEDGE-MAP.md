# EKOM — Mapa da Fonte Única da Verdade

**Classe da fonte:** Normativa

**Estado da fonte:** Vigente

O mapa localiza autoridade, estrutura e relações sem duplicar contratos
detalhados. A tabela responde onde está a fonte; a árvore, como o domínio se
organiza; o diagrama, como elementos separados se conectam.

## 1. Governança

| Área | Fonte | Tipo | Estado |
|---|---|---|---|
| Instruções para agentes | `AGENTS.md` | Normativo | Active |
| Diretrizes EKOM | `<REFERÊNCIA EXTERNA OU docs/rfc/EKOM-GUIDELINES.md>` | Normativo | Active |
| Mapa de conhecimento | `docs/rfc/KNOWLEDGE-MAP.md` | Normativo | Active |
| Histórico EKOM | `docs/rfc/EKOM-CHANGELOG.md` | Operacional | Active |
| Visão do sistema | `docs/specs/SYSTEM-DOSSIER.md` | `<CLASSIFICAÇÃO>` | `<ESTADO>` |

## 2. Índice de domínios e autoridade

| Domínio | Fonte normativa | Estado do workflow | Código principal | Evidência | Cobertura |
|---|---|---|---|---|---|
| `<DOMÍNIO>` | `<ESPECIFICAÇÃO OU GAP>` | `<RASCUNHO E ANÁLISE/PRONTA/IMPLEMENTAÇÃO/VALIDAÇÃO/CONCLUÍDA>` | `<CAMINHOS>` | `<TESTES/BUILD/AMBIENTE REAL>` | `<NÍVEL>` |

## 3. Árvore de conhecimento

A árvore é obrigatória quando contenção, composição ou responsabilidade for
material: mais de um runtime target, aplicativo, serviço ou firmware, ou três
ou mais domínios/componentes relacionados. Caso contrário, registre `Não se
aplica` e a justificativa.

```text
<REPOSITÓRIO OU SISTEMA>
├── <ALVO, DOMÍNIO OU APLICAÇÃO>
│   ├── <RESPONSABILIDADE OU COMPONENTE>
│   └── <RESPONSABILIDADE OU COMPONENTE>
└── <ALVO, DOMÍNIO OU APLICAÇÃO>
    └── <RESPONSABILIDADE OU COMPONENTE>
```

Use a menor árvore capaz de orientar localização. Não liste cada arquivo nem
repita requisitos das especificações.

## 4. Diagrama de relações

O diagrama Mermaid é obrigatório quando alvos implantáveis separadamente se
conectarem por protocolo, API, evento ou dados, ou quando um fluxo cruzar três
ou mais fronteiras. Caso contrário, registre `Não se aplica` e a justificativa.

```mermaid
flowchart LR
    A["ALVO OU DOMÍNIO A"] -->|"PROTOCOLO, API OU FLUXO"| B["ALVO OU DOMÍNIO B"]
```

Mantenha o diagrama pequeno e estável. Detalhes comportamentais pertencem às
fontes apontadas pelo índice.

## 5. Lacunas

| ID | Estado | Lacuna | Critério de encerramento | Dependência |
|---|---|---|---|---|
| `EKOM-GAP-0001` | `Open` | `<DESCRIÇÃO>` | `<EVIDÊNCIA OBJETIVA>` | `<DECISÃO OU TAREFA>` |

## 6. Débitos técnicos

Use esta seção somente para postergações aceitas explicitamente pelo Arquiteto.
Achado ainda não classificado permanece no relatório correspondente; lacuna de
conhecimento permanece em `EKOM-GAP`.

| ID | Estado | Condição e alcance | Evidência | Consequência | Decisão de postergação | Gatilho ou critério de quitação | Relações |
|---|---|---|---|---|---|---|---|
| `EKOM-DEBT-0001` | `Accepted` | `<CONDIÇÃO CONHECIDA E ALCANCE>` | `<FONTE OU EVIDÊNCIA>` | `<CUSTO, RISCO OU LIMITAÇÃO>` | `<DECISÃO DO ARQUITETO>` | `<CONDIÇÃO OBJETIVA>` | `<ESPECIFICAÇÃO, ADR, GAP OU CHG>` |

Estados admitidos: `Accepted`, `In Remediation`, `Repaid` e `Superseded`.
Somente o Arquiteto aceita a postergação e determina a quitação ou substituição.

## 7. Manutenção

**Namespace de transações, lacunas e débitos:** `EKOM` | `EKM` legado para
transações e lacunas

Atualize este mapa quando uma especificação, fonte relacionada, autoridade,
responsabilidade, evidência, estado, lacuna ou débito mudar. Cada domínio deve
apontar para uma especificação como autoridade normativa; não remova entrada
sem indicar o destino do conhecimento.

Reconcilie também a árvore quando contenção ou responsabilidade mudar e o
diagrama quando surgir, desaparecer ou mudar uma relação material entre alvos.

Somente o Arquiteto determina Concluída ou Reaberta. Estados mais granulares
podem permanecer na especificação quando necessários, sem transferir essa
autoridade.
