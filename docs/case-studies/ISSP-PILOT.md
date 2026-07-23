# Estudo de caso — Refatoração ISSP

## Contexto

Um firmware IEEE 802.15.4 funcional precisava transformar sua stack ISSP em componentes reutilizáveis. A refatoração envolveu transporte, protocolo, commissioning, reports, comandos, persistência e integração em hardware.

## Hipótese inicial

Um arquiteto humano poderia definir recortes enquanto um agente implementaria código, build, testes e relatórios. A combinação deveria aumentar produtividade sem transferir as decisões arquiteturais.

## Evidências observadas

### Especificações reduziram expansão de escopo

Recortes com objetivo, limites e critérios explícitos produziram implementações mais disciplinadas e relatórios técnicos úteis.

### Hardware revelou hipóteses incorretas

Builds aprovados não detectaram conflitos de ciclo de vida do rádio nem algumas condições de concorrência. A validação em hardware permaneceu indispensável.

### Conhecimento normativo foi perdido

Durante uma consolidação, um documento de arquitetura foi reescrito e perdeu decisões vigentes. O código compilava e o relatório não tornou a perda suficientemente visível.

### `HEAD` não representava todo o baseline

Uma auditoria de componentes reutilizáveis precisou recuperar alterações que já existiam no worktree antes da tarefa. A equivalência só foi comprovada contra o estado inicial registrado.

## Mudanças introduzidas na EKM

- proteção explícita de documentos normativos;
- separação entre especificação, diretriz e relatório;
- princípio de reconstruibilidade;
- baseline baseado no worktree real;
- transações `EKM-CHG` e lacunas `EKM-GAP`;
- reabertura de mudanças quando a evidência é insuficiente;
- dois estados independentes para especificações;
- relatório semântico de ativos de conhecimento.

## Resultado

O experimento demonstrou utilidade operacional das especificações e expôs a insuficiência de código, build, Git e relatórios como proteção isolada do conhecimento.

## Limitação

O caso ocorreu em um projeto embarcado específico, com forte participação do arquiteto e validação manual em hardware. Ele não comprova que o método funciona sem adaptação em outros contextos.
