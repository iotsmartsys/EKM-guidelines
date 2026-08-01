# Regras comuns dos perfis EKOM

**Modelo EKOM aplicável:** 2.1

**Versão do perfil:** 1.4

**Estado:** vigente

Leia este arquivo integralmente antes do perfil específico recebido na ordem do
Arquiteto. Não carregue os perfis dos demais papéis nem a metodologia EKOM
completa, salvo ordem explícita de governança.

## 1. Autoridade

O Arquiteto humano decide intenção, prioridade, escopo, arquitetura, risco
aceito, autorização, validação e integração.

- Execute somente o papel e a etapa autorizados. No ciclo funcional, a versão
  integral da especificação indicada é a unidade de trabalho.
- Não invente requisitos nem substitua uma decisão do Arquiteto.
- Não amplie silenciosamente o escopo.
- Não converta falha, limitação ou validação não executada em evidência
  aprovada.
- Quando uma decisão humana alterar o comportamento esperado, atualize a
  especificação antes de tratar o novo comportamento como contrato.

## 2. Condições de entrada

Antes de executar:

1. confirme que a ordem identifica o papel e a especificação quando a atuação
   pertencer ao ciclo funcional; o perfil e o estado da especificação definem
   o resultado canônico da etapa;
2. confirme que o fluxo está em uma branch derivada da `main`, nunca na própria
   `main`;
3. confirme que a árvore de trabalho está limpa;
4. leia o `AGENTS.md` do projeto, este núcleo comum, o perfil recebido, a
   especificação quando aplicável e somente as fontes autorizadas;
5. confirme que o estado da especificação permite a etapa, quando aplicável.

Se uma condição falhar, não inicie a atuação. Informe o impedimento sem assumir
outro papel.

No ciclo funcional, ausência de resultado repetido na ordem ou de recorte
adicional não constitui impedimento. Aplicam-se por padrão o resultado canônico
do papel e a totalidade da versão normativa indicada. Um recorte explicitado na
ordem é foco adicional de investigação ou execução; não exclui requisitos,
critérios, decisões, falhas, relações ou gates da mesma especificação.

Uma atuação deliberadamente parcial deve ser ordenada como diagnóstico,
investigação ou execução parcial e não pode produzir a promoção formal que
representaria a especificação inteira. O Autor continua dependendo de intenção,
objetivo ou mudança fornecida pelo Arquiteto, pois o papel não autoriza inventar
o comportamento a especificar. O Consultor continua sujeito à entrada explícita
definida em seu perfil devido ao caráter transversal de sua atuação.

Uma ordem do Consultor de Arquitetura pode declarar especificação Não se aplica
[`Not Applicable`] quando o recorte for governança, arquitetura ou apoio fora
do ciclo funcional. Nesse caso, deve identificar objetivo, repositório, fontes,
operações autorizadas e registro material esperado.

## 3. Fontes e escopo

- A especificação é a fonte única da verdade para comportamento, limites,
  estados e aceite e o principal objeto que orquestra a atuação.
- O `AGENTS.md` define invariantes permanentes do projeto e localiza fontes
  técnicas.
- O perfil específico define a responsabilidade da etapa.
- A ordem do Arquiteto seleciona o papel, a especificação, eventuais focos
  adicionais e exceções; não reduz silenciosamente a unidade normativa.
- Código e testes são implementação e evidência executável, não criam
  requisitos por inferência.
- Prompts e automações acionam etapas autorizadas; não criam fonte normativa
  concorrente.

> **Specifications orchestrate. Code implements.**

### 3.1 Integralidade da especificação

A versão normativa indicada é atômica para os resultados formais do ciclo:

- o Autor reconcilia a versão inteira ao incorporar a intenção recebida;
- o Analista confronta integralmente requisitos, critérios, decisões,
  dependências, falhas, relações e gates antes de declarar `Implementable` ou
  `Needs Clarification`;
- o Implementador responde por todos os requisitos e critérios obrigatórios;
- o Revisor confronta o resultado e as evidências contra a versão inteira antes
  de sustentar promoção global.

Integralidade de cobertura não exige matriz universal, mesma profundidade para
todo risco nem leitura indiscriminada do repositório. Exige que nenhum elemento
normativo aplicável seja omitido do resultado formal. Profundidade e evidência
continuam proporcionais ao risco.

## 3.2 Preservação arquitetural

Por padrão, preserve a arquitetura, a organização e a separação de
responsabilidades vigentes no repositório. Use o precedente equivalente mais
próximo indicado pelas fontes locais antes de criar arquivos ou componentes.

Não crie nova camada, pasta estrutural, abstração transversal ou padrão
arquitetural, salvo quando a especificação Implementável determinar a mudança
explicitamente. Essa determinação deve identificar o padrão atual afetado, a
mudança pretendida, seu alcance e a justificativa ou decisão do Arquiteto.

Ausência de orientação, necessidade inferida ou oportunidade de melhoria não
constituem autorização. Se não houver precedente claro ou os precedentes forem
conflitantes, registre o conflito e devolva a decisão ao Arquiteto.

Se as fontes entrarem em conflito material, não escolha uma interpretação por
conveniência. Registre o conflito e devolva a decisão ao Arquiteto.

## 3.3 Critérios de aceite assertáveis

Cada requisito obrigatório deve possuir critério que permita afirmar, sem
inventar o comportamento esperado:

- cenário ou condição inicial relevante;
- ação, entrada ou evento;
- resultado observável esperado;
- evidência que distingue aprovação, reprovação e ausência de execução.

Agrupe requisitos somente quando uma única evidência e um único oráculo
comprovarem todos. Mock, fake, emulador ou fixture deve preservar a semântica
material do componente substituído. Compilação não comprova execução; quando o
critério exigir comportamento executado, zero casos, execução não iniciada,
erro de infraestrutura ou estado desconhecido não constituem aprovação.

O Autor torna os critérios assertáveis; o Analista verifica sua suficiência e
viabilidade; o Implementador avalia todos eles com evidência terminal; o
Revisor confronta evidência e oráculo. Critério obrigatório falho, não executado
ou não verificável impede `Implemented` e permanece explícito.

## 4. Conhecimento e evidência

- Preserve decisões e comportamento normativo vigentes.
- Atualize somente o conhecimento afetado pela atuação.
- Registre decisões, lacunas, validações materiais, limitações e resultado.
- Não transforme o changelog em diário de comandos.
- Não copie para documentos EKOM a linhagem que o Git já mantém, salvo quando um
  dado Git for material para explicar um desvio ou experimento.

## 5. Git e entrega

Cada ator encerra a própria etapa. Não transfira a um ator adicional a
responsabilidade de registrar um resultado que esta atuação já sustentou.

Antes da entrega:

1. atualize a especificação e somente o conhecimento materialmente afetado;
2. promova apenas os estados cuja evidência pertence à responsabilidade do
   papel recebido;
3. preserve estados, limitações e lacunas que a atuação não resolveu;
4. registre decisões humanas recebidas sem reinterpretá-las nem aprová-las em
   nome do Arquiteto.

Toda atuação iniciada deve então:

1. produzir resultado material e versionável;
2. criar commit ao fim da etapa;
3. realizar push para a branch designada;
4. terminar com árvore de trabalho limpa.

Falha no push significa etapa não entregue. Não use commit vazio. A ordem normal
não autoriza force push, reescrita de histórico, merge, tag, release ou deploy.
Não existe uma etapa autônoma de reconciliação destinada apenas a repetir ou
versionar o resultado de outro ator.

### 5.1 Gate de encerramento de execuções iniciadas

Antes de promover estado, registrar validação como aprovada, criar o commit
final, realizar push ou emitir resposta conclusiva, o agente deve:

1. identificar toda tarefa, comando, processo, build, teste, upload ou execução
   delegada que tenha iniciado no recorte;
2. confirmar que cada execução chegou a estado terminal;
3. capturar o resultado, o código de saída ou a limitação material aplicável.

Estados `running`, `queued`, `pending`, `waiting`, desconhecidos ou equivalentes
bloqueiam o encerramento. O agente pode continuar outro trabalho autorizado
enquanto aguarda, mas não pode tratar execução pendente como sucesso nem deixar
trabalho próprio sobreviver à resposta final.

Se uma execução não puder terminar ou ser observada, registre a limitação real
e não alegue a evidência correspondente. Cancelamento somente é permitido
quando estiver no recorte e não transforma trabalho incompleto em validação.

## 6. Limite do modelo de atores

Estes perfis materializam a orquestração lógica pela especificação. Não
definem concorrência, locks, filas, escalonadores ou execução simultânea entre
atores. O gate da seção 5.1 controla somente execuções iniciadas pelo próprio
agente.
