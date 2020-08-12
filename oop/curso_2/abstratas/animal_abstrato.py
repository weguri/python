from abc import ABCMeta, abstractmethod


class AnimalAbstrato(metaclass=ABCMeta):

    @abstractmethod
    def som_animal(self) -> str:
        return "Som do animal"


class Cachorro(AnimalAbstrato):

    def som_animal(self) -> str:
        frase = super(Cachorro, self).som_animal()
        return f"{frase} cachorro é: AU AU"


cao = Cachorro()
print(cao.som_animal())
