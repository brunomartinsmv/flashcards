"""Recalcula os exemplos numéricos com NumPy, SciPy e scikit-learn."""

import json
from pathlib import Path

import numpy as np
import scipy
from scipy import special, stats
import sklearn
from sklearn import metrics as sk


ROOT = Path(__file__).resolve().parents[1]


def calculate():
    results = {
        "media": np.mean([2, 4, 6]), "mediana": np.median([1, 2, 3, 100]),
        "variancia": np.var([2, 4, 6], ddof=1), "desvio": np.std([2, 4, 6], ddof=1),
        "iqr": np.subtract(18, 10), "mad": stats.median_abs_deviation([1, 2, 3, 100]),
        "cv": np.divide(10, 50), "correlacao": stats.pearsonr([1, 2, 3], [2, 4, 6]).statistic,
        "condicional": np.divide(5, 20), "independencia": 0.2 * 0.3,
        "bayes": 0.9 * 0.01 / (0.9 * 0.01 + 0.1 * 0.99),
        "esperanca": np.average([0, 10], weights=[0.7, 0.3]), "binomial": stats.binom.mean(10, 0.2),
        "entropia": stats.entropy([0.5, 0.5], base=2), "erro_padrao": 10 / np.sqrt(25),
        "ic_superior": 50 + 1.96 * 2, "poder": 1 - 0.2, "bonferroni": 0.05 / 10,
    }
    y, pred = np.array([2., 4.]), np.array([3., 2.])
    error = pred - y
    results.update({
        "mae": sk.mean_absolute_error(y, pred), "mse": sk.mean_squared_error(y, pred),
        "rmse": np.sqrt(sk.mean_squared_error(y, pred)), "medae": sk.median_absolute_error([0, 0, 0], [1, 2, 100]),
        "max_error": sk.max_error(y, pred), "me": np.mean(error), "mape": sk.mean_absolute_percentage_error(y, pred),
        "smape": np.mean(2 * np.abs(error) / (np.abs(y) + np.abs(pred))),
        "wape": np.sum(np.abs(error)) / np.sum(np.abs(y)), "r2": sk.r2_score(y, pred),
        "r2_ajustado": 1 - (1 - 0.8) * (10 - 1) / (10 - 2 - 1),
        "ev": sk.explained_variance_score(y, y + 10),
        "rmsle": np.sqrt(sk.mean_squared_log_error([1], [3])),
        "pinball": sk.mean_pinball_loss([10], [8], alpha=0.9),
        "poisson": sk.mean_poisson_deviance([2], [1]), "gamma": sk.mean_gamma_deviance([2], [1]),
        "tweedie": sk.mean_tweedie_deviance(y, pred, power=0), "huber": np.mean(special.huber(1, [1, -2])),
    })
    # O vetor reproduz a matriz [[55,5],[10,30]], com classe positiva 1.
    truth = np.array([1] * 40 + [0] * 60)
    prediction = np.array([1] * 30 + [0] * 10 + [1] * 5 + [0] * 55)
    tn, fp, fn, tp = sk.confusion_matrix(truth, prediction, labels=[0, 1]).ravel()
    results.update({
        "accuracy": sk.accuracy_score(truth, prediction), "precision": sk.precision_score(truth, prediction),
        "recall": sk.recall_score(truth, prediction), "specificity": sk.recall_score(truth, prediction, pos_label=0),
        "npv": sk.precision_score(truth, prediction, pos_label=0), "fpr": fp / (fp + tn),
        "fnr": fn / (fn + tp), "fdr": fp / (fp + tp), "balanced_accuracy": sk.balanced_accuracy_score(truth, prediction),
        "f1": sk.f1_score(truth, prediction), "f2": sk.fbeta_score(truth, prediction, beta=2),
        "mcc": sk.matthews_corrcoef(truth, prediction), "kappa": sk.cohen_kappa_score(truth, prediction),
        "prevalence": np.mean(truth), "cost": (2 * fp + 10 * fn) / len(truth),
    })
    precision, recall, _ = sk.precision_recall_curve([1, 0, 1], [0.9, 0.8, 0.6])
    brier = sk.brier_score_loss([1, 0], [0.8, 0.3])
    macro_truth = [0] * 10 + [1] * 2
    macro_pred = [0] * 8 + [1] * 2 + [0, 1]
    multi_truth = [[1, 1, 0], [0, 1, 0]]
    multi_pred = [[1, 0, 0], [0, 1, 1]]
    results.update({
        "roc_auc": sk.roc_auc_score([1, 1, 0, 0], [0.9, 0.6, 0.8, 0.2]),
        "pr_auc": sk.auc(recall, precision), "ap": sk.average_precision_score([1, 0, 1], [0.9, 0.8, 0.6]),
        "log_loss": sk.log_loss([1, 0], [0.8, 0.3]), "brier": brier, "bss": 1 - brier / 0.25,
        "ece": abs(np.mean([0.8] * 10) - np.mean([1] * 6 + [0] * 4)),
        "multiclass_log_loss": sk.log_loss([1], [[0.1, 0.7, 0.2]], labels=[0, 1, 2]),
        "top_k": sk.top_k_accuracy_score([1], [[0.6, 0.3, 0.1]], k=2, labels=[0, 1, 2]),
        "macro_recall": sk.recall_score(macro_truth, macro_pred, average="macro"),
        "macro_f1": sk.f1_score(macro_truth, macro_pred, average="macro"),
        "weighted_f1": sk.f1_score(macro_truth, macro_pred, average="weighted"),
        "micro_f1": sk.f1_score(macro_truth, macro_pred, average="micro"),
        "jaccard": sk.jaccard_score([[1, 1, 0]], [[0, 1, 1]], average="samples"),
        "hamming": sk.hamming_loss(multi_truth, multi_pred), "subset_accuracy": sk.accuracy_score(multi_truth, multi_pred),
        "samples_f1": sk.f1_score(multi_truth, multi_pred, average="samples"),
    })
    reference, crossed = [0, 0, 1, 1], [0, 1, 0, 1]
    db_points, db_labels = np.array([[-1], [1], [4], [8]]), [0, 0, 1, 1]
    # a e b são resumos fornecidos no enunciado, não dados brutos de um dataset.
    results.update({
        "silhouette": (5 - 2) / max(2, 5), "db": sk.davies_bouldin_score(db_points, db_labels),
        "ch": (100 / (2 - 1)) / (20 / (12 - 2)), "inertia": np.sum((np.array([0, 2]) - 1) ** 2),
        "ri": sk.rand_score(reference, crossed), "ari": sk.adjusted_rand_score(reference, crossed),
        "nmi": sk.normalized_mutual_info_score(reference, crossed, average_method="arithmetic"),
        "ami": sk.adjusted_mutual_info_score(reference, [1, 1, 0, 0]),
        "homogeneity": sk.homogeneity_score(reference, [0, 1, 2, 3]),
        "completeness": sk.completeness_score(reference, [0, 0, 0, 0]), "v_measure": 2 * 1 * 0.5 / (1 + 0.5),
        "purity": (max([2, 1]) + max([2, 1])) / 6,
    })
    label_truth, label_scores = [[1, 0, 1]], [[0.9, 0.8, 0.6]]
    results.update({
        "precision_k": np.mean([1, 0, 1]), "recall_k": np.sum([1, 0, 1]) / 4,
        "hit_rate": np.mean([1, 1, 0]), "mrr": np.mean(1 / np.array([2, 4])),
        "map": np.mean([sk.average_precision_score([1, 0, 1], [0.9, 0.8, 0.6]),
                        sk.average_precision_score([0, 1, 0], [0.9, 0.8, 0.6])]),
        "ndcg": sk.ndcg_score([[0, 1]], [[0.9, 0.6]], k=2),
        "ranking_loss": sk.label_ranking_loss(label_truth, label_scores),
        "coverage_error": sk.coverage_error(label_truth, label_scores),
        "lrap": sk.label_ranking_average_precision_score(label_truth, label_scores),
    })
    train_diff = np.diff([1., 3., 2.])
    random_hits = (tp + fp) * (tp + fn) / len(truth)
    intervals = np.array([[0, 2], [3, 7]])
    results.update({
        "mase": 1.5 / np.mean(np.abs(train_diff)), "rmsse": np.sqrt(2.5 / np.mean(train_diff ** 2)),
        "skill": 1 - 3 / 5, "pod": sk.recall_score(truth, prediction),
        "csi": sk.jaccard_score(truth, prediction), "ets": (tp - random_hits) / (tp + fp + fn - random_hits),
        "picp": np.mean([True] * 9 + [False]), "mpiw": np.mean(intervals[:, 1] - intervals[:, 0]),
        "interval_score": (6 - 2) + (2 / 0.2) * max(8 - 6, 0),
        "crps": np.mean(np.abs(np.array([3.]) - 5)) - 0.5 * np.mean(np.abs(np.array([[3.]]) - np.array([3.]))),
        "return_mean": np.mean([1, 3, 2]), "success_rate": np.mean([True] * 15 + [False] * 5),
    })
    return {key: float(value) for key, value in results.items()}


def main():
    calculated = calculate()
    data = json.loads((ROOT / "fontes/estatistica_metricas.json").read_text(encoding="utf-8"))
    checks = [c["verificacao"] for m in data["modulos"] for c in m["cartoes"] if "verificacao" in c]
    assert set(calculated) == {c["id"] for c in checks}, "Há exemplos sem cálculo ou cálculos sem cartão."
    for check in checks:
        np.testing.assert_allclose(calculated[check["id"]], check["esperado"], rtol=0, atol=1e-10, err_msg=check["id"])
    results = {"ambiente": {"numpy": np.__version__, "scipy": scipy.__version__, "sklearn": sklearn.__version__},
               "exemplos_verificados": len(checks), "calculados": calculated}
    Path(__file__).with_name("resultados_metricas.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Verificados {len(checks)} exemplos numéricos de estatística e métricas.")


if __name__ == "__main__":
    main()
