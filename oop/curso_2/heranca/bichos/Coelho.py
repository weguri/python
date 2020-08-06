from oop.curso_2.heranca.bichos.animal import Animal


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)