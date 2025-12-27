import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib

def train_model():
    print("Loading database")
    dataset = pd.read_csv("../data/train/telecom_churn_train.csv")

    print("Training model")
    model = RandomForestClassifier()
    X = dataset.drop(['Churn'], axis=1)
    y = dataset['Churn']
    X = X.astype(float)
    smote = SMOTE(sampling_strategy='minority')
    X_smote, y_smote = smote.fit_resample(X, y)
    model.fit(X_smote, y_smote)

    print("Saving model")
    joblib.dump(
        {
            "model": model,
            "threshold": 0.2
        },
        "random_forest_churn_v1.pk"
    )

    print("Sucess!")

def main():
    train_model()

if __name__ == "__main__":
    main()

