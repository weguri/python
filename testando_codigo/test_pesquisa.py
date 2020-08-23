import unittest
from testando_codigo.pesquisa import PesquisaAnonima

"""
setUp
    Executa esse metodo antes de qualquer outro.

    Como este metodo é executado primeiro, então deve ser
    criar as varias ou instancia da classe para poder ser 
    utilizada nos outros metodos.

assertIn
    Verificar se item está em lista
    Para conferir se a resposta está na lista
    de respostas depois que ela for armazenada
"""


class TestPesquisaAnonima(unittest.TestCase):
    """Testes para a classe PesquisaAnonima"""

    def setUp(self):
        """
        Crie uma pesquisa e um conjunto de respostas para uso em todos os métodos de teste.
        """
        questao = "Qual idioma você aprendeu primeiro a falar?"

        # Criar uma instância da classe
        self.minha_pesquisa = PesquisaAnonima(questao)
        self.respostas = ['English', 'Spanish', 'Mandarin']

    def test_armazenar_resposta_unica(self):
        """
        Teste se uma única resposta está armazenada corretamente.
        """
        self.minha_pesquisa.armazenar_resposta(self.respostas[0])
        self.assertIn(self.respostas[0], self.minha_pesquisa.respostas)

    def test_armazenar_tres_respostas(self):
        """
        Teste se três respostas individuais estão armazenadas corretamente.
        """
        for resposta in self.respostas:
            self.minha_pesquisa.armazenar_resposta(resposta)

        for resposta in self.respostas:
            self.assertIn(resposta, self.minha_pesquisa.respostas)


if __name__ == '__main__':
    unittest.main()
