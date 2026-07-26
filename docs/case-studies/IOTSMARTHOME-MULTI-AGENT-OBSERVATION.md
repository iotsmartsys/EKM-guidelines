# Observação multiagente no iotsmarthome

**Estado:** evidência experimental

**Modelo EKM aplicado:** 1.8 durante a execução; simplificações consolidadas na
EKM 1.9 após a análise do processo

**Projeto:** aplicativo Swift para iOS, iPadOS e watchOS

**Repositório observado:**
`/Users/marcelocostamiranda/source/IoT/SmartHome/Apps/iotsmarthome/iotsmarthome`

## Contexto

O caso foi iniciado para preparar e usar a EKM em outro tipo de sistema após o
experimento no SmartHome-DeviceApi. A aplicação do processo revelou custo
operacional excessivo no protocolo vigente e motivou a simplificação que
resultou no modelo 1.9.

## Resultado funcional

O Arquiteto executou a validação humana e os testes integrados da implementação.
O comportamento foi aceito e os testes integrados foram aprovados.

Esse resultado comprova a aceitação funcional observada no ambiente do
Arquiteto. Ele não apaga desvios processuais ocorridos durante a execução.

## Resultado de conformidade

Nos experimentos relatados pelo Arquiteto, somente o Codex cumpriu
integralmente a EKM de forma consistente. Agentes e modelos usados pelo chat do
VS Code deixaram de cumprir partes do método ou tomaram decisões incompatíveis
com suas regras, mesmo quando produziram resultados tecnicamente aproveitáveis.

A observação separa duas dimensões:

- **resultado funcional:** a implementação pode estar correta e ser aceita;
- **conformidade do processo:** o agente pode ainda ter violado limites,
  estados ou responsabilidades da EKM.

Uma dimensão não deve ser usada como prova automática da outra.

## Interpretação e limite

A assertividade do Codex foi percebida também em conversas novas e sem contexto
conversacional anterior. Isso não comprova que o Codex reutilize memória de
outras conversas ou contexto do ChatGPT.

A diferença observada pode estar relacionada ao modelo, ao ambiente agente, à
hierarquia de instruções, às ferramentas disponíveis ou à capacidade de
localizar e aplicar os artefatos do repositório. O experimento não isolou essas
variáveis e, portanto, não permite atribuir causalidade a uma delas.

## Consequência para a EKM

A EKM não deve depender de memória implícita, conversa anterior ou capacidade
específica de um fornecedor. Suas regras operacionais precisam ser curtas,
locais, explícitas e verificáveis a partir do repositório e da ordem atual do
Arquiteto.

O caso reforça as decisões já incorporadas na EKM 1.9:

- reduzir burocracia que compete pela atenção do agente;
- manter o Arquiteto como autoridade final;
- usar o estado da especificação para orientar a próxima etapa;
- preservar decisões, lacunas e evidências materiais;
- exigir entrega versionada por commit e push;
- avaliar separadamente qualidade funcional e conformidade metodológica.

O caso não justifica introduzir novos controles no fluxo vigente nem afirmar
independência da EKM em relação ao executor.
