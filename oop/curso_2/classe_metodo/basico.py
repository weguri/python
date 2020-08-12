"""
Para se criar métodos que pertençam à classe, e não ao objeto,
pode-se usar os decoradores:
    @staticmethod
    ou
    @classmethod

    Ambos são semelhantes, embora o primeiro não faça referência alguma à classe e o segundo o faça
"""


class Exemplo:
    @staticmethod
    def testar_staticmethod(a, b, c):
        pass

    @classmethod
    def testar_classmethod(cls, a, b, c):
        pass


"""
Testar Exemplo
"""
Exemplo.testar_staticmethod(1, 2, 3)  # Os argumentos são 1, 2 e 3
Exemplo.testar_classmethod(1, 2, 3)  # Os argumentos são Foo, 1, 2 e 3

#
# Também se pode chamar métodos de classe a partir de uma instância
x = Exemplo()
x.testar_staticmethod(1, 2, 3)  # Os argumentos são 1, 2 e 3
x.testar_classmethod(1, 2, 3)  # Os argumentos são Foo, 1, 2 e 3
