# Analysis and forecasting of brazilian electricity

O objetivo deste trabalho é realizar uma análise dos dados de energia elétrica brasileira, para isso foram utilizados os dados fornecidos pela [ONS](https://www.ons.org.br/) de 2000 a 2020, sendo os dados de 2000 a 2018 para análise e modelagem e os dados de 2019 e 2020 para o teste do modelo.

## Dicionário dos Dados

Segue um resumo do documento [dicionário de dados](./data/DicionarioDados_GeracaoPorUsina.pdf) fornecido pelo próprio site da ONS:


## Dados Utilizados

A partir do estudo do dicionário de dados descrito anteriormente, foram retiradas as variáveis nom_subsistema (se assemalha a id_subsistema), nom_estado (se assemelha a id_estado), id_ons e ceg (pois não seriam importantes para o projeto)