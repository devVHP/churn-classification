import joblib
import pandas as pd

def predictions():
    print('Loading dataset and model')
    artifact = joblib.load('random_forest_churn_v1.pk')
    dataset = pd.read_csv('../data/processed/new_data.csv')

    model = artifact["model"]
    threshold = artifact["threshold"]
    expected_columns = model.feature_names_in_
    dataset = dataset[expected_columns]

    print('Making predictions')
    proba = model.predict_proba(dataset)[:, 1]
    y_pred = (proba >= threshold).astype(int)

    dataset['churn_prediction'] = y_pred
    dataset['probability'] = proba

    print('Exporting file')
    dataset.to_excel('churn_prediction.xlsx')

    print('Sucess!')

def main():
    predictions()

if __name__ == "__main__":
    main()