# ADR-0003 — Roteamento documental e separação de evidências no EKOM 3.1

**Estado:** Aceita

**Data:** 2026-08-11

**Versão resultante:** EKOM 3.1

## Contexto

O EKOM 3.0 distingue conceitualmente especificação, ADR, relatório, mapa,
changelog e Git, mas não define destinos obrigatórios, ciclo de vida dos
relatórios nem gatilho operacional para ADR. O template vigente de
especificação ainda contém seções para análise de implementabilidade,
evidências da implementação, challenge e decisão final.

No experimento de variantes de firmware do IoTSmartLink15.4, essa contradição
levou a especificação a acumular contrato, análises, relatórios de
implementação, revisão, decisões e encerramento. O resultado funcional e as
fronteiras arquiteturais foram satisfatórios, mas a especificação alcançou
1.573 linhas. Entre o início do recorte e sua integração ocorreram vinte
commits exclusivamente documentais, cinco commits com alteração funcional e
dois merges. O experimento demonstrou valor do mapa e das fronteiras, mas não
demonstrou contexto mínimo nem aceleração do workflow documental.

O caso não decorreu apenas de desobediência dos atores. A ausência de caminhos,
templates, autoridade de escrita e guardas estruturais tornou a especificação o
destino concreto mais disponível para qualquer registro.

## Decisão

### Responsabilidade de cada fonte

- **Especificação:** comportamento pretendido, limites, invariantes, critérios
  de aceite, evidências exigidas e decisões normativas locais vigentes.
- **ADR/RFC:** decisão transversal ou durável, motivação, alternativas,
  trade-offs, consequências e substituição de decisão anterior.
- **Relatório:** fatos, achados, execução e evidências de uma atuação. Não altera
  fonte normativa implicitamente.
- **Mapa:** localização, autoridade, relações e lacunas.
- **Changelog EKOM:** estado resumido da transação de conhecimento e ponteiros
  para as fontes materiais; não é relatório, ADR ou diário do Git.
- **Git:** autoria, diferenças, commits, branches e linhagem técnica.

### Estrutura mínima de projetos adotantes

```text
docs/
├── adr/
├── reports/
│   └── <mudança>/
│       ├── analysis/
│       ├── implementation/
│       ├── review/
│       └── validation/
├── rfc/
└── specs/
```

Projetos podem adaptar os nomes, desde que o `AGENTS.md` e o mapa forneçam
roteamento inequívoco e preservem as mesmas autoridades.

### Autoridade por capacidade

- o Autor e o Arquiteto escrevem o contrato normativo;
- o Analista registra seu resultado em relatório de análise;
- o Implementador altera os artefatos autorizados e registra relatório de
  implementação;
- o Revisor registra challenge em relatório de revisão;
- a pessoa responsável pela validação registra a evidência em relatório de
  validação;
- somente o Arquiteto incorpora achados em especificações, aceita ADRs, promove
  estados normativos e determina conclusão ou reabertura.

Uma ordem pode autorizar atualização documental mecânica fora desse padrão,
mas deve nomear arquivos e transformação. Essa exceção não transfere decisão
normativa.

Cada capacidade pode criar commit com seu resultado material. Push, merge,
promoção ou integração continuam dependentes da ordem e das regras do projeto.

### Gatilho de ADR

ADR é obrigatória quando uma decisão:

- afeta mais de uma especificação ou componente;
- estabelece fronteira, direção de dependência ou restrição permanente;
- escolhe entre alternativas com trade-offs relevantes;
- substitui decisão arquitetural anterior; ou
- precisa ser localizada sem conhecer a especificação que a originou.

Comportamento específico de uma funcionalidade permanece na especificação.
Decisão local de execução permanece no relatório.

### Ciclo de vida

ADRs usam `Proposed`, `Accepted`, `Rejected`, `Deprecated` ou `Superseded`.
Uma ADR aceita não é reescrita para simular uma decisão posterior; a sucessora
declara a substituição.

Relatórios concluídos são históricos e não normativos. Correção factual usa
adendo ou novo relatório relacionado. Cada relatório identifica, quando
aplicável, papel, especificação, revisão confrontada, resultado, evidências,
limitações e decisões requeridas.

### Guardas proporcionais

Projetos adotantes devem verificar automaticamente o que for estrutural e
objetivo: localização, classe da fonte, campos mínimos, estrutura de ADR e
ausência de seções de relatório no template de especificação. Suficiência da
evidência, relevância de achado e necessidade semântica de ADR continuam sob
julgamento humano.

## Consequências

- especificações ficam menores e orientadas ao contrato vigente;
- análises e evidências continuam versionadas sem adquirir autoridade
  normativa;
- decisões transversais tornam-se localizáveis independentemente da
  especificação de origem;
- o Arquiteto passa a realizar uma incorporação explícita entre achado e
  mudança normativa;
- projetos adotantes precisam criar destinos e adaptar seu roteamento antes de
  migrar conteúdo existente;
- há custo adicional de arquivos e referências, mitigado por templates curtos
  e pela proibição de duplicar Git ou narrativas completas no changelog.

## Compatibilidade e migração

A mudança é `minor`: preserva autoridade, estados e workflow do EKOM 3.0, mas
torna operacional uma separação já declarada. Registros antigos permanecem
válidos sob a versão usada.

Novas atuações devem adotar o roteamento assim que o projeto migrar para EKOM
3.1. Conteúdo histórico não é movido automaticamente. Primeiro criam-se os
destinos; depois cada migração identifica o que permanece normativo, o que vira
ADR e o que se torna relatório, com autorização do Arquiteto.
