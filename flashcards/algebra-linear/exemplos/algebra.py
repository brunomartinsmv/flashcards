"""Resolve os exercícios numéricos da coleção de álgebra linear."""
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def calcular():
    v = np.array([3., 4.])
    a = np.array([[1., 2.], [0., 1.]])
    x = np.array([2., 0.])
    diagonal = np.array([1., 1.])
    matrix = np.diag([3., 1.])
    u, singular, vt = np.linalg.svd(matrix)
    truncated = singular[0] * np.outer(u[:, 0], vt[0, :])
    return {
        'al_soma': np.array([1, 2]) + np.array([3, -1]),
        'al_escalar': -2 * np.array([1, -3]),
        'al_combinacao': 2*np.array([1, 0])+3*np.array([0, 1]),
        'al_produto_interno': np.dot([1, 2], [3, 4]),
        'al_norma': np.linalg.norm(v),
        'al_unitario': v / np.linalg.norm(v),
        'al_angulo': np.degrees(np.arccos(np.dot([1, 0], [0, 1]))),
        'al_distancia': np.linalg.norm(np.array([4, 5])-np.array([1, 1])),
        'al_dimensao_produto': (np.zeros((2, 3)) @ np.zeros((3, 4))).shape,
        'al_ax': a @ np.array([3, 4]),
        'al_ab': a @ np.array([[2, 0], [1, 3]]),
        'al_transposta': np.array([[1, 2, 3], [4, 5, 6]]).T,
        'al_traco': np.trace([[2, 5], [1, 3]]),
        'al_rotacao': np.array([[0, -1], [1, 0]]) @ np.array([2, 1]),
        'al_sistema': np.linalg.solve([[1, 1], [1, -1]], [3, 1]),
        'al_posto': np.linalg.matrix_rank([[1, 2], [2, 4]]),
        'al_inversa': np.linalg.inv(np.diag([2., 4.])),
        'al_determinante': np.linalg.det([[1, 2], [3, 4]]),
        'al_coordenadas': np.linalg.solve([[1, 1], [1, -1]], [2, 0]),
        'al_nulidade': 5 - np.linalg.matrix_rank(np.column_stack((np.eye(3), np.zeros((3, 2))))),
        'al_projecao': np.dot(v, [1, 0]) * np.array([1, 0]),
        'al_projecao_diagonal': (x @ diagonal)/(diagonal @ diagonal)*diagonal,
        'al_gram_schmidt': diagonal - (diagonal @ np.array([1, 0])) * np.array([1, 0]),
        'al_minimos_constante': np.linalg.lstsq(np.ones((3, 1)), [1, 2, 3], rcond=None)[0][0],
        'al_minimos_reta': np.linalg.lstsq([[1, 0], [1, 1], [1, 2]], [1, 2, 3], rcond=None)[0],
        'al_pseudoinversa': np.linalg.pinv(np.diag([2., 0.])),
        'al_autovalor': (np.diag([2, 3]) @ np.array([1, 0]))[0],
        'al_autovalores': np.linalg.eigvalsh([[2, 1], [1, 2]]),
        'al_forma_quadratica': np.array([1, 2]) @ np.diag([2, 3]) @ np.array([1, 2]),
        'al_singulares': singular,
        'al_svd_truncada': truncated,
        'al_erro_svd': np.linalg.norm(matrix - truncated, 'fro'),
        'al_condicao': np.linalg.cond(np.diag([1., .001]), 2),
    }


def main():
    calculated = {k: np.asarray(v).tolist() for k, v in calcular().items()}
    modules = json.loads((ROOT / 'fontes/cartoes.json').read_text())['modulos']
    checks = [c['verificacao_nucleo'] for m in modules for c in m['cartoes'] if 'verificacao_nucleo' in c]
    assert len(checks) == len(calculated) == len({c['id'] for c in checks})
    assert {c['id'] for c in checks} == set(calculated)
    for c in checks:
        np.testing.assert_allclose(calculated[c['id']], c['esperado'], rtol=1e-10, atol=1e-10, err_msg=c['id'])
    report = {'calculados': calculated, 'verificados': len(checks), 'numpy': np.__version__}
    (ROOT / 'exemplos/resultados.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(f'{len(checks)} exercícios de álgebra linear verificados.')


if __name__ == '__main__':
    main()
