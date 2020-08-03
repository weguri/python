class Sintaxe:
    pass

s = Sintaxe()

s.x = 5
s.y = 22
s.curso = "Python"

print(s.curso)

""" 
Listado os recusos da Classe Sintaxe, 
Vai aparecer os atributos x, y e curso
Estes atributos foram criados fora da class
"""
dir(s)