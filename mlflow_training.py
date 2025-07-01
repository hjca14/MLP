import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Carregar dados
df = pd.read_csv("dados.csv")

X = df["descricao"]
y = df["categoria"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hiperparâmetros a testar
n_estimators_list = [10, 50, 100]
max_depth_list = [5, 10]

# Iniciar experimento no MLflow
mlflow.set_experiment("classificacao_produto_v2")

for n in n_estimators_list:
    for d in max_depth_list:
        with mlflow.start_run():
            # Criar pipeline
            clf = Pipeline([
                ("vect", TfidfVectorizer()),
                ("rf", RandomForestClassifier(n_estimators=n, max_depth=d, random_state=42))
            ])

            # Treinar
            clf.fit(X_train, y_train)

            # Prever
            y_pred = clf.predict(X_test)

            # Avaliar
            acc = accuracy_score(y_test, y_pred)

            # Exemplo
            input_example = pd.DataFrame({"descricao": ["Calça jeans masculina"]})

            # Registrar no MLflow
            mlflow.log_param("n_estimators", n)
            mlflow.log_param("max_depth", d)
            mlflow.log_metric("accuracy", acc)
            mlflow.sklearn.log_model(
                sk_model=clf,
                name="modelo",
                input_example=input_example
            )
            print(f"Executado: n_estimators={n}, max_depth={d}, acc={acc:.2f}")
