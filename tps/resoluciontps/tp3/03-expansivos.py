import unittest
import numpy as np

def expand(arreglo: np.ndarray) -> np.ndarray:
    resultado = []
    cifra_actual = arreglo[0]
    contador = 1
    for i in range(1, len(arreglo)):
        if arreglo[i] == cifra_actual:
            contador += 1
        else:
            resultado.append(contador)
            resultado.append(cifra_actual)
            cifra_actual = arreglo[i]
            contador = 1
    resultado.append(contador)
    resultado.append(cifra_actual)
    return np.array(resultado)


def list2num(arreglo: np.ndarray) -> int:
    numero = 0
    for cifra in arreglo:
        numero = numero * 10 + cifra
    return numero


class TestExpansivos(unittest.TestCase):
    def test_expand(self):
        np.testing.assert_array_equal(expand(np.array([1])), np.array([1, 1]))
        np.testing.assert_array_equal(expand(np.array([1, 1])), np.array([2, 1]))
        np.testing.assert_array_equal(expand(np.array([2, 1])), np.array([1, 2, 1, 1]))
        np.testing.assert_array_equal(expand(np.array([1, 2, 1, 1])), np.array([1, 1, 1, 2, 2, 1]))

    def testList2num(self):
        self.assertEqual(list2num(np.array([1, 1])), 11)
        self.assertEqual(list2num(np.array([2, 1])), 21)
        self.assertEqual(list2num(np.array([1, 2, 1, 1])), 1211)
        self.assertEqual(list2num(np.array([1, 1, 1, 2, 2, 1])), 111221)


if __name__ == "__main__":
    unittest.main()