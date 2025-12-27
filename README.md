# Churn Classification

Este projeto tem como objetivo o desenvolvimento de um modelo de **Machine Learning** para a classificação de **clientes com potencial de churn** em uma empresa de telecomunicações.

Ao longo do desenvolvimento do projeto, as seguintes habilidades foram aprendidas e aprimoradas:

1. Análise de dados
2. Análise estatística
3. Modelagem de modelos de machine learning
4. Undersampling e Oversampling
5. Análise de métricas estatísticas como:
   1. Correlação; 
   2. Recall, Acurácia, Matriz de confusão; 
   3. Curva ROC;
   4. Métrica AUC;

# Como rodar o projeto

## Bibliotecas utilizadas:
Para executar o projeto, certifique-se de que as seguintes bibliotecas estão instaladas:

```python
imblearn
numpy
scipy
pandas
seaborn
joblib
sklearn
matplotlib
```
O projeto conta com dois scripts principais:
- Para criar o modelo, executamos o primeiro script "create_model.py", a execução pode ser feita na própria IDE ou rodando o comando abaixo no seu terminal linux:
```bash
python scripts/create_model.py
```
O Script irá criar um arquivo contendo o modelo e o threshold que será utilizado.

- Para gerarmos as previsões, primeiro tenha certeza de que tem o arquivo "new_data.csv"
na pasta data/processed. Após isso executamos pela IDE ou pelo terminal novamente:
```bash
python scripts/prediction.py
```

O arquivo churn_prediction.xlsx será gerado com as predições do modelo, incluindo uma coluna indicativa de churn (0 = não churn, 1 = churn) e a respectiva probabilidade associada à ocorrência de churn, conforme estimada pelo modelo.

## Estrutura do projeto
```python
churn-classification/
│
├── data/
│   ├── raw/
│   │   └── telecom_churn.csv
│   │
│   ├── train/
│   │   └── telecom_churn_train.csv
│   │
│   └── processed/
│       ├── new_data.csv
│       └── answers.csv
│
├── notebooks/
│   ├── analyze-train.ipynb
│   └── modelo-train.ipynb
│
├── scripts/
│   ├── create_model.py
│   └── prediction.py
│
├── README.md
└── requirements.txt
```
### data/
Contém todos os dados do projeto, organizados por estágio do pipeline.

- data/raw/: dados originais, sem qualquer tratamento.

- data/train/: 
Dados já selecionados para treino

- data/processed/: dados processados ou de entrada para inferência.
  - new_data.csv: novos clientes para previsão de churn.
  - answers.csv: resultados originais.

### notebooks/

Usado apenas para exploração e experimentação.

- analyze-train.ipynb: EDA (correlações, churn rate); treinamento de  diversos modelos; análises estatísticas; análise de métricas.
- modelo-train.ipynb: Teste e validação com modelo selecionado.

### scripts/
Scripts executáveis do projeto.

- create_model.py: Treina o modelo final
- prediction.py: Carrega o modelo treinado, recebe novos dados, gera predições de churn
