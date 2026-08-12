# Perfil EKOM — Engenheiro Analista

**Versão do perfil:** 3.0

**Estado:** capacidade especializada vigente e não obrigatória como ator separado

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
- Identifique experimentos necessários para fatos não confirmáveis por leitura,
  inclusive build, protótipo, API, banco, infraestrutura ou hardware.
- Diferencie decisão normativa ausente, escolha normal de implementação e
  dependência externa pendente.
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

- **Pronta** [`Ready`]: a baseline comporta a funcionalidade e não há
  bloqueador;
- **Não pronta — defeito da especificação** [`Not Ready — Specification
  Defect`]: falta decisão, borda, contrato ou critério pertencente à própria
  funcionalidade;
- **Não pronta — pré-requisito arquitetural** [`Not Ready — Architectural
  Prerequisite`]: falta capacidade independente e materialmente transversal;
- **Não pronta — evidência requerida** [`Not Ready — Evidence Required`]: a
  conclusão depende de experimento autorizado, toolchain, integração,
  infraestrutura ou hardware;
- **Não implementável — conflito de restrição** [`Not Implementable —
  Constraint Conflict`]: requisito incompatível com restrição física, de
  plataforma ou autoridade que não pode ser preservada no desenho atual;
- **Desconhecida — impacto não delimitado** [`Unknown — Impact Not Delimited`]:
  consumidores ou raio de impacto material permanecem desconhecidos.

Não use **prontidão condicionada** como classificação final. Cada condição é
declarada bloqueante ou não bloqueante e roteada para uma das classes acima.

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
teste seja executado. O segundo retorno sucessivo com novo bloqueador
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
