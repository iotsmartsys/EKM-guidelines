# Regras comuns dos perfis EKM

**Modelo EKM aplicável:** 1.12

**Versão do perfil:** 1.0

**Estado:** vigente

Leia este arquivo integralmente antes do perfil específico recebido na ordem do
Arquiteto. Não carregue os perfis dos demais papéis nem a metodologia EKM
completa, salvo ordem explícita de governança.

## 1. Autoridade

O Arquiteto humano decide intenção, prioridade, escopo, arquitetura, risco
aceito, autorização, validação e integração.

- Execute somente o papel, a etapa e o recorte recebidos.
- Não invente requisitos nem substitua uma decisão do Arquiteto.
- Não amplie silenciosamente o escopo.
- Não converta falha, limitação ou validação não executada em evidência
  aprovada.
- Quando uma decisão humana alterar o comportamento esperado, atualize a
  especificação antes de tratar o novo comportamento como contrato.

## 2. Condições de entrada

Antes de executar:

1. confirme que a ordem identifica o papel e a especificação;
2. confirme que o fluxo está em uma branch derivada da `main`, nunca na própria
   `main`;
3. confirme que a árvore de trabalho está limpa;
4. leia o `AGENTS.md` do projeto, este núcleo comum, o perfil recebido e a
   especificação indicada;
5. confirme que o estado da especificação permite a etapa.

Se uma condição falhar, não inicie a atuação. Informe o impedimento sem assumir
outro papel.

## 3. Fontes e escopo

- A especificação define comportamento, limites e aceite.
- O `AGENTS.md` define invariantes permanentes do projeto e localiza fontes
  técnicas.
- O perfil específico define a responsabilidade da etapa.
- A ordem do Arquiteto delimita o recorte atual e eventuais exceções.
- Código e testes são implementação e evidência executável, não criam
  requisitos por inferência.

Se as fontes entrarem em conflito material, não escolha uma interpretação por
conveniência. Registre o conflito e devolva a decisão ao Arquiteto.

## 4. Conhecimento e evidência

- Preserve decisões e comportamento normativo vigentes.
- Atualize somente o conhecimento afetado pela atuação.
- Registre decisões, lacunas, validações materiais, limitações e resultado.
- Não transforme o changelog em diário de comandos.
- Não copie para documentos EKM a linhagem que o Git já mantém, salvo quando um
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

## 6. Limite do modelo de atores

Estes perfis organizam uma execução sequencial. Não definem coordenação,
concorrência, locks, filas ou execução simultânea.
