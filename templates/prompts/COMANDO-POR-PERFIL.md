# Comando mínimo — perfil EKOM referenciado

**Modelo EKOM:** 4.5

**Estado:** vigente

Atue como **<PAPEL EKOM>** na especificação
**<CAMINHO OU ID, OU NÃO SE APLICA>**.

Produza o resultado da capacidade autorizada. Autoria e análise podem ser
combinadas; segregação deve ser explícita quando necessária. Para o Autor, a
intenção ou mudança é:
**<INTENÇÃO OU MUDANÇA, OU NÃO SE APLICA>**.

Siga o roteamento definido no `AGENTS.md` do projeto. Leia somente as regras
comuns, o perfil correspondente ao papel, a especificação indicada e as fontes
técnicas pertinentes.

Na autoria, localize e confronte as autoridades normativas dos elementos
afetados antes de recomendar prontidão; registre relações na especificação e,
no relatório, somente conflito material que sustente bloqueio.

Na análise, produza exatamente uma classificação do EKOM e teste se existe ao
menos uma implementação tecnicamente plausível e conforme na baseline e no
recorte. Não exija solução interna completa nem evidência própria de
Implementação ou Revisão. Só bloqueie por impossibilidade ou conflito, decisão
normativa ausente, pré-requisito arquitetural, impacto material não delimitado
ou evidência prévia indispensável para decidir se alguma solução conforme é
possível. Fonte anterior só bloqueia com cadeia cumulativa: requisito anterior
explícito e aplicável, requisito novo necessariamente incompatível, conflito
inevitável e nenhuma implementação conforme no recorte. Não exija prova de
ausência de regressão, não investigue conflito por mera proximidade técnica e
não use `prontidão condicionada` nem devolva capacidade arquitetural
independente como simples ajuste da funcionalidade.

Declare cobertura de requisitos, critérios e débitos relacionados; reconcilie
cada bloqueador anterior aplicável; registre até cinco restrições materiais não
bloqueantes; confronte critérios com recorte e remediações postergadas; e, antes
de `Ready`, execute challenge limitado contra contradição interna, critério
insatisfazível, remediação fora do recorte ou achado anterior omitido. Persista o
relatório no diretório autorizado. Sem relatório persistido, o parecer é apenas
consultivo. A investigação pode ser profunda, mas o relatório tem no máximo 800
palavras e contém somente classificação, bloqueadores objetivos, reconciliação,
controle resumido e restrições indispensáveis. Não repita requisitos, não
antecipe implementação, não sugira correções e não escreva próximos passos.

Crie sempre um arquivo novo e imutável no formato
`YYYY-MM-DDTHHMMSSZ-<revisão>-<id-da-execução>-implementability-analysis.md`.
Reanálise ou correção não substitui relatório anterior. Antes de entregar,
confirme que o Git registra o relatório como adicionado (`A`), nunca modificado
(`M`).

Na implementação, confirme análise `Ready` da versão corrente. Esta ordem,
quando nomeia inequivocamente a implementação e a versão, aprova e autoriza a
passagem; não exija promoção ou campo documental adicional. Se faltar análise
aplicável, recuse sem mutação. Registre `In Progress` como primeiro efeito e
execute o build canônico proporcional; execução de testes e operações externas
continua dependente de autorização própria.

Crie ou altere testes somente quando a especificação os exigir explicitamente
e vinculá-los a requisito ou critério de aceite. Não invente suíte, matriz ou
cobertura. Criar teste não autoriza executá-lo.

**Foco adicional, se houver:** `<FOCO OU NENHUM>`

O foco orienta atenção ou sequência. Revisão é o quarto estágio, com challenge
proporcional ao risco. Somente o Arquiteto conclui ou reabre.

**Operações autorizadas:** `<LEITURA, DOCUMENTAÇÃO, CÓDIGO, EXECUÇÃO DE TESTES,
CONFIGURAÇÃO OU OUTRAS OPERAÇÕES DELIMITADAS>`

**Exceções autorizadas pelo Arquiteto:** `<EXCEÇÕES OU NENHUMA>`
