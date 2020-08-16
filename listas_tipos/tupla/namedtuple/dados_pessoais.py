from collections import namedtuple

""" Mapear nomes a elemento de sequência """

Humano = namedtuple("Pessoa", 'nome idade, genero')

print("Tipo de pessoa:", type(Humano))

maria = Humano(nome="Maria", idade=22, genero="Mulher")

print(maria)
print(maria.nome)
