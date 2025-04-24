import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import mlflow
import mlflow.sklearn

df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

with mlflow.start_run():
    model = LogisticRegression()
    model.fit(X, y)
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_param("solver", model.solver)
    mlflow.log_metric("score", model.score(X, y))
    joblib.dump(model, 'model.joblib')
    print("Model trained, saved, and experiment logged to MLflow")
