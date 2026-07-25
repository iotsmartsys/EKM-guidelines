# Instruções para agentes

Este repositório adota Gestão do Conhecimento de Engenharia
(*Engineering Knowledge Management* — EKM).

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
- Engenheiro Líder Técnico (`Tech Lead`);
- Validador de Integridade da EKM.

Não acumule papéis na mesma execução. Se a tarefa não indicar um papel e a ação
puder pertencer a mais de uma etapa, interrompa e solicite definição.

Valide o marco versionado de entrada, os estados esperados e a transação antes de
atuar. A Coordenação deve declarar a fonte EKM, a versão do contrato aplicável e
qualquer normalização desde o marco anterior. Registre a saída na seção
correspondente da mesma `EKM-CHG`.

## Regras obrigatórias

- Use português do Brasil na prosa normativa. Preserve nomes de ferramentas,
  comandos, APIs e identificadores no idioma original e apresente estados e
  resultados com o rótulo canônico e o identificador legado quando necessário.
- Não use isoladamente `Accepted`, `Pending` ou `Blocked`; declare o contexto do
  parecer, da admissão, da implementação, da transação ou da auditoria.
- A especificação define o comportamento esperado; não invente contratos ausentes.
- A modalidade de confecção da especificação fica fora do contrato. A EKM não
  prevê nem exige automação da autoria. Se atuar como Autor, aplique o contrato
  ao artefato resultante.
- O Autor da Especificação preenche as seções normativas, encerra em Proposta
  [`Proposed`] com parecer humano Pendente [`Pending`] e revisão Pendente de
  revisão [`Pending Review`], e não executa a revisão de implementabilidade.
- Antes da análise, deve existir parecer humano explícito de Intenção aceita
  [`Accepted`] sobre a especificação e o marco versionado. Nenhum agente pode
  inferir, fabricar ou conceder
  esse parecer.
- O parecer humano da especificação não substitui Implementável
  [`Implementable`] nem a
  aprovação humana posterior para implementação.
- A seção da revisão de implementabilidade pertence exclusivamente ao Engenheiro
  Analista.
- Antes da revisão de implementabilidade, o Analista executa o ponto de controle de admissão
  sobre branch, SHA, árvore de trabalho, estados, parecer humano da especificação,
  transação, contrato aplicável e artefatos da autoria.
- Marco bloqueado [`Checkpoint Blocked`] encerra a atuação antes da revisão,
  não altera o estado da revisão de implementabilidade e retorna à Coordenação.
  Não é resultado da revisão de implementabilidade.
- Antes de qualquer alteração de implementação, deve existir uma revisão de
  implementabilidade integral executada pelo Engenheiro Analista e seu resultado
  deve estar registrado. Somente Implementável [`Implementable`] pode seguir
  para aprovação humana; Precisa de esclarecimento [`Needs Clarification`]
  bloqueia a implementação.
- Classifique individualmente todos os requisitos e dimensões obrigatórias em uma matriz de evidências. Um bloqueio interrompe a implementação, mas não encerra a análise restante.
- Na matriz do Analista, classifique a natureza de cada lacuna como Normativa
  [`Normative`], Estado de referência [`Baseline`], Ferramentas [`Tooling`],
  Evidência [`Evidence`] ou Nenhuma [`None`].
- O Analista classifica toda dúvida ou decisão já declarada como Bloqueante
  [`Blocking`], Não bloqueante [`Non-blocking`], Fora de escopo
  [`Out of scope`] ou Opção não solicitada [`Unrequested option`].
- Execute a revisão de implementabilidade e a implementação em execuções
  separadas. A execução da revisão deve encerrar sem alterar implementação,
  inclusive com resultado Implementável [`Implementable`].
- Trate Implementável [`Implementable`] como apto para aprovação humana, não
  como autorização automática. Implemente somente após aprovação explícita do
  responsável para a revisão e o estado de referência registrados.
- Antes da primeira alteração, reconfirme especificação, parecer humano, branch,
  commit, árvore de trabalho, resultado aprovado e transação Aberta [`Open`].
  Mudança material
  exige novo parecer humano e nova revisão integral.
- Se qualquer requisito obrigatório exigir inferência relevante, não implemente nenhum item; registre a lacuna e proponha o ajuste na especificação.
- Após ajuste aprovado da especificação, repita a análise integral antes de implementar.
- Em Precisa de esclarecimento [`Needs Clarification`], altere somente registros
  EKM e a correção normativa explicitamente aprovada.
- Reporte Precisa de esclarecimento [`Needs Clarification`] como bloqueio, nunca
  como implementação concluída.
- Preserve APIs, contratos e conhecimento normativo salvo autorização explícita.
- Considere toda a árvore de trabalho inicial como estado de referência.
- Abra ou identifique uma transação EKM antes de mudança relevante.
- Registre lacunas em vez de preenchê-las por suposição.
- Não transforme descoberta em decisão de produto, arquitetura, contrato, persistência, segurança, compatibilidade ou comportamento.
- Não reescreva versão de especificação já integrada à referência de produção; crie uma nova especificação relacionada.
- Não presuma que exista `EKM Gate` ou garantia automatizada sem ferramenta e política explicitamente implantadas.
- Não execute operações Git ou externas não autorizadas.
- Preserve alterações preexistentes e fora do escopo.
- O Líder Técnico (`Tech Lead`) revisa e produz parecer ou recorte corretivo; não implementa a
  correção.
- O Validador audita o processo; não repete a revisão de implementabilidade, não
  substitui o Líder Técnico e não corrige artefatos.

## Relatório obrigatório

Use a seção do seu papel na transação `EKM-CHG`. Informe marco versionado, resultado,
requisitos ou controles avaliados, arquivos, evidências, validações, pendências,
desvios, estados recomendados, comandos, resultados, operações Git ou externas,
artefatos temporários e reconciliação da árvore de trabalho. Não preencha a seção de
outro papel.
