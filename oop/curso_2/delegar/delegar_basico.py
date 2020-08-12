class Recendo:
    __dividido = []

    def faz_split(self, txt):
        self.__dividido = txt.split()

    def exibir(self):
        return self.__dividido


class Delegando:
    def __init__(self):
        """
        Instância da classe Recendo()
        """
        self.cls = Recendo()

    def texto(self, frs):
        """
        Acessando o metodo da outra classe
        Isso seria forma delegar o processo para outra classe
        """
        self.cls.faz_split(frs)

    def saida_split(self):
        return self.cls.exibir()  # delegando para classe Recendo


"""
Fazendo teste
"""

delegar = Delegando()
delegar.texto("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

lista = delegar.saida_split()

print(lista)
