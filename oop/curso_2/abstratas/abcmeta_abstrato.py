from abc import ABCMeta, abstractmethod


class AbstratoClass(metaclass=ABCMeta):

    @abstractmethod
    def exibir_dados(self) -> str:
        pass

    @abstractmethod
    def processamento_dados(self, dados):
        pass

# erro para instanciar
# inst = AbstratoClass()
