from oop.curso_2.Polimorfismo.formageometrica.circulo import Circulo
from oop.curso_2.Polimorfismo.formageometrica.quadrado import Quadrado

quad = Quadrado(2)
print("Area: %d" % quad.area())
print("Perimetro: %d" % quad.perimetro())

print('-' * 30)

circulo = Circulo(2)
print("Area: %d" % circulo.area())
print("Perimetro: %d" % circulo.perimetro())
