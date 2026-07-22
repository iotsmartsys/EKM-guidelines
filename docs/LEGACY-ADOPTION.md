# Adoção da EKM em projetos legados

## 1. Propósito

Aplicar a EKM a um sistema que não foi criado com fontes normativas suficientes, sem tentar documentar todo o repositório de uma vez nem confundir comportamento existente com comportamento desejado.

## 2. Resultado esperado

Ao final da fundação inicial, o projeto deve possuir:

- uma entrada obrigatória para agentes;
- diretrizes EKM locais;
- um mapa das fontes e lacunas;
- um changelog transacional;
- um dossiê executivo do sistema;
- especificações iniciais para os domínios prioritários;
- perguntas humanas registradas quando a intenção não puder ser inferida.

Isso não significa que todo o legado estará imediatamente `Reconstructible`.

## 3. Níveis de cobertura

| Nível | Significado |
|---|---|
| `Unmapped` | Domínio ainda não localizado |
| `Inventoried` | Arquivos, entradas e símbolos principais identificados |
| `Mapped` | Fluxos e dependências principais compreendidos |
| `Reviewed` | Contratos, riscos e comportamento confrontados com o código |
| `Specified` | Fonte normativa criada e reconciliada com a decisão humana |
| `Reconstructible` | Comportamento, contratos e validações permitem reconstrução sem inferência relevante |

## 4. Fluxo de adoção

### Fase 0 — Autorização e limites

Definir:

- caminho e escopo do repositório;
- se a fase é somente documental;
- ações externas proibidas;
- orçamento de tempo/contexto;
- pessoas responsáveis por decisões.

### Fase 1 — Baseline real

Registrar branch, commit, worktree, arquivos de instrução, builds, testes e documentação existentes. Alterações preexistentes pertencem ao baseline e não podem ser apagadas ou atribuídas à adoção.

### Fase 2 — Inventário em largura

Localizar sem leitura integral indiscriminada:

- linguagens, frameworks e plataformas;
- entradas e executáveis;
- módulos e dependências;
- APIs públicas e consumidores;
- dados persistentes e integrações externas;
- builds, testes, CI/CD e releases;
- documentos existentes.

Usar índices, manifests, árvores rasas, busca de símbolos e configurações antes de abrir implementações extensas.

### Fase 3 — Mapa de domínios

Dividir o sistema por comportamentos e responsabilidades, não apenas por pastas. Classificar a cobertura e priorizar domínios por impacto, regressões históricas, exposição pública e frequência de mudança.

### Fase 4 — Questões de intenção

Solicitar decisão humana somente quando o repositório não conseguir distinguir:

- requisito vigente;
- limitação intencional;
- compatibilidade obrigatória;
- comportamento acidental;
- bug conhecido;
- código obsoleto;
- preparação para futuro suporte.

Perguntas devem ser agrupadas e objetivas para reduzir custo de interação.

### Fase 5 — Fundação documental

Criar os ativos mínimos e um dossiê executivo. Especificações inicialmente descobertas devem permanecer `Draft` ou `Proposed` até a intenção ser confirmada. Apenas decisões humanas ou fontes normativas inequívocas justificam `Active`.

### Fase 6 — Aprofundamento orientado por risco

Aplicar **specification on touch**: antes de mudar uma funcionalidade relevante ainda não especificada, elevar seu domínio ao menos a `Specified`.

Áreas estáveis e de baixo risco podem permanecer `Mapped`, desde que a lacuna esteja visível.

### Fase 7 — Auditoria

Confrontar documentos com código, testes e automações. Registrar divergências sem corrigi-las silenciosamente. Fechar a transação inicial apenas quando os ativos criados estiverem consistentes e todas as incertezas restantes estiverem representadas como lacunas.

## 5. Autonomia segura

O agente pode autonomamente:

- inventariar arquivos e dependências;
- descrever fluxos comprovados;
- localizar APIs e integrações;
- classificar evidências;
- propor estados e especificações;
- registrar lacunas;
- validar links e consistência documental.

O agente deve interromper ou solicitar decisão antes de:

- declarar intenção não comprovada;
- tornar uma proposta `Active` sem autorização;
- remover ou reclassificar suporte;
- alterar código, build, dados ou automações fora da autorização;
- resolver contradições normativas por preferência própria.

## 6. Eficiência de contexto

- Começar em largura e aprofundar sob demanda.
- Preferir buscas e índices a dumps integrais.
- Ler arquivos completos apenas quando governam a tarefa ou são necessários para provar um contrato.
- Agrupar perguntas humanas.
- Referenciar fontes estáveis em vez de duplicar conteúdo.
- Registrar conclusões duráveis no repositório antes de encerrar a sessão.

## 7. Critério de conclusão da fundação

A adoção inicial está concluída quando:

- o baseline está registrado;
- os domínios relevantes estão ao menos inventariados;
- a arquitetura e os fluxos principais estão no dossiê;
- APIs, integrações, persistência, build, testes e release possuem localização conhecida;
- fontes normativas existentes foram classificadas;
- decisões confirmadas foram especificadas;
- incertezas foram convertidas em lacunas ou perguntas;
- não houve alteração funcional não autorizada;
- a transação EKM inicial foi auditada e encerrada.
