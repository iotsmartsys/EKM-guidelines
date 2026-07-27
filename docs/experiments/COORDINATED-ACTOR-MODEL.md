# Protocolo experimental de execução por etapas

**Modelo EKM aplicável:** 1.10

**Versão do protocolo:** 0.8

**Estado:** experimental

## 1. Hipótese

Uma mudança pode ser executada com mais clareza e menor carga operacional
quando cada etapa recebe um objetivo delimitado, lê o estado vigente da
especificação e entrega um resultado versionado, sem formulários de handoff nem
duplicação do histórico Git.

## 2. Autoridade e acionamento

O Arquiteto humano é a autoridade final. Cada etapa começa por prompt ou comando
de pipeline emitido pelo Arquiteto. Essa ordem define o trabalho autorizado.

O agente pode recomendar, alertar e bloquear sua própria execução diante de
lacuna factual, mas não pode sobrepor uma decisão do Arquiteto, mudar requisitos
ou expandir o recorte.

## 3. Etapas

| Etapa | Entrada mínima | Saída mínima |
|---|---|---|
| Autoria | objetivo e decisões do Arquiteto | especificação Proposta e Pendente de revisão |
| Análise | ordem do Arquiteto e especificação Proposta | Implementável ou Precisa de esclarecimento |
| Implementação | ordem do Arquiteto e especificação Implementável | implementação, conhecimento atualizado e evidências |
| Revisão opcional | ordem do Arquiteto e resultado implementado | achados e recomendação |
| Integração | decisão do Arquiteto | entrega aceita e estados reconciliados |

As etapas formam uma sequência lógica. O protocolo não cria coordenação,
locking, filas ou verificações de concorrência.

## 4. Contrato comum de execução

Toda etapa de agente:

1. verifica que o fluxo está em uma branch derivada da `main`, nunca diretamente
   na `main`;
2. verifica que a árvore de trabalho está limpa antes de começar;
3. lê `AGENTS.md`, a especificação aplicável e a transação relacionada;
4. executa apenas a etapa solicitada;
5. atualiza somente os artefatos necessários;
6. registra evidências materiais e limitações;
7. cria commit e realiza push;
8. confirma a árvore limpa ao terminar.

O agente não copia SHA, branch, comandos de leitura ou mensagem de commit para
a documentação. O Git mantém essa trilha.

Falha no push impede considerar a etapa entregue. Force push, merge, tag,
release e deploy exigem ordem específica.

## 5. Análise

A análise responde a uma pergunta: é possível implementar o recorte sem tomar
uma decisão reservada ao Arquiteto?

Uma lista curta relacionando requisito, evidência e eventual decisão ausente é
suficiente. Matrizes extensas são usadas apenas quando a complexidade do caso
as tornar úteis.

Ao identificar uma lacuna bloqueante, o Analista pode concluir Precisa de
esclarecimento [`Needs Clarification`] sem continuar uma busca exaustiva.
Bloqueios materiais já encontrados devem ser agrupados no mesmo retorno.

## 6. Implementação

A implementação só começa com:

- ordem do Arquiteto para implementar;
- especificação Implementável [`Implementable`];
- branch de trabalho derivada da `main`;
- árvore de trabalho limpa.

O Implementador produz código, testes, conhecimento atualizado e evidências
proporcionais ao risco. Uma decisão necessária não prevista retorna ao
Arquiteto.

## 7. Revisão e fechamento

Revisão técnica adicional e validação de integridade não são papéis
obrigatórios. O Arquiteto as solicita quando agregarem confiança ao caso.

A mudança é encerrada quando:

- o recorte autorizado foi entregue por commit e push;
- as evidências materiais estão registradas;
- as fontes afetadas estão atuais;
- lacunas restantes estão explícitas.

O estado da entrega da especificação registra separadamente se houve
integração. O fechamento não repete o histórico Git nem exige um commit
posterior de reconciliação.

## 8. Evidência do experimento

O protocolo 0.8 preserva a simplificação introduzida pelo protocolo 0.7 e exige
que o fluxo comece em uma branch derivada da `main`.

O protocolo 0.7 substituiu os checkpoints, declarações
de prontidão, matrizes universais, registros manuais de SHA e papéis obrigatórios
do protocolo 0.6.

O protocolo anterior e sua execução permanecem recuperáveis no histórico Git e
nos registros:

- `COORDINATED-ACTOR-MODEL-RUN-001.md`;
- `SMARTHOME-DEVICEAPI-COORDINATED-ACTORS.md`.

Esses registros são evidência histórica e não definem o fluxo vigente.
