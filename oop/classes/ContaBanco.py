class ContaBanco:
    def __init__(self, cliente, numero_conta, saldo=0):
        self.saldo = saldo
        self.cliente = cliente
        self.numero_conta = numero_conta

    def depositar(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def relatorio(self):
        print("Cliente.: %s \nConta numero.: %s \nSaldo.: %8.2f" %
              (self.cliente.rjust(10), self.numero_conta.rjust(10), self.saldo))
