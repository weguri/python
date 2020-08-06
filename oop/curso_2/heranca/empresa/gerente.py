from oop.curso_2.heranca.empresa.funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, salario, cpf, senha):
        """
        Construtor da classe gerente
        :param nome:
        :param salario:
        :param cpf:
        :param senha:
        """
        super().__init__(nome, salario, cpf)
        """Chamada para construtor da classe Funcionario"""

        self.senha = senha

    def getBonificacao(self) -> float:
        """
        Sobrescrever o método da classe pai
        :return: Float
        """
        # return self.salario * 0.10 + 1000.00
        return super().getBonificacao() + 1000.00

    def imprimir(self) -> str:
        return f'{super().imprimir()}, senha: {self.senha}'
