""" 
Possibilidade de criar varias classes no mesmo arquivo
Quando importa este arquivo é outro pode informar todas classes
ou informa somente a classe que vai ser usada
"""


class Quadrado:
    """
    Calcular a area do quadrado
    """
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado * self.lado


class Retangulo:
    """ 
    Calcular area do retangulo
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
