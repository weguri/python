class Veiculo:
    pass


class Carro(Veiculo):
    pass


class Trem(Veiculo):
    pass


class CarroTrem(Carro, Trem):
    pass


"""
MRO - method resolution order
    (ordem de resolução do método)

mro() - retorna uma lista
__mro__ - retorna uma tupla
"""

print(Veiculo.mro())
print(Carro.__mro__)
print(CarroTrem.__mro__)