# Chama os metodos individuas
# from oop.curso_2.sintaxe.poligono import Quadrado
# from oop.curso_2.sintaxe.poligono import Retangulo

# Importar as duas classes em uma Linha, sendo do mesmo arquivo
from oop.curso_2.sintaxe.poligono import Quadrado, Retangulo

# Chamada univerval
# from oop.curso_2.sintaxe.poligono import *

# Classe
q = Quadrado(5)
print("Quadrado:", q.perimetro(), q.area(), sep="\n\n")


# Classe
r = Retangulo(5, 10)
print("Retangulo", r.area())
