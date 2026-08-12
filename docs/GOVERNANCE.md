# Governança do EKOM

## 1. Objetivo

Evoluir o EKOM por evidência, com autoridade humana e com a menor carga
operacional capaz de manter conhecimento, decisões, auditabilidade e
verificabilidade.

**Modelo vigente:** EKOM 3.5.

A especificação é a fonte única da verdade para o comportamento pretendido e
o principal objeto do pipeline. Mudanças no método não podem criar em prompts,
automações, relatórios ou código uma autoridade normativa concorrente.

## 2. Autoridade

O Arquiteto humano decide intenção, prioridade, adoção das regras, suficiência
das evidências e conclusão ou reabertura. Agentes podem propor mudanças e
apresentar evidências, mas não tornam uma hipótese obrigatória por iniciativa
própria.

## 3. Critério para adicionar governança

Uma nova obrigação deve demonstrar:

- problema observado em execução real;
- ganho esperado para entrega, conhecimento ou verificação;
- custo operacional e cognitivo;
- forma proporcional de aplicação;
- evidência que permitirá mantê-la, reduzi-la ou descartá-la.

Ideias ainda não aprovadas não entram no fluxo vigente, nos templates, nos
critérios dos experimentos ou nas validações.

## 4. Critério para reduzir governança

Um controle deve ser simplificado ou removido quando:

- repete informação já preservada por uma fonte confiável, como o Git;
- exige preenchimento sem apoiar decisão humana;
- cria etapas universais para um risco localizado;
- atrasa o experimento sem evidência de ganho;
- aumenta divergência entre documentos.

Remover burocracia não autoriza perder decisão, lacuna ou evidência material.

## 5. Versionamento

- **major:** mudança incompatível nos estados ou no modelo;
- **minor:** mudança compatível de comportamento, regra ou capacidade;
- **patch:** esclarecimento sem mudança operacional.

Projetos adotantes migram deliberadamente. Registros históricos continuam
válidos sob a versão usada em sua execução.

## 6. Evolução

Para alterar o método:

1. registrar o problema e a evidência;
2. obter decisão do Arquiteto;
3. atualizar método, decisões, templates e navegação afetados;
4. preservar a compreensão dos experimentos EKM e versões anteriores;
5. validar consistência textual e referências;
6. entregar a mudança por commit e push.

Uma revisão do próprio modelo registra explicitamente hipóteses sustentadas,
revisadas, refutadas ou ainda não comprovadas. O histórico não é reescrito para
fazer versões anteriores parecerem compatíveis com o entendimento novo.

Mudança documental do método deve atualizar também o roteamento e os templates
que induzem a execução. Uma regra conceitual sem destino, autoridade e guarda
proporcional não é considerada operacionalizada.

## 7. Medida de sucesso

O sucesso não é quantidade de documentos ou controles. Avalie:

- tempo entre intenção e entrega validada;
- capacidade de experimentar e descartar ideias;
- atualização do conhecimento;
- decisões localizáveis;
- evidências suficientes para verificar conclusões;
- retrabalho e carga cognitiva;
- confiança proporcional ao risco.

Autonomia completa é horizonte evolutivo. Não é promovida a capacidade vigente
sem experimentos materiais e decisão arquitetural versionada.
