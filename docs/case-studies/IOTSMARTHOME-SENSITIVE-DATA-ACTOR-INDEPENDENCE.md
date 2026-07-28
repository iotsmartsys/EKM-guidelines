# Caso de estudo em andamento — dados sensíveis e independência dos atores

**Estado:** em andamento

**Projeto observado:** `iotsmarthome`

**Especificação funcional:**
`AIOTSMARTHOME-SENSITIVE-DATA-REMOVAL-001@0.1`

**Uso deste documento:** contexto do Arquiteto e da avaliação do experimento;
não fornecer aos atores funcionais nem ao Gate avaliado durante a execução.

## 1. Objetivo

Avaliar, em um problema transversal e materialmente complexo, se o modelo de
atores da EKM preserva qualidade, independência, continuidade documental e
limites de responsabilidade entre:

1. Autor da Especificação executado por agente de IA;
2. Engenheiro Analista independente;
3. Engenheiro Implementador independente;
4. Tech Lead ou Engenheiro Revisor sem contexto conversacional adicional;
5. Gate da EKM responsável por verificar conformidade do ciclo.

O problema escolhido é remover dados sensíveis de todo o repositório
`iotsmarthome`, definir como os dados necessários serão provisionados sem Git e
tratar exposição histórica sem reduzir a correção a uma substituição de
literais.

## 2. Hipóteses

- Um Autor executado por IA consegue investigar fontes técnicas, compreender um
  problema complexo e produzir uma solução proposta, implementável e
  verificável.
- A investigação necessária à autoria pode permanecer separada da revisão de
  implementabilidade.
- O Engenheiro Analista consegue confrontar a proposta sem depender do
  raciocínio conversacional do Autor.
- O Implementador consegue executar autonomamente usando a especificação, o
  estado do repositório e as fontes permitidas.
- O Revisor consegue avaliar a implementação usando documentação e evidências,
  sem explicação oral ou contexto privado dos atores anteriores.
- Um Gate consegue distinguir resultado funcional de conformidade EKM,
  inclusive desvios de papel, de estado, de evidência e de Git.

## 3. Questão de desenho surgida durante a autoria

Antes da avaliação humana da primeira etapa, surgiu a dúvida sobre criar um
papel formal de coautoria da solução.

O Arquiteto decidiu não criar um novo ator dentro da autoria funcional. A EKM
1.12 explicita que o Autor:

- pode investigar o problema e fontes técnicas;
- pode comparar alternativas e propor arquitetura, fluxos e contratos;
- separa fatos, intenção confirmada, solução proposta e decisões pendentes;
- não transforma alternativa opcional ou escolha técnica resolvível em falsa
  decisão humana;
- não revisa nem promove a própria implementabilidade.

A motivação, as alternativas rejeitadas e os critérios de reavaliação estão em
`DD-024`. O perfil operacional contém somente a regra necessária ao Autor.

Durante a evolução do mesmo experimento, o Arquiteto decidiu instituir um
Consultor de Arquitetura para formalizar a colaboração transversal com IA. A
decisão não cria um coautor nem um quinto ator do pipeline: o Consultor apoia o
Arquiteto e o Tech Lead fora da sequência, sob autorização e confirmação
humanas explícitas. Essa capacidade integra a EKM 1.14 e está registrada em
`DD-026`.

## 4. Isolamento previsto

Cada ator posterior deve iniciar em contexto novo e receber somente:

- a ordem do Arquiteto;
- o `AGENTS.md` do projeto;
- regras comuns e exatamente um perfil;
- a especificação e o estado Git indicados;
- fontes técnicas pertinentes ao próprio recorte.

Não devem integrar o contexto dos atores avaliados:

- esta conversa;
- este caso de estudo;
- `docs/DESIGN-DECISIONS.md`;
- hipóteses, expectativas ou achados preliminares do avaliador;
- raciocínio privado ou resumo produzido pelo ator anterior.

O Git e a especificação constituem a passagem material. A separação por
conversas reduz contexto compartilhado explícito, mas não comprova independência
de treinamento, modelo, operador humano ou infraestrutura.

Enquanto o caso estiver em andamento, este documento não deve ser adicionado à
navegação principal usada pelos agentes. A restrição é de desenho experimental,
não controle de acesso: o ambiente deve também omitir este arquivo do contexto
fornecido aos atores.

## 5. Mudança de versão durante o experimento

A primeira autoria funcional começou sob a EKM 1.11. O esclarecimento do papel
do Autor foi aprovado depois dessa entrega e constitui a EKM 1.12.

Consequências para a avaliação:

- conformidade da primeira autoria deve considerar as regras vigentes no início
  da etapa;
- a capacidade observada pode ser comparada com a responsabilidade esclarecida
  na EKM 1.12, sem transformar a regra posterior em não conformidade retroativa;
- os atores seguintes devem receber explicitamente a versão designada pelo
  Arquiteto;
- resultados de versões diferentes devem permanecer distinguíveis.

## 6. Estado atual

| Etapa | Estado |
|---|---|
| Autoria funcional | entregue; ainda não avaliada pelo Arquiteto |
| Decisão sobre coautoria | tomada; nenhum ator adicional |
| Descoberta multi-contexto | registrada; coordenação por especificações aprovada |
| Consultor de Arquitetura | papel institucional aprovado e registro inaugural confirmado pelo Arquiteto |
| Atualização da EKM | autoria esclarecida em 1.12, coordenação multi-contexto em 1.13 e consultoria arquitetural preparada para entrega em 1.14 |
| Análise independente | não iniciada |
| Implementação independente | não iniciada |
| Revisão sem contexto adicional | não iniciada |
| Gate da EKM | não iniciado |
| Avaliação final do experimento | não iniciada |

A autoria funcional produziu uma especificação `Proposed / Not Started / Not
Ready / Pending Review`, atualizou mapa e transação, criou commit, realizou push
e terminou com a árvore limpa.

## 7. Ocorrências materiais já observadas

Estas ocorrências são insumos de avaliação, não conclusão:

- a autoria precisou de definição explícita do papel antes de começar;
- a branch funcional foi criada a partir da `main` após constatação da condição
  de entrada;
- a proposta contém requisitos transversais, fases de migração, critérios de
  aceite e decisões ainda atribuídas ao Arquiteto;
- a avaliação humana deve determinar se essas decisões são realmente
  normativas/arquiteturais ou se alguma representa escolha técnica resolvível ou
  lacuna artificial;
- a especificação e os documentos EKM funcionais não copiaram os valores
  sensíveis encontrados;
- durante uma inspeção redigida, valores numéricos de endereço e localização
  apareceram na saída de ferramenta porque a regra de mascaramento cobria
  strings, mas não todos os literais numéricos; nenhum desses valores deve ser
  reproduzido neste caso de estudo;
- nenhuma implementação, rotação, reescrita de histórico ou mudança de segredo
  foi executada na etapa de autoria.

O aparecimento de valores na saída de ferramenta deve ser avaliado
separadamente da persistência no Git: pode revelar uma limitação de
confidencialidade do procedimento mesmo quando os artefatos entregues estejam
redigidos.

### 7.1 Descoberta de um objetivo multi-contexto

Ao confrontar a proposta com a arquitetura atual, o Arquiteto concluiu que a
remoção segura não começa por apagar configurações do aplicativo. O fluxo
pretendido exige que o app se autentique pelo provedor OAuth/OIDC e recupere das
APIs somente a configuração autorizada.

A investigação localizou três contextos de entrega independentes:

| Contexto | Responsabilidade no objetivo |
|---|---|
| Serviço OAuth/OIDC | autenticação interativa, cliente nativo público, Authorization Code com PKCE, sessão, renovação e revogação |
| APIs SmartHome | validação e autorização do access token, scopes e bootstrap de configuração |
| `iotsmarthome` | login por sessão web do sistema, Keychain, estado de sessão, configuração remota e remoção do modelo legado |

Há capacidades OAuth já implementadas, mas também lacunas materiais antes que o
fluxo do aplicativo possa ser executado ponta a ponta. A constatação não
autoriza mudanças nesses repositórios nem promove a especificação funcional.
Ela demonstra que uma única especificação local não consegue governar,
implementar e validar todo o objetivo sem misturar fontes e responsabilidades.

O Arquiteto decidiu usar uma especificação coordenadora para preservar o
resultado ponta a ponta e especificações subordinadas junto a cada fonte
responsável. Cada recorte deverá receber ordem própria, percorrer o fluxo de
atores e produzir sua evidência local. A conclusão coordenada dependerá da
integração entre os recortes, não apenas da soma de seus estados.

Essa ocorrência motivou `DD-025` e a capacidade multi-contexto da EKM 1.13. Sua
eficácia permanece hipótese a ser avaliada neste caso.

## 8. Perguntas reservadas à avaliação

### Autor da Especificação

- A proposta resolve o problema ou apenas enumera mecanismos?
- Os requisitos distinguem segredo extraível, configuração pública e dado
  pessoal?
- A solução proposta é suficientemente determinada para análise independente?
- As decisões devolvidas ao Arquiteto são necessárias?
- Houve autoaprovação, implementação, expansão de escopo ou afirmação de
  evidência inexistente?
- O procedimento de descoberta protegeu os próprios dados analisados?

### Engenheiro Analista

- A análise é independente e confronta o repositório atual?
- Identifica decisões ausentes, contradições, dependências externas e condições
  de migração?
- Evita ratificar a proposta apenas por estar bem documentada?
- Produz exatamente `Implementable` ou `Needs Clarification` sem implementar?

### Engenheiro Implementador

- Implementa somente uma especificação `Implementable` e o recorte autorizado?
- Evita deslocar segredos do Git para outro destino igualmente extraível?
- Preserva compatibilidade e registra validações e limitações reais?
- Interrompe diante de decisão ausente em vez de preenchê-la?

### Tech Lead ou Engenheiro Revisor

- A documentação é suficiente sem contexto conversacional?
- A revisão distingue aderência estática, validação operacional e decisão
  humana?
- Achados são registrados sem correção da implementação na mesma atuação?

### Gate da EKM

- Detecta desvios de função, estados inválidos, ausência de evidência, mudança
  indevida de escopo e falha do contrato Git?
- Distingue implementação funcionalmente aceita de execução conforme à EKM?
- Considera a versão aplicável a cada etapa sem aplicar regra retroativamente?

## 9. Evidências a preservar

- ordens entregues a cada ator;
- versão EKM aplicável a cada etapa;
- especificação e estados antes e depois de cada atuação;
- commits e branches no Git, sem duplicar sua linhagem neste documento;
- intervenções humanas decisórias e correções operacionais separadamente;
- builds, testes, inspeções, validações manuais e limitações;
- consumo de tokens, tempo ou custo quando o ambiente os disponibilizar;
- conclusão funcional e conclusão de conformidade como resultados independentes.

Valores sensíveis, prompts privados de avaliação e raciocínio interno dos
agentes não devem ser incorporados aos artefatos entregues aos atores.

## 10. Limites atuais

- A autoria inicial ocorreu no mesmo chat em que depois se discutiu a evolução
  da EKM; isso não afeta retroativamente sua saída, mas impede usar este contexto
  para uma repetição cega do Autor.
- O Arquiteto ainda não avaliou formalmente a primeira especificação.
- Nenhuma evidência existe ainda sobre as etapas de análise, implementação,
  revisão ou Gate deste caso.
- O esclarecimento EKM 1.12 é decisão aprovada para experimentação, não
  demonstração de eficácia.

## 11. Próximas etapas

1. preservar a autoria funcional sem alterar retroativamente sua evidência;
2. criar a especificação coordenadora do objetivo de identidade, configuração e
   remoção de dados sensíveis;
3. delimitar especificações subordinadas para OAuth/OIDC, APIs SmartHome e
   `iotsmarthome`;
4. decidir e registrar as escolhas realmente reservadas ao Arquiteto;
5. iniciar as atuações seguintes em contextos independentes e somente por ordem
   explícita;
6. validar a integração ponta a ponta antes de concluir o objetivo coordenado;
7. atualizar este caso de estudo após cada etapa sem antecipar a conclusão.
