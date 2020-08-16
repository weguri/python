from collections import namedtuple

com_classe = namedtuple('Pessoas', 'nome class idade genero', rename=True)
print(com_classe._fields)

duas_idades = namedtuple('Pessoas', 'nome idade genero idade', rename=True)
print(duas_idades._fields)

