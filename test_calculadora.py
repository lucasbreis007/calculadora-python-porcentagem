import unittest
from calculadora import somar, subtrair, multiplicar, dividir, calcular_porcentagem

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-2, 3), 1)
        self.assertAlmostEqual(somar(2.5, 3.1), 5.6)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)
        self.assertEqual(subtrair(5, 10), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(7, 8), 56)
        self.assertEqual(multiplicar(-3, 4), -12)
        self.assertEqual(multiplicar(5, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(7, 2), 3.5)

    def test_divisao_por_zero(self):
        resultado = dividir(10, 0)
        self.assertIn("Erro", resultado)

    def test_calcular_porcentagem(self):
        # 15% de 200 = 30
        self.assertEqual(calcular_porcentagem(200, 15), 30.0)
        # 50% de 80 = 40
        self.assertEqual(calcular_porcentagem(80, 50), 40.0)
        # 100% de 99.5 = 99.5
        self.assertEqual(calcular_porcentagem(99.5, 100), 99.5)
        # 0% de 50 = 0
        self.assertEqual(calcular_porcentagem(50, 0), 0.0)

if __name__ == "__main__":
    unittest.main()
