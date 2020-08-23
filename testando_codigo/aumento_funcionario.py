class DarAumentoFuncionario:
    """ Trabalhar com informações dos funcionarios """

    def __init__(self, nome: str, salario: float, porcentagem_aumento: float = 50) -> None:
        self.nome = nome
        self.salario = salario
        self.porcentagem_aumento = porcentagem_aumento

    def aumento_anual(self) -> None:
        self.salario = (self.salario * (self.porcentagem_aumento / 100)) + self.salario

    def dar_aumento(self, aumento_salario: float = 5000) -> None:
        self.salario += aumento_salario

    def exibir(self) -> str:
        return f'{self.nome}, seu novo salário é R$ {self.salario:.2f}'


if __name__ == "__main__":
    aumento = DarAumentoFuncionario("José", 2.123)
    aumento.dar_aumento()
    aumento.aumento_anual()
    print(aumento.exibir())
