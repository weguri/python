from oop.curso_2.heranca.bichos.animal import Animal


class Gato(Animal):
    def __init__(self, nome, cor, som):
        super().__init__(nome, cor)
        self.som = som
