"""Seis experiências pequenas, offline, com dados sintéticos e seed fixa."""

import json
from pathlib import Path

import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_classification
from sklearn.decomposition import PCA
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import (adjusted_rand_score, f1_score, mean_absolute_error,
                             precision_score, recall_score, silhouette_score)
from sklearn.model_selection import GridSearchCV, StratifiedKFold, TimeSeriesSplit, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


SEED = 42


def imoveis():
    rng = np.random.default_rng(SEED)
    area = rng.uniform(30, 150, 300)
    quartos = rng.integers(1, 5, 300)
    X = np.column_stack([area, quartos])
    y = 50000 + 2000 * area + 12000 * quartos + rng.normal(0, 15000, 300)
    X_dev, X_test, y_dev, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)
    scores = {}
    for name, model in {
        "baseline_media": DummyRegressor(strategy="mean"),
        "ridge": make_pipeline(StandardScaler(), Ridge(alpha=1)),
    }.items():
        model.fit(X_dev, y_dev)
        scores[name] = {"mae_reais": float(mean_absolute_error(y_test, model.predict(X_test)))}
    return scores


def cancelamento():
    X, y = make_classification(n_samples=600, n_features=8, n_informative=5,
                              n_redundant=1, weights=[0.8, 0.2], class_sep=1.2, random_state=SEED)
    X_dev, X_test, y_dev, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=SEED)
    pipeline = Pipeline([("escala", StandardScaler()), ("modelo", LogisticRegression(max_iter=1000))])
    cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=SEED)
    search = GridSearchCV(pipeline, {"modelo__C": [0.01, 0.1, 1, 10]}, cv=cv, scoring="f1")
    search.fit(X_dev, y_dev)
    models = {
        "baseline_majoritaria": DummyClassifier(strategy="most_frequent"),
        "logistica_ajustada": search.best_estimator_,
        "knn": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=7)),
        "svm_rbf": make_pipeline(StandardScaler(), SVC(C=1, gamma="scale")),
        "naive_bayes": GaussianNB(),
        "arvore": DecisionTreeClassifier(max_depth=5, min_samples_leaf=5, random_state=SEED),
        "floresta": RandomForestClassifier(n_estimators=100, max_depth=8, min_samples_leaf=3, random_state=SEED),
        "boosting": HistGradientBoostingClassifier(max_iter=100, learning_rate=0.1, max_leaf_nodes=15, random_state=SEED),
        "mlp": make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(32, 16), alpha=0.001,
                                                             learning_rate_init=0.001, max_iter=1500, random_state=SEED)),
    }
    scores = {}
    for name, model in models.items():
        if name != "logistica_ajustada":
            model.fit(X_dev, y_dev)
        prediction = model.predict(X_test)
        scores[name] = {
            "precision": float(precision_score(y_test, prediction, zero_division=0)),
            "recall": float(recall_score(y_test, prediction, zero_division=0)),
            "f1": float(f1_score(y_test, prediction, zero_division=0)),
        }
    return {"melhor_C_no_desenvolvimento": search.best_params_["modelo__C"], "teste": scores}


def clientes():
    X, reference = make_blobs(n_samples=300, centers=[[3, 200], [15, 500], [10, 1700]],
                             cluster_std=0.6, random_state=SEED)
    # Ajusta a dispersão de gasto sem mudar os centros dos grupos.
    centers = np.array([[3, 200], [15, 500], [10, 1700]])
    X[:, 1] = centers[reference, 1] + 100 * (X[:, 1] - centers[reference, 1])
    scaler = StandardScaler()
    scaled = scaler.fit_transform(X)
    model = KMeans(n_clusters=3, n_init=10, random_state=SEED)
    labels = model.fit_predict(scaled)
    return {"centroides_unidades_originais": scaler.inverse_transform(model.cluster_centers_).tolist(),
            "silhouette": float(silhouette_score(scaled, labels)),
            "ari_referencia_sintetica": float(adjusted_rand_score(reference, labels))}


def reducao():
    X, y = make_classification(n_samples=400, n_features=15, n_informative=4,
                              n_redundant=8, random_state=SEED)
    X_dev, X_test, y_dev, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=SEED)
    model = make_pipeline(StandardScaler(), PCA(n_components=0.95, svd_solver="full"),
                          LogisticRegression(max_iter=1000))
    model.fit(X_dev, y_dev)
    baseline = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(X_dev, y_dev)
    pca = model.named_steps["pca"]
    return {"features_originais": 15, "componentes": int(pca.n_components_),
            "variancia_retida": float(pca.explained_variance_ratio_.sum()),
            "f1_com_pca": float(f1_score(y_test, model.predict(X_test))),
            "f1_sem_pca": float(f1_score(y_test, baseline.predict(X_test)))}


def temporal():
    rng = np.random.default_rng(SEED)
    dias = np.arange(180)
    X = dias.reshape(-1, 1)
    y = 20 + 0.05 * dias + rng.normal(0, 0.5, len(dias))
    X_dev, X_test, y_dev, y_test = X[:150], X[150:], y[:150], y[150:]
    search = GridSearchCV(make_pipeline(StandardScaler(), Ridge()),
                          {"ridge__alpha": [0.01, 0.1, 1, 10]},
                          cv=TimeSeriesSplit(n_splits=4), scoring="neg_mean_absolute_error")
    search.fit(X_dev, y_dev)
    return {"dias_treino": 150, "dias_teste": 30, "alpha": search.best_params_["ridge__alpha"],
            "mae_modelo": float(mean_absolute_error(y_test, search.predict(X_test))),
            "mae_baseline_ultimo_valor": float(mean_absolute_error(y_test, np.full(30, y_dev[-1])))}


def reforco():
    rng = np.random.default_rng(SEED)
    q = np.zeros((5, 2))
    alpha, gamma, epsilon = 0.3, 0.9, 0.2
    # Linha com cinco estados. Ações 0=esquerda, 1=direita; estado 4 é terminal.
    for _ in range(500):
        state = 0
        for _ in range(50):
            if rng.random() < epsilon:
                action = int(rng.integers(2))
            else:
                best = np.flatnonzero(q[state] == q[state].max())
                action = int(rng.choice(best))
            next_state = int(np.clip(state + (-1 if action == 0 else 1), 0, 4))
            terminal = next_state == 4
            reward = 1.0 if terminal else -0.01
            future = 0.0 if terminal else float(q[next_state].max())
            q[state, action] += alpha * (reward + gamma * future - q[state, action])
            state = next_state
            if terminal:
                break
    state, trajectory = 0, [0]
    for _ in range(10):
        action = int(q[state].argmax())
        state = int(np.clip(state + (-1 if action == 0 else 1), 0, 4))
        trajectory.append(state)
        if state == 4:
            break
    return {"q": q.tolist(), "trajetoria_gulosa": trajectory, "chegou_ao_objetivo": state == 4}


def main():
    results = {"ambiente": {"sklearn": sklearn.__version__, "numpy": np.__version__, "seed": SEED},
               "imoveis": imoveis(), "cancelamento": cancelamento(), "clientes": clientes(),
               "reducao": reducao(), "temporal": temporal(), "reforco": reforco()}
    assert results["reforco"]["chegou_ao_objetivo"], "A política não chegou ao terminal."
    output = Path(__file__).with_name("resultados.json")
    output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
