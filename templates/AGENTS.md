# Instruções para agentes

Este repositório adota Engineering Knowledge Management (EKM).

Antes de qualquer atuação, leia nesta ordem:

1. `docs/rfc/EKM-GUIDELINES.md`;
2. `docs/rfc/KNOWLEDGE-MAP.md`;
3. as especificações relacionadas à tarefa em `docs/specs/`, considerando seu
   estado normativo;
4. `docs/rfc/EKM-CHANGELOG.md` e a transação aberta.

Quando o projeto adotar o experimento de coordenação por atores, leia também
`docs/experiments/COORDINATED-ACTOR-MODEL.md` ou a referência externa declarada
pelo projeto.

## Papel obrigatório

Antes de atuar, declare exatamente um papel:

- Coordenação do processo;
- Autor da Especificação;
- Engenheiro Analista;
- Engenheiro Implementador;
- Engenheiro Tech Lead;
- Validador de Integridade da EKM.

Não acumule papéis na mesma execução. Se a tarefa não indicar um papel e a ação
puder pertencer a mais de uma etapa, interrompa e solicite definição.

Valide o checkpoint de entrada, os estados esperados e a transação antes de
atuar. A Coordenação deve declarar a fonte EKM, a versão do contrato aplicável e
qualquer normalização desde o checkpoint anterior. Registre a saída na seção
correspondente da mesma `EKM-CHG`.

## Regras obrigatórias

- A especificação define o comportamento esperado; não invente contratos ausentes.
- A modalidade de confecção da especificação fica fora do contrato. A EKM não
  prevê nem exige automação da autoria. Se atuar como Autor, aplique o contrato
  ao artefato resultante.
- O Autor da Especificação preenche as seções normativas, encerra em `Proposed`
  com parecer humano `Pending` e `Pending Review`, e não executa a Technical
  Readiness Review.
- Antes da análise, deve existir parecer humano explícito `Accepted` sobre a
  especificação e o checkpoint. Nenhum agente pode inferir, fabricar ou conceder
  esse parecer.
- O parecer humano da especificação não substitui `Implementable` nem a
  aprovação humana posterior para implementação.
- A seção de Technical Readiness Review pertence exclusivamente ao Engenheiro
  Analista.
- Antes da Technical Readiness Review, o Analista executa o gate de admissão
  sobre branch, SHA, worktree, estados, parecer humano da especificação,
  transação, contrato aplicável e artefatos da autoria.
- `Checkpoint Blocked` encerra a atuação antes da revisão, não altera
  `Technical readiness` e retorna à Coordenação. Não é resultado da Technical
  Readiness Review.
- Antes de qualquer alteração de implementação, deve existir uma Technical
  Readiness Review integral executada pelo Engenheiro Analista e seu resultado
  deve estar registrado. Somente `Implementable` pode seguir para aprovação
  humana; `Needs Clarification` bloqueia a implementação.
- Classifique individualmente todos os requisitos e dimensões obrigatórias em uma matriz de evidências. Um bloqueio interrompe a implementação, mas não encerra a análise restante.
- Na matriz do Analista, classifique a natureza de cada lacuna como
  `Normative`, `Baseline`, `Tooling`, `Evidence` ou `None`.
- O Analista classifica toda dúvida ou decisão já declarada como `Blocking`,
  `Non-blocking`, `Out of scope` ou `Unrequested option`.
- Execute a Technical Readiness Review e a implementação em execuções separadas. A execução da revisão deve encerrar sem alterar implementação, inclusive com resultado `Implementable`.
- Trate `Implementable` como apto para aprovação humana, não como autorização automática. Implemente somente após aprovação explícita do responsável para a revisão e o baseline registrados.
- Antes da primeira alteração, reconfirme especificação, parecer humano, branch,
  commit, worktree, resultado aprovado e transação `Open`. Mudança material
  exige novo parecer humano e nova revisão integral.
- Se qualquer requisito obrigatório exigir inferência relevante, não implemente nenhum item; registre a lacuna e proponha o ajuste na especificação.
- Após ajuste aprovado da especificação, repita a análise integral antes de implementar.
- Em `Needs Clarification`, altere somente registros EKM e a correção normativa explicitamente aprovada.
- Reporte `Needs Clarification` como bloqueio, nunca como implementação concluída.
- Preserve APIs, contratos e conhecimento normativo salvo autorização explícita.
- Considere todo o worktree inicial como baseline.
- Abra ou identifique uma transação EKM antes de mudança relevante.
- Registre lacunas em vez de preenchê-las por suposição.
- Não transforme descoberta em decisão de produto, arquitetura, contrato, persistência, segurança, compatibilidade ou comportamento.
- Não reescreva versão de especificação já integrada à referência de produção; crie uma nova especificação relacionada.
- Não presuma que exista `EKM Gate` ou garantia automatizada sem ferramenta e política explicitamente implantadas.
- Não execute operações Git ou externas não autorizadas.
- Preserve alterações preexistentes e fora do escopo.
- O Tech Lead revisa e produz parecer ou recorte corretivo; não implementa a
  correção.
- O Validador audita o processo; não repete a Technical Readiness Review, não
  substitui o Tech Lead e não corrige artefatos.

## Relatório obrigatório

Use a seção do seu papel na transação `EKM-CHG`. Informe checkpoint, resultado,
requisitos ou controles avaliados, arquivos, evidências, validações, pendências,
desvios, estados recomendados, comandos, resultados, operações Git ou externas,
artefatos temporários e reconciliação do worktree. Não preencha a seção de
outro papel.
