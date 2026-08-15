# Relatórios EKOM

Relatórios preservam fatos, achados e evidências de uma atuação. Não criam nem
alteram requisitos, decisões arquiteturais ou estados por autoridade própria.

Organize-os por mudança e capacidade:

```text
docs/reports/<mudança>/
├── analysis/
├── implementation/
├── review/
└── validation/
```

Depois de concluído, um relatório é histórico. Correção factual usa adendo ou
novo relatório relacionado; o original não é reescrito para refletir decisão
posterior. Metadados já preservados pelo Git não devem ser copiados sem motivo
material.

Cada análise formal cria exclusivamente um arquivo novo em `analysis/`, com UTC
e unicidade no nome:

```text
YYYY-MM-DDTHHMMSSZ-<revisão>-<id-da-execução>-implementability-analysis.md
```

Exemplo:

```text
2026-08-15T021530Z-91b3e67-run-31840956083-implementability-analysis.md
```

O run ID da automação ou outro identificador único nomeia a execução. Colisão
interrompe a escrita. Reanálise e correção criam novo arquivo relacionado. O
delta da atuação deve registrar `A`; `M` ou `D` em relatório existente exige
ordem específica do Arquiteto.
