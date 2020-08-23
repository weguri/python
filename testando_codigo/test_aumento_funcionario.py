import unittest
from testando_codigo.aumento_funcionario import DarAumentoFuncionario


class TestDarAumentoFuncionario(unittest.TestCase):
    """Testes para a classe DarAumentoFuncionario"""

    def setUp(self) -> None:
        self.aumento_funcionario = DarAumentoFuncionario('José', 2.123)

    def test_aumento(self):
        self.aumento_funcionario.dar_aumento()

    def test_exibir(self):
        self.assertEqual(self.aumento_funcionario.exibir,
                         'José, seu novo salário é R$ 7503.18')


if __name__ == "__main__":
    unittest.main()
