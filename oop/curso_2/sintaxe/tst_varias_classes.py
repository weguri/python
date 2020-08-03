# Chama os metodos individuas
from oop.curso_2.sintaxe.varias_classes import Quadrado
from oop.curso_2.sintaxe.varias_classes import Retangulo

# Chamada univerval 
# from oop.curso_2.sintaxe.varias_classes import *


q = Quadrado(5)
print(
    "Quadrado:",
    q.perimetro(),
    q.area(),
    sep="\n"
)


r = Retangulo(5, 10)

print("Retangulo", r.area())