
# Boston House Price Regression Model

Este README fornece uma visão geral do modelo de regressão utilizado para prever 
os preços das casas na área de Boston.

## Instruções iniciais

- As evidências da utilizam do MLFlow Model Registry está nos notebooks ao qual apresentam
o processo de desenvolvimento inteiro do modelo. 

## Descrição do Conjunto de Dados

O conjunto de dados de preços de casas de Boston contém informações sobre várias
características das casas em diferentes bairros de Boston. Ele inclui 506 amostras e 13 variáveis
preditoras. As variáveis são:

1. **CRIM**: Taxa de criminalidade per capita por cidade.
2. **ZN**: Proporção de terrenos residenciais divididos em lotes com mais de 25.000 pés quadrados.
3. **INDUS**: Proporção de acres de negócios não varejistas por cidade.
4. **CHAS**: Variável fictícia Charles River (1 se o trecho limita o rio; 0 caso contrário).
5. **NOX**: Concentração de óxidos nítricos (partes por 10 milhões).
6. **RM**: Número médio de quartos por habitação.
7. **AGE**: Proporção de unidades ocupadas pelos proprietários construídas antes de 1940.
8. **DIS**: Distâncias ponderadas para cinco centros de emprego em Boston.
9. **RAD**: Índice de acessibilidade às rodovias radiais.
10. **TAX**: Taxa de imposto sobre propriedade de valor total por $10.000.
11. **PTRATIO**: Proporção aluno-professor por cidade.
12. **B**: 1000(Bk - 0.63)^2 onde Bk é a proporção de negros por cidade.
13. **LSTAT**: Porcentagem de status inferior da população.
14. **MEDV**: Valor mediano das casas ocupadas pelos proprietários em $1000s (variável alvo).

## Objetivo

O objetivo deste projeto é construir um modelo de regressão que possa prever o valor mediano das casas 
ocupadas pelos proprietários (MEDV) com base nas outras 13 variáveis preditoras.

## Análise Exploratória

A análise exploratória dos dados foi realizada com o objetivo de compreender as características e padrões
presentes no conjunto de dados. Foram calculadas métricas descritivas, como a média e o desvio padrão, permitindo
 uma visão geral sobre a dispersão das variáveis.

Observou-se que o dataset é pequeno, com considerável dispersão em relação às médias das variáveis. Além disso, 
analisando a distribuição das variáveis, percebe-se que, embora algumas apresentem características ligeiramente
similares a uma distribuição gaussiana, muitas delas divergem significativamente desse padrão.

Em relação à correlação entre as variáveis, identificou-se que estas possuem correlações
predominantemente não lineares, variando de baixa a moderada. Essa característica representa
um desafio para modelos lineares, como a regressão linear, que pressupõem linearidade entre as
 variáveis, o que pode impactar negativamente na sua performance.

Durante a análise, identificamos a presença de outliers em várias variáveis, com destaque 
para as colunas CHAS, CRIM e ZN. Optamos por remover esses dados, considerando que os algoritmos
 a serem testados são sensíveis a valores extremos.

Embora uma alternativa fosse substituir esses valores pela mediana, decidimos evitar essa abordagem, 
pois havia o receio de introduzir um viés que pudesse impactar negativamente o desempenho dos modelos. 
Assim, a remoção dos outliers foi escolhida como uma solução mais segura e direta para este caso.


## Pré-processamento dos Dados

Antes de treinar o modelo, os dados passam por um pré-processamento que inclui:

- Tratamento de valores ausentes.
- Remoção de colunas que não irão ser usadas para treinar o modelo
- Tratamento de Outliers
- Normalização das variáveis.

## Modelos de Regressão Utilizados

Foram avaliados diferentes modelos de regressão para este problema, incluindo:

- **Regressão Linear Simples**: Um modelo linear básico, útil para entender relações diretas entre as variáveis.

- **Árvores de Decisão**: Modelos não lineares que capturam relações mais complexas entre as variáveis, 
    adaptando-se melhor a dados com baixa linearidade.

- **Random Forest**: Um método baseado em múltiplas árvores de decisão, projetado para melhorar a precisão e 
    mitigar problemas de overfitting.

Para aproveitar ao máximo o conjunto de dados, que é relativamente pequeno, foi utilizada a validação cruzada, 
especificamente o método K-Fold Cross Validation. Essa abordagem permitiu uma avaliação mais robusta do desempenho 
de cada modelo, maximizando o uso das informações disponíveis.

A performance dos modelos foi avaliada utilizando a métrica:

- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**
- **R^2** 

## Resultados

Os experimentos realizados mostraram que o modelo Random Forest (ou Floresta Aleatória) 
obteve o melhor desempenho em comparação com a Árvore de Regressão e a Regressão Linear. 
Especificamente, o modelo apresentou um MAE de 5%, o que indica que as predições feitas 
pela Random Forest tinham, em média, uma diferença de 5% em relação aos valores reais dos 
preços das casas.

Após a análise inicial dos experimentos, o modelo Random Forest foi submetido a 
um processo de otimização de hiperparâmetros, o que resultou em um MAE final de 6,5%. 
O modelo otimizado foi então registrado no MLflow para facilitar seu rastreamento e reprodutibilidade.

## Como testar a aplicação?

Para testar o deployment da solução, existe os seguintes requisitos:

- Possuir Docker instalado na máquina.

Após atender esses requisitos execute o comando abaixo na raiz do projeto:

``docker-compose up --build``

O próximo passo é navegar até ``http://127.0.0.1:8084`` aonde a porta do container 
é exposta para o host

## Monitoramento

No monitoramente é natural que precisamos de métricas para avaliar a performance de modelos.
Se tratando de um problema de regressão, as seguintes métricas poderiam ser utilzadas para 
monitorar esse modelo em produção:

- **Mean Absolute Error** - MAE é uma métrica de performance para modelos de regressão. O Erro
absoluto é a diferença absoluta entre o valor previsto pelo modelo e o valor real da observação. 
No final é calculado a média dos erros absolutos de cada observação no dataset.

- **Mean Square Erro**: O MSE calcula a média dos quadrados das diferenças entre os valores 
previstos e os valores reais. Uma vantagem é que erros maiores são mais penalizados do que menores.

Essas métricas são úteis pois sua interpretabilidade é muito alta. E teremos com elas uma base sólida
para avaliar o modelo em produção.

O monitoramento contínuo é essencial no processo de Machine Learning. Quando um modelo finalmente é 
colocado em produção, o trabalho não está concluído; na verdade, ele nunca acaba. Isso é o que chamamos
de MLOps: tudo deve ser feito de forma contínua. No mundo real, as condições estão sempre mudando—os dados,
o mercado, as preferências dos clientes, entre outros fatores. Por essa razão, é natural que o desempenho 
do modelo diminua com o tempo.

Uma das principais causas dessa queda de desempenho são os fenômenos conhecidos como Data Drift e Concept Drift.

- **Data Drift** refere-se a mudanças nas distribuições estatísticas dos dados de entrada. 
Quando os dados começam a se comportar de maneira diferente do que o modelo foi treinado para prever,
o modelo passa a gerar previsões menos precisas.

- **Concept Drift**,por sua vez, ocorre quando há mudanças nas relações entre as variáveis de entrada (features)
e a variável alvo (target). Isso significa que, com o tempo, o próprio relacionamento entre as variáveis pode mudar,
fazendo com que o modelo se torne obsoleto se não for ajustado.


Esses problemas trazem a necessidade do cientista de dados, iniciar novamente o processo e treinar um novo modelo
preditivo. A pergunta é: como lidar com a necessidade de re-treinar um modelo devido a esses problemas?


- Monitoramento contínuo é fundamental para identificar quando re-treinar é necessário.
- Utilizar ferramentas de versionamento, para possuir um histórico de versões anteriores de modelos treinados. Isso facilita 
o acompanhamento do desempenho de diferentes versões e a reversão para versões anteriores, caso o modelo re-treinado não tenha
um bom desempenho em produção.
- Realizar validações no modelo retreinado como teste A/B.
