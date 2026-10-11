"""Recalcula as contas dos estudos 01 a 12, sem depender dos resultados salvos."""
import json
from pathlib import Path
import numpy as np
from sklearn.metrics import mean_absolute_error, precision_score, recall_score, accuracy_score

ROOT = Path(__file__).resolve().parents[1]


def calcular():
    truth = [1] * 12 + [0] * 2
    predicted = [1] * 8 + [0] * 4 + [1] * 2
    current, alpha, reward, gamma, future = 2, .5, 3, .9, 4
    return {
        'fund_z': (5000-3000)/1000,
        'fund_classe_rara': [accuracy_score([1]*10+[0]*990, [0]*1000), recall_score([1]*10+[0]*990, [0]*1000)],
        'fund_precision_recall': [precision_score(truth, predicted), recall_score(truth, predicted)],
        'fund_mae': mean_absolute_error([10, 20], [12, 17]),
        'fund_preco': 50000+2000*60,
        'fund_limiar': int(.7 >= .8),
        'fund_grade': 3*4*5,
        'fund_batches': 1000//100,
        'fund_retorno': 2+.5*4,
        'fund_qlearning': current+alpha*(reward+gamma*future-current),
        'fund_divisao': [180-30, 30],
    }


def main():
    calculated = {k: np.asarray(v).tolist() for k, v in calcular().items()}
    modules = json.loads((ROOT/'fontes/cartoes.json').read_text(encoding='utf-8'))['modulos']
    checks = [c['verificacao_fundamentos'] for m in modules for c in m['cartoes'] if 'verificacao_fundamentos' in c]
    assert len(checks) == len(calculated) == len({c['id'] for c in checks})
    assert {c['id'] for c in checks} == set(calculated)
    for check in checks:
        np.testing.assert_allclose(calculated[check['id']], check['esperado'], rtol=0, atol=1e-10, err_msg=check['id'])
    (ROOT/'exemplos/resultados_fundamentos.json').write_text(json.dumps({'calculados':calculated,'verificados':len(checks)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'{len(checks)} exercícios de fundamentos verificados.')


if __name__ == '__main__':
    main()
