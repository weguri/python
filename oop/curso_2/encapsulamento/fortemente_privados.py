class FortementePrivados:
    """
    Métodos e atributos fortemente privados tem um duplo sublinhado
        'underline' (__) no inicio de seus nomes
    """

    def __init__(self):
        self.__atributo_fortemente_privado = 520741

    def __metodo_fortemente_privado(self):
        print("Método Fortemente privado")


"""
Acessando os itens fortemente privados utilizando o método padrão de acesso.
Tanto: Método e Atributo são privados, se tentar acessar gera um erro
"""

p1 = FortementePrivados()

print(dir(p1))

#
# Error: AttributeError
# p1.__metodo_fortemente_privado()

#
# Erro: AttributeError
# p1.__atributo_fortemente_privado
