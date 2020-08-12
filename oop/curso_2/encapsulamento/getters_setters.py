"""
Getters (também conhecidos como 'acessadores')
Setters (também conhecidos como 'mutators')

@property
    seria: Getters

@variavel.setter
    seria: Setters
"""


class P:
    """
    Maneira Pythonic de fazer
    """
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


"""
Exemplo de Uso
Quando atribui um valor automaticamente o metodo x.setter 
"""
#
# Valor maior 1000 vai sempre retorna 1000
vrs = P(2000)
print(vrs.x)

#
# Menor que 1000 retorna o proprio valor
vrs.x = 100
print(vrs.x)

#
# Menor que zero, retorna zero
vrs.x = -2
print(vrs.x)
