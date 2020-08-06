class Funcionario:

    __serial = int()

    def __init__(self, nome: str, salario: float, cpf: str, x: int = 0) -> None:
        self.nome = nome
        self.salario = salario
        self.cpf = cpf
        self.__serial = x

    # 
    # 
    def getBonificacao(self) -> float:
        return self.salario * 0.10

    def getSerial(self) -> int:
        return self.__serial

    def setSerial(self, x: int):
        self.__serial = x

    def imprimir(self) -> str:
        return f'{self.nome}, {self.cpf}'
