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
