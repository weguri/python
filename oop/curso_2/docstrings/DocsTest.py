class DocsTest:
    """
    Class Para exemplificar o Docstrings
    """
    lista = list()
    """ Lista de dados"""

    tupla = tuple()

    def __init__(self, nomes, valores):
        """
        Docstring dentro do metodo construtor
        :param nomes: string
        :param valores: int
        """
        pass

    def inserir(self, id):
        """
        Metodo para inserção de dados
        :param id:
        :return: boolean
        """
        pass

    def atualizar(self):
        pass

    def deletar(self):
        pass


dt = DocsTest("Sergio", 3333)
dt.inserir(1)

# print(dt.__doc__)  # Aqui vai exibir somente a documentação da class
help(dt)  # Mostra toda classe e seus metodos
