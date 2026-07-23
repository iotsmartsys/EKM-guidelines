# Estudo de caso — Adoção no IoTSmartSysCore

## Contexto

O IoTSmartSysCore é uma biblioteca Arduino/ESP32 extensa, criada antes da EKM. Possui API pública, capabilities, settings, conectividade, integrações, testes e processo de release, além de código legado e preparação parcial para outra plataforma.

## Problema

Aplicar a EKM por documentação exaustiva consumiria muito contexto e poderia transformar o método em burocracia. Ao mesmo tempo, inferir intenção apenas pelo código confundiria requisitos com limitações históricas.

## Estratégia experimentada

1. registrar o baseline real;
2. inventariar o repositório em largura;
3. localizar APIs, runtime, integrações, testes e release;
4. aprofundar somente domínios prioritários;
5. agrupar perguntas de intenção ao responsável;
6. criar a fundação EKM e especificações iniciais;
7. manter divergências de implementação como gaps, sem corrigi-las.

## Decisões humanas necessárias

O código não era suficiente para decidir, por exemplo:

- Arduino/ESP32 como suporte vigente;
- ESP-IDF como preparação futura;
- ESP8266 como não suportado;
- retrocompatibilidade da API pública;
- limite intencional de oito capabilities;
- configuração completa antes de `setup()`;
- reboot após atualização de settings;
- MQTT como transporte principal;
- release permitido somente na `main`.

## Resultado inicial

Foram produzidos diretrizes, mapa, changelog e especificações de API pública, ciclo de vida e release. A adoção também registrou lacunas em vez de iniciar correções funcionais.

## Mudanças introduzidas na EKM

- metodologia específica para projetos legados;
- níveis de cobertura de `Unmapped` a `Reconstructible`;
- inventário em largura antes do aprofundamento;
- specification on touch;
- separação explícita entre fato, decisão, inferência, desvio e lacuna;
- instrução única para adoção inicial por agente.

## Limitação

A fundação documental foi aplicada apenas parcialmente. Ainda precisamos observar se outro executor consegue usar a instrução inicial com pouco contexto adicional e se o custo de manutenção permanece sustentável.
