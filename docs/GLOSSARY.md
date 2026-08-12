# Glossário do EKOM

| Termo | Significado canônico |
|---|---|
| EKOM | Engineering Knowledge Orchestration Model, nome oficial vigente desde a versão 2.0. |
| EKM | Engineering Knowledge Model, formulação histórica das versões 1.x; também prefixo legado compatível. |
| Especificação | Fonte única da verdade para o comportamento pretendido, seus limites, estados e critérios de aceite. |
| Versão normativa integral | Unidade atômica de cobertura para resultados formais do ciclo; nenhum elemento normativo aplicável pode ser omitido da promoção. |
| Foco adicional | Prioridade, dúvida ou área de atenção indicada na ordem; orienta profundidade ou sequência sem reduzir a especificação. |
| Atuação parcial | Diagnóstico, investigação ou execução explicitamente limitada que não promove o estado formal representativo da versão inteira. |
| Fonte única da verdade | Autoridade normativa única por comportamento; não exige que todo conhecimento esteja em um único arquivo. |
| Confronto de autoridade normativa | Verificação orientada por impacto que localiza as fontes vigentes dos elementos afetados, classifica a relação da mudança e impede prontidão diante de conflito, omissão ou alcance sem decisão. |
| Baseline arquitetural | Conjunto vigente de responsabilidades, contratos, lifecycle, precedentes e capacidades contra o qual a implementabilidade é avaliada. |
| Pré-requisito arquitetural | Capacidade ausente, independente da funcionalidade e materialmente transversal que precisa preparar e validar uma nova baseline antes da implementação funcional. |
| Especificação preparatória | Especificação própria da capacidade arquitetural que habilita uma ou mais funcionalidades sem incorporar a política particular de cada consumidora. |
| `Depends On` | Relação de dependência: a especificação consumidora não pode ser implementada antes do estado material exigido da fonte referenciada. |
| `Enables` | Relação inversa pela qual uma preparação fornece capacidade arquitetural a uma especificação consumidora. |
| Não pronta — defeito da especificação | Classificação de análise para decisão, borda, contrato ou critério ausente que ainda pertence à própria funcionalidade. |
| Não pronta — pré-requisito arquitetural | Classificação bloqueante usada quando a baseline não oferece capacidade independente e transversal necessária à funcionalidade. |
| Não pronta — evidência requerida | Classificação bloqueante quando a conclusão depende de experimento, toolchain, integração, infraestrutura ou hardware autorizado. |
| Não implementável — conflito de restrição | Classificação para incompatibilidade do desenho com restrição física, de plataforma ou autoridade que não pode ser preservada. |
| Desconhecida — impacto não delimitado | Classificação bloqueante quando consumidores ou raio de impacto material não foram suficientemente identificados. |
| Plano de controle | Função exercida pela especificação ao determinar recorte, passagens, critérios e relações do pipeline. |
| Orquestração | Coordenação do ciclo de engenharia pela especificação entre humanos, agentes de IA, automações, implementação, validação, evidências e evolução. |
| Pipeline | Ciclo governado de rascunho e análise, prontidão, implementação, validação, conclusão e aprendizado; challenge é consultivo. |
| Fonte derivada | Código, teste, relatório ou automação que implementa, evidencia ou consome uma especificação sem criar requisito. |
| ADR | Registro de decisão arquitetural transversal ou durável, com contexto, alternativas, decisão e consequências; não substitui o contrato comportamental da especificação. |
| Relatório | Registro histórico e não normativo dos fatos, achados e evidências de uma atuação. |
| Roteamento documental | Associação obrigatória entre classe de conhecimento, destino, autoridade de escrita e ciclo de vida. |
| Mapa de conhecimento | Fonte navegacional que combina índice de autoridade, árvore hierárquica, relações materiais e lacunas sem duplicar contratos. |
| Árvore de conhecimento | Visão textual da contenção, composição e responsabilidade entre alvos, domínios e componentes. |
| Diagrama de relações | Visão Mermaid pequena das conexões materiais entre alvos ou domínios separados. |
| Evidência | Resultado observável e terminal capaz de sustentar ou limitar uma conclusão. |
| Ator | Pessoa ou agente que executa uma capacidade delimitada e registra fatos e evidências sem assumir autoridade do Arquiteto. |
| Arquiteto | Autoridade humana final sobre intenção, arquitetura, risco aceitável, relevância das críticas, suficiência das evidências, aprovação, conclusão ou reabertura e integração. |
| Análise de implementabilidade | Função obrigatória anterior à implementação; registra evidências, impactos, restrições, incertezas, experimentos e bloqueadores, sem exigir ator separado. |
| Challenge | Crítica consultiva e proporcional ao risco; informa o Arquiteto sem aprovar ou reprovar o workflow. |
| Evidência material | Fato observável como diff, build, execução, log, teste, integração real, relatório, decisão humana ou defeito posterior. |
| Concluída [`Done`] | Estado determinado exclusivamente pelo Arquiteto quando evidências e risco residual são considerados suficientes. |
| Reaberta [`Reopened`] | Especificação concluída devolvida ao ciclo pelo Arquiteto diante de nova necessidade ou evidência material. |
| `EKOM-CHG` | Namespace recomendado para novas transações de mudança desde o EKOM 2.0. |
| `EKOM-GAP` | Namespace recomendado para novas lacunas de conhecimento desde o EKOM 2.0. |
| `EKM-CHG` / `EKM-GAP` | Namespaces legados aceitos para compatibilidade com adoções EKM 1.x. |
