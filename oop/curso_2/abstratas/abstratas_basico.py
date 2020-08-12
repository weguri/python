from abc import ABC, abstractmethod


class AbstratoExemplo(ABC):
    def __init__(self, valor):
        self.valor = valor
        super().__init__()

    @abstractmethod
    def execute_algo(self):
        print("print da classe AbstratoExemplo")


class FilhaAbstrato(AbstratoExemplo):
    """
    Uma classe derivada de uma classe abstrata não pode ser instanciada,
    a menos que todos os seus métodos abstratos sejam substituídos.


    Metodo execute_algo, tem que ser implementado
    nesta classe, pois é obrigatorio
    """

    def execute_algo(self):
        # Para acessar metodo da classe Pai
        super(FilhaAbstrato, self).execute_algo()

        # Acessando atributo self.valor
        print("Valor:", self.valor ** 2)


"""
Erro para instanciar

TypeError
inst = AbstratoExemplo()
"""

inst = FilhaAbstrato(8)
inst.execute_algo()
