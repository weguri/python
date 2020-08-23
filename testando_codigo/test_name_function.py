import unittest
from unittest.main import main
from testando_codigo.nome_function import obter_nome_formatado

"""
assertEqual
    Verifica se a == b
"""


class NamesTestCase(unittest.TestCase):
    """Testes para 'nome_function.py'"""

    def test_primeiro_segundo_nome(self):
        """Nomes como 'Jessica Martins Oliveira' funcionam?"""

        nome_formatado = obter_nome_formatado('Jessica', 'Martins')
        self.assertEqual(nome_formatado, 'Jessica Martins')

    def test_nome_meio_ultimo(self):
        """ Nomes como 'Jessica Martins Oliveira' funcionam? """

        nome_formatado = obter_nome_formatado('Jessica', 'Martins', 'Oliveira')
        self.assertEqual(nome_formatado, 'Jessica Martins Oliveira')


if __name__ == "__main__":
    unittest.main()
