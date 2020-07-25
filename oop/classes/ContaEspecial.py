import oop.classes.ContaBanco as Heritage

"""
Heritage = Herança 
    poderia ser qualquer palavra
"""


class ContaEspecial(Heritage.ContaBanco):
    """
    ContaEspecial é a classe filha da classe ContaBanco
    """

    def __init__(self, cliente, numero_conta, saldo=0, limite=0):
        Heritage.ContaBanco.__init__(self, cliente, numero_conta, saldo)
        self.limite = limite

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        elif valor <= (self.saldo + self.limite):
            self.saldo = valor - (self.saldo + self.limite)
        else:
            self.saldo = valor - self.limite
