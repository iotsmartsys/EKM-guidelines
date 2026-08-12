# ADR-0008 — Build é verificação intrínseca da implementação

**Estado:** Aceita

**Data:** 2026-08-12

**Versão resultante:** EKOM 3.6

## Contexto

Durante a promoção da v0.11 de deep sleep do `IoTSmartLink15.4`, a
especificação declarava que não autorizava build, testes ou hardware. Depois da
promoção, o Arquiteto precisou esclarecer que o build deveria ocorrer na
implementação e que somente a execução de testes permanecia sem autorização.

Tratar o build ordinário como permissão particular de cada especificação
duplica uma regra de engenharia, aumenta a chance de contratos funcionais
divergirem e obriga o Autor a governar uma responsabilidade própria do
Implementador. Build e teste também possuem efeitos probatórios diferentes:
build confronta construção do artefato; teste executa um oráculo comportamental.

## Decisão

A autorização de implementação de mudança em artefato construível autoriza e
exige o build canônico e proporcional dos entregáveis materialmente afetados.
Não é necessária autorização adicional nem cláusula na especificação
funcional.

O projeto localiza em `AGENTS.md` ou fonte técnica equivalente os comandos,
targets, configurações e restrições admitidos. O Implementador seleciona o
menor conjunto capaz de construir os entregáveis afetados; componente
compartilhado inclui seus consumidores materiais quando a política local assim
os identifica.

Build significa a construção não operacional do artefato — configuração,
compilação, link, empacotamento ou verificação equivalente do ecossistema. Ele
não autoriza, por si só:

- coleta ou execução de testes;
- flash, monitor ou uso de hardware;
- deploy, release, publicação ou integração;
- instalação persistente de toolchain, uso de credencial, serviço pago ou
  alteração externa necessária ao comando.

Quando um comando de build também executar testes ou outra operação não
autorizada, o Implementador usa uma variante somente de build. Se não houver
separação segura, interrompe e solicita autorização para a operação adicional.

O resultado registra comando ou entrada canônica, ambiente relevante, alvo,
estado terminal e código de saída. Build falho é falha observada: o
Implementador corrige causas dentro do recorte e repete a verificação. Se o
build continuar falho ou não puder executar por ambiente, dependência ou
autoridade ausente, a implementação não pode ser declarada concluída; permanece
`In Progress` com a limitação explícita, salvo decisão posterior do Arquiteto
sobre suficiência e risco.

Mudança exclusivamente documental, repositório sem artefato construível ou
operação para a qual não exista build canônico não exige comando artificial.
Uma exceção ao build ordinário precisa ser explícita e registrada pelo
Arquiteto; o resultado continua `Not Executed`, nunca “aprovado”.

## Fronteira com a especificação

A especificação descreve comportamento, limites e evidências funcionais
específicas. Ela não repete a autorização do build ordinário. Pode declarar
somente uma matriz excepcional, um artefato adicional material ao aceite ou
uma restrição que a regra geral e as fontes locais não consigam determinar.

Testes escritos ou atualizados como parte da implementação continuam sendo
artefatos de código. Sua coleta ou execução não é inferida da autorização de
implementação e depende da política local e da ordem do Arquiteto.

## Consequências

- toda implementação de código construível confronta compilação e link antes
  de alegar conclusão;
- especificações funcionais deixam de repetir permissão ou proibição do build
  ordinário;
- build falho ou não executado permanece evidência explícita;
- execução de testes e operações físicas continua separada e proporcional;
- comandos híbridos não ampliam silenciosamente a autoridade da implementação;
- projetos adotantes migram deliberadamente para EKOM 3.6.

## Alternativas rejeitadas

- exigir que cada especificação autorize build foi rejeitado por duplicar uma
  responsabilidade permanente do Implementador;
- tratar build e teste como uma única permissão foi rejeitado porque possuem
  efeitos, custos e riscos distintos;
- tornar toda matriz de targets universal foi rejeitado porque o conjunto
  afetado depende do projeto e da mudança;
- permitir alegação de implementação concluída sem build disponível foi
  rejeitado porque ausência de evidência não comprova construção do artefato.

## Critério de reavaliação

Reavaliar se a regra induzir builds excessivos sem relação com o delta, se
ecossistemas sem etapa de construção forem tratados artificialmente ou se
comandos híbridos continuarem executando testes ou operações externas sem
autorização.
