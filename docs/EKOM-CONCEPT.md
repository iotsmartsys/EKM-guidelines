# O que é o EKOM

## Definição operacional

Engineering Knowledge Orchestration Model (EKOM) é um modelo de orquestração
de engenharia no qual a especificação governa a execução dos agentes de IA,
enquanto o Arquiteto mantém autoridade sobre decisões, riscos, validação e
conclusão do workflow.

> **Specifications orchestrate. Code implements.**

Seu objetivo é permitir que uma solução seja especificada, implementada,
documentada e entregue sem que o Arquiteto precise executar diretamente o
desenvolvimento. Isso é execução amplamente delegada, não delegação do
julgamento arquitetural.

## Problema tratado

Projetos preservam código com mais facilidade que intenção, decisões, limites,
riscos aceitos e evidências. Git recupera versões de arquivos, mas não garante
a recuperação do porquê. Conversas, prompts, relatórios e testes ajudam, porém
não são fontes normativas estáveis por si sós.

O EKOM torna a especificação o plano de controle capaz de declarar:

- comportamento, escopo, limites e critérios de aceite;
- decisões confirmadas, incertezas, lacunas e débitos técnicos aceitos;
- componentes impactados e restrições conhecidas;
- estados e condições para avançar ou retornar;
- evidências e experimentos necessários;
- como o contrato será emendado, substituído, concluído ou reaberto.

## Autoridade e execução

Agentes podem consultar o repositório, localizar impactos, revelar incertezas,
propor soluções, implementar contratos e produzir evidências. Automações podem
executar verificações derivadas. Nenhum deles recebe, por capacidade técnica,
autoridade sobre intenção, arquitetura ou risco.

O Arquiteto decide:

- decisões arquiteturais e prioridade;
- risco aceitável;
- relevância das críticas;
- suficiência das evidências;
- aprovação da solução;
- conclusão ou reabertura do workflow.

Ele não carimba decisões da IA: confronta evidência, assume responsabilidade e
decide. Autoridade humana também não altera fatos; falha registrada permanece
falha, ainda que o Arquiteto aceite conscientemente o risco residual.

## Funções do workflow

### Autoria da especificação

O Autor transforma intenção em contrato verificável. Consulta repositório,
arquitetura, conhecimento e precedentes para fundamentar a proposta e sua
implementabilidade. Antes da prontidão, confronta a proposta com as autoridades
normativas dos comportamentos, APIs, estados, ciclos de vida, nomes e fronteiras
afetados. IA pode ampliar a investigação sem converter inferência em decisão.

### Análise de implementabilidade

A análise anterior à implementação permanece obrigatória, mas não requer ator
separado. Pode ser realizada pelo próprio Autor, pelo Autor apoiado por IA, por
agente especializado ou por especialista separado quando risco e incerteza
justificarem segregação.

Ela não certifica o futuro apenas pela leitura do código. Registra evidências
encontradas, componentes impactados, restrições, incertezas, experimentos
necessários e bloqueadores. Compilação, protótipo, consulta a API ou banco e
hardware real são experimentos quando a confirmação depende deles.

Prontidão é um teste de suficiência: deve existir ao menos uma implementação
tecnicamente plausível dentro da baseline e do recorte, sem conflito ou decisão
normativa ausente. Não é necessário resolver antecipadamente escolhas técnicas
locais nem produzir evidências que pertencem à implementação e à revisão. Um
experimento só bloqueia antes da implementação quando é indispensável para
decidir se alguma solução conforme é possível.

Autoridade normativa é estritamente comportamental. Uma especificação não se
torna proprietária de todas as evoluções de uma fachada, componente, arquivo ou
domínio por mencioná-lo. Extensões aditivas governam seus próprios contratos e
presumem-se não interferentes; fonte anterior só bloqueia quando requisitos
explícitos tornam o conflito inevitável em qualquer implementação dentro do
recorte.

Análise confiável também precisa tornar visível o que descartou. Um `Ready`
formal reconcilia bloqueadores anteriores, declara cobertura de requisitos,
critérios e débitos, preserva restrições materiais não bloqueantes e registra um
challenge final contra inconsistência interna. Parecer não persistido permanece
consultivo.

Essa cobertura dirige a investigação, não o volume da saída. O relatório é uma
síntese decisória curta, e cada execução cria evidência nova sem substituir
relatórios anteriores.

### Implementação

Uma análise `Ready` da versão corrente e uma ordem explícita do Arquiteto são
suficientes para iniciar. A ordem aprova e autoriza a passagem; não existe
promoção documental intermediária. O Implementador registra `In Progress`,
executa a especificação, faz verificações técnicas, registra
decisões locais e produz relatório e evidências. Dúvidas, limitações e desvios
são declarados, não preenchidos silenciosamente.

Em artefato construível, a autorização de implementação inclui o build canônico
e proporcional dos entregáveis afetados. A especificação não precisa repetir
essa permissão. Build falho ou não executado impede alegar implementação
concluída. Criar ou alterar testes exige previsão explícita na especificação;
executá-los, assim como usar hardware ou realizar operações externas, exige
autorização operacional própria.

### Revisão e challenge

Revisão é o quarto estágio e confronta implementação, contrato e evidências.
Sua profundidade e independência são proporcionais ao risco. Segurança,
autorização, corrupção de dados, concorrência, operações irreversíveis e falhas
recorrentes justificam challenge adicional.

O crítico pode localizar inconsistências e pontos cegos, ou concluir que não
encontrou risco adicional relevante. Não substitui o Arquiteto, não aprova ou
reprova o workflow, não redefine unilateralmente critérios, não obriga uma
narrativa de testes e não reabre decisão registrada sem nova evidência.

Agentes com capacidades, contexto e vieses semelhantes não constituem
necessariamente validação independente, mesmo quando ocupam sessões distintas.

## Validação e evidências

Testes automatizados são evidências limitadas, não prova absoluta. A
especificação decide explicitamente se sua criação ou alteração integra o
recorte, relacionando-os a critérios de aceite e ao meio de validação. O
Implementador não inventa testes por cobertura, conveniência ou preferência.
Criar teste não autoriza executá-lo, e teste contratado nunca é alterado apenas
para produzir resultado verde.

O Implementador não usa testes que implementou como
argumento autorreferente de correção. O conjunto de aceitação pode incluir:

- código e diffs;
- builds e execução;
- logs e testes;
- hardware, APIs, bancos e infraestrutura reais;
- relatórios dos atores;
- decisões e observações do Arquiteto;
- defeitos encontrados posteriormente.

Em firmware e integrações, execução no ambiente real pode ser a evidência
funcional mais forte. O Arquiteto decide a suficiência do conjunto e o risco
residual aceito.

## Especificação como conhecimento evolutivo

Uma especificação nasce antes do código, avança e retorna durante investigação,
implementação e validação e permanece rastreável após a conclusão. Retornos
registram aprendizado controlado, não necessariamente fracasso. Apenas o
Arquiteto determina conclusão ou reabertura.

"Fonte da verdade" não significa documento monolítico. ADRs explicam decisões;
diretrizes governam o método; mapas localizam; código e testes implementam e
evidenciam; Git preserva linhagem; relatórios registram execuções. Para cada
comportamento, a autoridade normativa continua inequívoca.

## Modelo experimental

As hipóteses da EKOM são continuamente confrontadas com experimentos reais.
Teorias, papéis e mecanismos podem ser confirmados, ajustados ou refutados
conforme evidências materiais. O próprio modelo faz parte do objeto de
aprendizado, e seu histórico não é reescrito para acomodar conclusões novas.

A versão 3.0 preserva especificação como coordenação e execução amplamente
delegada, mas refuta como regras universais a segregação obrigatória do
Analista, o Revisor obrigatório, agentes múltiplos como revisão independente,
testes verdes como prova suficiente e autonomia completa como capacidade atual.

## O que o EKOM não é

- substituição do Arquiteto;
- promessa de autonomia completa ou automação de ponta a ponta;
- documentação de cada linha de código;
- substituição de Git, testes, ADRs, observabilidade ou CI/CD;
- autorização para agentes decidirem requisitos ou risco;
- motor universal de agentes, filas ou escalonamento;
- processo rígido ou dogma imune a evidências.

## Estado do método

O EKOM 4.5 está aprovado e vigente para adoção. Autonomia completa permanece
horizonte evolutivo, não capacidade comprovada. A decisão está registrada no
[`ADR-0002`](adr/ADR-0002-EKOM-3-OPERATIONAL-AUTHORITY.md), com o roteamento
documental operacionalizado pela
[`ADR-0003`](adr/ADR-0003-DOCUMENT-ROUTING-AND-EVIDENCE-SEPARATION.md).
O mapa combina índice de autoridade, árvore de conhecimento e diagrama de
relações conforme a
[`ADR-0004`](adr/ADR-0004-KNOWLEDGE-MAP-VISUAL-STRUCTURE.md).
O confronto de autoridade normativa durante a autoria está registrado na
[`ADR-0005`](adr/ADR-0005-SPECIFICATION-AUTHORITY-CONFRONTATION.md).
A contenção de escopo funcional e os pré-requisitos arquiteturais estão
registrados na
[`ADR-0006`](adr/ADR-0006-SPECIFICATION-SCOPE-AND-ARCHITECTURAL-PREREQUISITES.md).
O workflow simplificado em quatro estágios e a ordem como passagem estão
registrados na [`ADR-0009`](adr/ADR-0009-FOUR-STAGE-WORKFLOW.md), que substitui
a ADR-0007.
O build intrínseco à implementação está registrado na
[`ADR-0008`](adr/ADR-0008-BUILD-INTRINSIC-TO-IMPLEMENTATION.md).
Testes dirigidos pela especificação estão registrados na
[`ADR-0010`](adr/ADR-0010-SPECIFICATION-DRIVEN-TESTS.md).
A entrega Git intrínseca a toda mudança material autorizada está registrada na
[`ADR-0011`](adr/ADR-0011-INTRINSIC-GIT-DELIVERY.md).
A preservação e remediação de débito técnico aceito estão registradas na
[`ADR-0013`](adr/ADR-0013-TECHNICAL-DEBT.md).
O limite de prontidão por suficiência, a autoridade normativa limitada e os
controles contra omissão estão registrados na
[`ADR-0014`](adr/ADR-0014-IMPLEMENTABILITY-SUFFICIENCY-BOUNDARY.md).
