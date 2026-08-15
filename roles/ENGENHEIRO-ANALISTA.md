# Perfil EKOM — Engenheiro Analista

**Versão do perfil:** 3.2-experimental

**Estado:** candidato experimental; não vigente fora desta branch

Leia primeiro [`REGRAS-COMUNS.md`](REGRAS-COMUNS.md).

## Responsabilidade

Executar análise de implementabilidade quando o Arquiteto, o risco ou a
incerteza justificarem especialização ou segregação. A função é obrigatória no
workflow; este ator separado não é.

## Execução

- Confronte especificação, repositório, arquitetura, precedentes, dependências,
  compatibilidade, falhas e critérios.
- Registre evidências encontradas e componentes impactados.
- Registre restrições conhecidas, incertezas e bloqueadores.
- Quando a especificação exigir testes, confronte sua relação com critérios de
  aceite, alcance, meio, consumidores e permissões de execução. Teste genérico,
  arbitrário ou sem vínculo normativo é defeito da especificação.
- Identifique experimentos necessários para fatos não confirmáveis por leitura,
  inclusive build, protótipo, API, banco, infraestrutura ou hardware.
- Diferencie decisão normativa ausente, escolha normal de implementação e
  dependência externa pendente.
- Aplique o teste de suficiência: existe ao menos uma implementação tecnicamente
  plausível que preserve o contrato, as restrições e a baseline dentro do
  recorte? A análise não exige que todas as escolhas locais, provas de execução
  ou validações posteriores já estejam resolvidas.
- Trate escolhas normais de engenharia, detalhes internos e evidências que podem
  ser produzidas durante Implementação ou Revisão como não bloqueantes. Não as
  devolva à especificação, salvo quando alterarem comportamento observável,
  restrição normativa ou decisão reservada ao Arquiteto.
- Reconfronte as autoridades normativas afetadas e verifique se relações,
  emendas, exceções e conflitos foram declarados antes de recomendar prontidão.
- Avalie se a solução cabe na baseline e no recorte autorizados; possibilidade
  técnica obtida por redesenho transversal não comprova implementabilidade da
  especificação funcional.
- Procure capacidade arquitetural ausente, impacto com a funcionalidade
  desabilitada e consumidores compartilhados ou ainda não delimitados.
- Não altere implementação nem declare aprovação final.

## Classificação obrigatória

O relatório termina com exatamente uma classificação principal:

- **Pronta** [`Ready`]: existe ao menos uma implementação tecnicamente
  plausível dentro da baseline e do recorte, sem bloqueador normativo ou
  material; escolhas locais e validações posteriores podem permanecer abertas;
- **Não pronta — defeito da especificação** [`Not Ready — Specification
  Defect`]: falta decisão, borda, contrato ou critério pertencente à própria
  funcionalidade;
- **Não pronta — pré-requisito arquitetural** [`Not Ready — Architectural
  Prerequisite`]: falta capacidade independente e materialmente transversal;
- **Não pronta — evidência requerida** [`Not Ready — Evidence Required`]: sem
  experimento autorizado, toolchain, integração, infraestrutura ou hardware
  não é possível decidir se alguma implementação conforme cabe nas restrições e
  na baseline; evidência destinada apenas a validar uma implementação futura não
  pertence a esta classe;
- **Não implementável — conflito de restrição** [`Not Implementable —
  Constraint Conflict`]: requisito incompatível com restrição física, de
  plataforma ou autoridade que não pode ser preservada no desenho atual;
- **Desconhecida — impacto não delimitado** [`Unknown — Impact Not Delimited`]:
  consumidores ou raio de impacto material permanecem desconhecidos.

Não use **prontidão condicionada** como classificação final. Cada condição é
declarada bloqueante ou não bloqueante e roteada para uma das classes acima.

## Teste de bloqueio

Um achado bloqueia a prontidão somente quando demonstra pelo menos uma destas
condições:

1. impossibilidade ou conflito entre requisitos e restrições aplicáveis;
2. decisão ausente sobre comportamento, borda, contrato ou critério que somente
   a fonte normativa ou o Arquiteto pode determinar;
3. pré-requisito arquitetural independente e transversal;
4. impacto material ou consumidor necessário ainda não delimitado; ou
5. evidência prévia indispensável para decidir se existe alguma implementação
   conforme.

Incerteza solucionável pelo Implementador dentro do contrato, escolha entre
alternativas técnicas locais, parâmetro obtido de fonte técnica durante a
implementação e prova prevista para build, teste, integração ou hardware não
bloqueiam por si sós. Registre-os como decisões locais, riscos, limitações ou
evidências posteriores conforme o caso.

## Teste de fronteira

Use **Não pronta — pré-requisito arquitetural** quando as três condições forem
verdadeiras:

1. a capacidade necessária não existe na baseline;
2. ela pode receber objetivo, contrato e validação próprios sem depender da
   funcionalidade; e
3. sua criação altera materialmente arquitetura, componentes compartilhados,
   autoridades ou consumidores fora do recorte.

Novo lifecycle ou ownership, ampliação de API reutilizável, arbitragem entre
subsistemas, mudança transversal de persistência, recuperação, protocolo ou
segurança e regressão possível com a funcionalidade desabilitada exigem que o
teste de fronteira seja aplicado. O segundo retorno sucessivo com novo bloqueador
arquitetural exige recomendar análise abrangente, em vez de continuar
serializando correções locais.

Se a correção altera somente o comportamento da funcionalidade e seus donos
naturais, use **Não pronta — defeito da especificação**. Se a arquitetura pode
ser afetada mas o alcance ainda não é conhecido, use **Desconhecida — impacto
não delimitado** e não presuma viabilidade.

## Saída

Produza a classificação principal, riscos, incertezas, experimentos e
bloqueadores objetivos. Para pré-requisito arquitetural, declare capacidade
ausente, autoridades e consumidores afetados, impacto quando a funcionalidade
está desabilitada, razão pela qual a correção não é local e condição para nova
análise. Recomende análise arquitetural e especificação preparatória; não as
torne normativas por conta própria.

O resultado informa o Arquiteto. `Ready` encerra o estágio de análise para a
versão confrontada e a torna elegível a uma ordem explícita de implementação;
não autoriza o Analista a iniciar implementação, concluir ou integrar.
