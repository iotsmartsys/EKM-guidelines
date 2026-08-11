# Regras comuns dos perfis EKOM

**Modelo EKOM aplicável:** 3.2

**Versão do perfil:** 2.1

**Estado:** vigente

Leia este arquivo antes do perfil recebido. Perfis representam capacidades
acionáveis; não formam uma sequência universal de atores separados.

## 1. Autoridade

O Arquiteto humano decide intenção, prioridade, escopo, arquitetura, risco
aceitável, relevância das críticas, suficiência das evidências, aprovação,
conclusão ou reabertura e integração.

- Execute somente o recorte e as operações autorizados.
- Não invente requisitos nem substitua decisão do Arquiteto.
- Não converta falha, limitação ou validação ausente em sucesso.
- Não declare aprovação, reprovação ou conclusão do workflow por autoridade
  própria.
- Quando decisão humana mudar o comportamento, atualize a especificação antes
  de tratá-lo como contrato.

## 2. Condições de entrada

Antes de executar:

1. confirme objetivo, especificação quando aplicável, função e operações;
2. confirme branch derivada da `main` e árvore limpa;
3. leia `AGENTS.md`, estas regras, o perfil aplicável, a especificação e as
   fontes pertinentes;
4. preserve alterações preexistentes;
5. confirme que o estado permite a atuação.

Se condição material falhar, informe o impedimento sem assumir autoridade
adicional. Uma ordem pode combinar Autoria e análise de implementabilidade; um
Analista ou Revisor separado só é obrigatório quando o Arquiteto ou o risco
determinarem segregação.

## 3. Fontes e arquitetura

- A especificação é a fonte da verdade para comportamento, limites, estados e
  aceite.
- `AGENTS.md` localiza invariantes e fontes técnicas.
- Código e testes implementam ou evidenciam; não criam requisito por inferência.
- Prompts e automações acionam trabalho; não criam autoridade normativa
  paralela.

> **Specifications orchestrate. Code implements.**

Preserve arquitetura, organização e separação de responsabilidades. Use o
precedente equivalente mais próximo. Nova camada, estrutura ou abstração
transversal requer decisão arquitetural explícita. Ausência ou conflito de
precedente é incerteza a registrar e devolver ao Arquiteto.

## 4. Funções necessárias

### 4.1 Autoria e análise

A especificação nasce antes do código. O Autor consulta repositório,
arquitetura e conhecimento existente. Antes de implementar, deve existir
análise de implementabilidade que registre evidências, componentes impactados,
restrições, incertezas, experimentos necessários e bloqueadores.

Essa análise pode ser feita pelo Autor, com apoio de IA, por agente
especializado ou por especialista separado. Leitura do código não certifica o
que depende de compilação, protótipo, API, banco, infraestrutura ou hardware;
registre o experimento necessário em relatório de análise separado. O relatório
pode recomendar mudança normativa, mas não a incorpora à especificação.

### 4.2 Implementação

O Implementador responde pela especificação autorizada, verificações técnicas e
relatório separado de decisões locais, evidências, dúvidas, limitações e
desvios. Restrição ou ambiguidade normativa retorna ao rascunho e análise.

### 4.3 Challenge

Crítica ou revisão é consultiva e proporcional ao risco. O crítico registra em
relatório separado riscos e pontos cegos ou declara que não encontrou risco
adicional relevante. Não edita a especificação, não promove estado, não
redefine aceite, não impõe narrativa de testes, não reabre decisão sem nova
evidência e não substitui o Arquiteto.

Outro agente não é automaticamente independente. Quando independência for
material, registre conflitos de participação, contexto e capacidade.

## 5. Critérios, testes e evidências

Critérios devem permitir distinguir sucesso, falha e ausência de evidência por
cenário, ação, resultado observável e meio de validação proporcional ao risco.
Doubles preservam a semântica material. Compilação não comprova execução; zero
casos não comprova comportamento.

Testes automatizados são evidências, não prova absoluta. Não os altere apenas
para obter verde nem os use como argumento autorreferente de correção. Eles são
especialmente valiosos para regressões, regras complexas, bordas, segurança e
contratos estáveis.

Registre, conforme o contexto, código e diffs, builds, execução real, logs,
testes, hardware, APIs, bancos, infraestrutura, relatórios, decisões do
Arquiteto e defeitos posteriores. Evidência real pode ter precedência funcional;
o Arquiteto decide a suficiência do conjunto.

## 6. Conhecimento, estado e entrega

- Atualize somente conhecimento materialmente afetado.
- Roteie contrato para especificação, arquitetura durável para ADR, execução
  para relatório, localização para mapa e estado resumido para changelog.
- Registre decisões, lacunas, validações, limitações e resultado na fonte de
  autoridade correspondente.
- Reconcilie índice, árvore e diagrama do mapa quando autoridade, contenção,
  responsabilidade ou relação material mudar.
- Não transforme changelog em diário nem copie a linhagem do Git.
- Agentes registram fatos e estados sustentados por sua execução.
- Apenas o Arquiteto determina que a especificação está Concluída ou Reaberta.

Analista, Implementador, Revisor e responsável pela validação escrevem seus
relatórios nos destinos declarados pelo projeto. Somente o Arquiteto incorpora
achados em especificações, aceita ADRs e promove estados normativos. Uma exceção
de escrita mecânica deve nomear arquivos e transformação; não transfere decisão.

Toda atuação material produz resultado versionável, commit e, quando
autorizado, push; termina com árvore limpa. Não use commit vazio. A ordem normal
não autoriza force push, merge, tag, release ou deploy.

Antes de promover estado, criar commit, fazer push ou responder
conclusivamente, confirme que toda execução iniciada chegou a estado terminal.
Estado pendente ou desconhecido bloqueia conclusão e nunca é convertido em
evidência aprovada.
