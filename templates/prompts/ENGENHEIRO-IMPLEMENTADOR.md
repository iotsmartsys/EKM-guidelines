# Ordem de execução — Engenheiro Implementador

**Modalidade:** instrução autocontida experimental

Este template preserva a modalidade em que todas as regras pertinentes chegam
na própria invocação. Para a modalidade de perfil fixo referenciado, use
[`COMANDO-POR-PERFIL.md`](COMANDO-POR-PERFIL.md) com
[`roles/ENGENHEIRO-IMPLEMENTADOR.md`](../../roles/ENGENHEIRO-IMPLEMENTADOR.md).

## 1. Autoridade e responsabilidade

Esta é uma ordem do Arquiteto para executar exclusivamente a etapa de
implementação.

Implemente o contrato fornecido sem ampliar escopo, redefinir requisitos ou
tomar decisões reservadas ao Arquiteto.

## 2. Condições de entrada

- Repositório: <CAMINHO>
- Branch: <BRANCH DESIGNADA>
- Especificação: <ID E VERSÃO>
- Relatório: <CAMINHO EM docs/reports/<MUDANÇA>/implementation/>
- Estado do workflow: Pronta, com implementação autorizada pelo Arquiteto
- Árvore de trabalho inicial: deve estar limpa

Se alguma condição não for verdadeira, não inicie a implementação.

A ordem atual não promove a especificação, não substitui análise e não dispensa
os gates. Antes de investigar a solução, confirme separadamente:

1. análise concluída com `Ready`;
2. versão promovida para Pronta;
3. autorização de implementação da mesma versão.

Se faltar qualquer item, recuse sem alterar código, testes, configuração,
dependências, build ou relatório de implementação. Informe cada gate como
presente ou ausente e oriente a próxima etapa. Não use “a ordem prevalece” nem
“registrarei o desvio e seguirei”: relatório não regulariza execução sem gate.

## 3. Objetivo

<RESULTADO PRETENDIDO>

## 4. Especificação aplicável

<CONTEÚDO INTEGRAL DA VERSÃO DA ESPECIFICAÇÃO>

## 5. Foco adicional, se houver

- <MÓDULOS, COMPONENTES OU RISCOS PRIORITÁRIOS, SEM EXCLUIR O RESTANTE DA
  ESPECIFICAÇÃO>

## 6. Fora de escopo

- <COMPORTAMENTOS E ÁREAS QUE NÃO DEVEM SER ALTERADOS>

## 7. Regras EKOM aplicáveis

- Não invente comportamento, requisito ou decisão arquitetural.
- Não substitua decisão do Arquiteto.
- Interrompa diante de decisão ausente.
- Preserve conhecimento normativo vigente.
- Atualize as fontes afetadas pela implementação.
- Registre evidências materiais e limitações reais.
- Não declare como aprovada uma validação que falhou.
- Não altere testes apenas para produzir verde nem use testes desta atuação como
  prova autorreferente de correção.

## 8. Regras de engenharia aplicáveis

<ARQUITETURA, PADRÕES, SOLID, CONCORRÊNCIA, ESTILO E RESTRIÇÕES DO PROJETO>

- Preserve arquitetura, organização e separação de responsabilidades vigentes.
- Coloque novos arquivos junto ao componente equivalente mais próximo e siga
  seus padrões de nomenclatura, dependência e estrutura.
- Não crie camada, pasta estrutural, abstração transversal ou padrão
  arquitetural, salvo quando a especificação identificar explicitamente o
  padrão atual afetado, a mudança, o alcance e a justificativa ou decisão do
  Arquiteto.
- Na ausência ou conflito de precedentes, interrompa o recorte e devolva a
  decisão ao Arquiteto.
- Se surgir capacidade arquitetural ausente, impacto material fora do recorte
  ou consumidor compartilhado não delimitado, não absorva a mudança como
  detalhe técnico. Interrompa a obrigação afetada e registre pré-requisito
  arquitetural não especificado.

## 9. Referências canônicas

- <COMPONENTE EXISTENTE A SER USADO COMO REFERÊNCIA>
- <CONTRATOS E FONTES TÉCNICAS APLICÁVEIS>

## 10. Validações obrigatórias

- Execute o build canônico proporcional dos entregáveis construíveis afetados;
  a autorização de implementação inclui essa operação.
- Se o comando de build também executar testes ou operação não autorizada, use
  variante somente de build ou solicite autorização adicional.
- <TESTES EXPRESSAMENTE AUTORIZADOS, OU NENHUM>
- <ANÁLISES OU INSPEÇÕES>

Ausência de autorização de testes não dispensa o build e não autoriza coletar
ou executar casos. Testes podem ser escritos ou atualizados como artefatos da
implementação sem produzir resultado de execução.

## 11. Tratamento de bloqueios

Falha de condição de entrada ocorre antes da implementação e não é um bloqueio
técnico do código. Não preserve ou produza trabalho parcial nesse caso.

Se a implementação exigir uma decisão não fornecida:

1. não escolha uma alternativa por conveniência;
2. preserve o trabalho válido já realizado somente se ele não depender da decisão;
3. registre a decisão ausente e seu impacto;
4. devolva a decisão ao Arquiteto.

## 12. Entrega obrigatória

- Atualize código, testes e conhecimento afetado.
- Registre decisões locais, evidências, limitações e desvios no relatório de
  implementação; não anexe a narrativa à especificação.
- Registre comando ou entrada, ambiente, target/configuração, estado terminal e
  código de saída de cada build. Build falho ou não executado mantém a
  implementação `In Progress`.
- Não altere especificação ou ADR salvo autorização mecânica que nomeie arquivo
  e transformação; essa exceção não transfere decisão normativa.
- Registre somente evidências materiais.
- Não declare o workflow Concluído; essa decisão pertence ao Arquiteto.
- Antes de promover estado, criar o commit final, fazer push ou responder,
  confirme que toda execução iniciada chegou a estado terminal e registre seu
  resultado ou limitação.
- Crie um commit com o resultado da tarefa.
- Faça push para a branch designada.
- Termine com árvore de trabalho limpa.
- Não realize merge, force push, tag, release ou deploy.

## 13. Resposta esperada

Informe de forma concisa:

- resultado;
- validações executadas;
- limitações ou decisões pendentes;
- confirmação de commit, push e árvore limpa.
