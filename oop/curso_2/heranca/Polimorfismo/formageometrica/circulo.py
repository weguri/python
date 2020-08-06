import math

from oop.curso_2.heranca.Polimorfismo.formageometrica.forma import Forma


class Circulo(Forma):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio
