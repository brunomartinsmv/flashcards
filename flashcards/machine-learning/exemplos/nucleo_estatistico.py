"""Recalcula os exercícios dos estudos 22 a 26 com NumPy e SciPy."""
import json
from pathlib import Path
import numpy as np
import scipy
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]


def calcular():
    covariance = np.array([[4., 2.], [2., 9.]])
    x = np.array([2., 1.])
    return {
        "prob_uniao": .4 + .3 - .1,
        "prob_marginal": .2 + .3,
        "prob_total": .8 * .25 + .2 * .75,
        "prob_uniforme": stats.uniform(0, 10).cdf(5) - stats.uniform(0, 10).cdf(2),
        "prob_variancia_soma": 4 + 9 + 2 * 2,
        "prob_sem_reposicao": stats.hypergeom.pmf(2, 5, 3, 2),
        "inf_eqm": 2**2 + 3,
        "inf_mle": np.mean([1, 1, 1, 1, 0]),
        "inf_t": stats.ttest_1samp([1, 2, 1, 2], 0).statistic,
        "inf_chi2": stats.chi2_contingency([[10, 10], [10, 10]], correction=False).statistic,
        "inf_anova": stats.f_oneway([1, 2, 3], [4, 5, 6], [7, 8, 9]).statistic,
        "ts_diferenca": np.diff([10, 13, 12, 16]),
        "ts_sazonal": np.array([10, 11, 12]) - np.array([1, 2, 3]),
        "ts_ar1": 1 + .5 * 4,
        "ts_ar2": 1 + .5 * (1 + .5 * 4),
        "ts_suavizacao": .2 * 20 + .8 * 10,
        "mv_correlacao": covariance[0, 1] / np.sqrt(covariance[0, 0] * covariance[1, 1]),
        "mv_mahalanobis": np.sqrt(x @ np.linalg.solve(np.diag([4., 1.]), x)),
        "mv_pca": np.max(np.linalg.eigvalsh(np.diag([9., 1.]))) / 10,
        "bayes_parametros": np.array([2, 2]) + np.array([6, 2]),
        "bayes_media": stats.beta.mean(8, 4),
        "bayes_variancia": stats.beta.var(8, 4),
        "bayes_preditiva": stats.betabinom.mean(1, 8, 4),
        "bayes_map": (8 - 1) / (8 + 4 - 2),
    }


def main():
    calculated = {k: np.asarray(v).tolist() for k, v in calcular().items()}
    modules = json.loads((ROOT / 'fontes/nucleo_estatistico.json').read_text())['modulos']
    checks = [c['verificacao_nucleo'] for m in modules for c in m['cartoes'] if 'verificacao_nucleo' in c]
    assert len(checks) == len(calculated) == len({c['id'] for c in checks})
    assert {c['id'] for c in checks} == set(calculated)
    for c in checks:
        np.testing.assert_allclose(calculated[c['id']], c['esperado'], rtol=1e-10, atol=1e-10, err_msg=c['id'])
    report = {'calculados': calculated, 'verificados': len(checks), 'numpy': np.__version__, 'scipy': scipy.__version__}
    (ROOT / 'exemplos/resultados_nucleo.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(f'{len(checks)} exercícios estatísticos verificados.')


if __name__ == '__main__':
    main()
