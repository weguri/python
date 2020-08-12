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
Tanto: Método e Atributo são privados, 
        mais no python de uma certa forma tudo é publico
"""

p1 = FortementePrivados()

#
# Acessando Método PRIVADO Fortemente
p1._FortementePrivados__metodo_fortemente_privado()

#
# Acessando atributo PRIVADO Fortemente
print(p1._FortementePrivados__atributo_fortemente_privado)
