# ADR-0001 — Evolução de EKM para EKOM

**Estado:** aceita

**Data:** 2026-08-01

**Decisores:** Arquiteto humano

## Contexto

O projeto foi formulado originalmente como Engineering Knowledge Model (EKM).
Nas versões 1.x, o modelo organizou conhecimento de engenharia, separou
responsabilidades entre atores, definiu estados e tornou intenção, decisões e
evidências recuperáveis por humanos e agentes de IA.

Os experimentos mostraram, porém, que a especificação não apenas descreve o
trabalho. Ela determina o recorte, autoriza passagens por estado, coordena
atores, orienta implementação e validação, recebe evidências e preserva a
evolução do comportamento. O termo *Model* sozinho tornou-se insuficiente para
expressar essa função.

A formulação anterior também declarava que a verdade era distribuída entre
fontes e que orquestração estava fora do método. Isso permitia interpretar
código, relatório, prompt ou automação como autoridades concorrentes. O EKOM
precisa distinguir a autoridade normativa da especificação das fontes que a
explicam, implementam ou comprovam.

## Decisão

O nome oficial passa a ser:

> **Engineering Knowledge Orchestration Model (EKOM)**

O EKOM é um framework de orquestração *specification-first* no qual o
conhecimento de engenharia atua como plano de controle da engenharia de
software. A especificação é a fonte única da verdade para o comportamento
pretendido e o principal objeto do pipeline, coordenando humanos, agentes de
IA, automações, implementação, validação, evidências e evolução.

> **Specifications orchestrate. Code implements.**

"Fonte única da verdade" significa autoridade normativa única por
comportamento, não concentração de todo o conhecimento em um arquivo. ADRs,
diretrizes, mapas, código, testes, Git e relatórios mantêm responsabilidades
próprias e referenciam a especificação aplicável sem competir com ela.

A mudança inaugura o EKOM 2.0 porque substitui decisões centrais do modelo 1.x.
O fluxo de atores, os estados, a autoridade humana, a governança proporcional,
a reconstruibilidade e os contratos Git permanecem compatíveis.

## Compatibilidade e história

- Documentos de experimentos e casos de estudo preservam EKM e as versões 1.x
  quando descrevem o modelo usado na época.
- `EKM-CHG-NNNN` e `EKM-GAP-NNNN` permanecem identificadores aceitos para não
  quebrar repositórios adotantes. Novas adoções podem usar `EKOM-CHG-NNNN` e
  `EKOM-GAP-NNNN`; um mesmo projeto escolhe um namespace e o declara no mapa.
- Caminhos oficiais com EKM no nome são renomeados para EKOM. Links antigos
  devem ser migrados deliberadamente; registros históricos não são reescritos.
- O nome físico do repositório e do remoto pode permanecer `EKM-guidelines`
  durante a transição, mas não define o nome conceitual vigente.

## Consequências

- Toda atuação funcional começa na especificação aplicável e devolve a ela ou
  às fontes explicitamente relacionadas os estados e evidências produzidos.
- Prompts, ordens e automações acionam o pipeline, mas não criam comportamento
  normativo fora da especificação.
- Código é um artefato derivado que implementa o contrato; divergência exige
  corrigir a implementação ou evoluir a especificação por decisão autorizada.
- O mapa de conhecimento localiza a autoridade normativa e suas derivações.
- Orquestração lógica passa a integrar o núcleo do método. Filas, locks,
  escalonadores e publicação distribuída continuam mecanismos opcionais.

## Decisões substituídas

Esta ADR substitui:

- DD-002, na parte em que admitia verdade normativa distribuída sem uma
  autoridade primária por comportamento;
- DD-021, na parte em que restringia o pipeline a uma ordem lógica sem
  reconhecer a especificação como plano de controle;
- os limites da EKM 1.19 que excluíam orquestração do método.

As motivações históricas dessas decisões permanecem registradas em
[`DESIGN-DECISIONS.md`](../DESIGN-DECISIONS.md).
