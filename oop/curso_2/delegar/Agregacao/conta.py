from oop.curso_2.delegar.Agregacao.Historico import Historico


class Conta:
    """
    Class Cliente
        Está sendo agregando na classe Conta
        Através do atributo titular
    """

    def __init__(self, numero, cliente, saldo, limite=1000.01):
        self.numero = numero
        """
        self.titular = cliente
                Uma referencia a classe Cliente
                Quando fazer a chamada da classe passar 
                A instancia para o atributo titular 
        """
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

        """
        Composição ou Delegar
            self.historico = Historico()
                O atributo é uma instancia do classe Historico()
                    Sendo assim tem acesso os metodos e atributos da classe
        """
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))

    def saca(self, valor) -> bool:
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True

    def extrato(self):
        print("Numero: {}\nSaldo: {}".format(self.numero, self.saldo))

        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transfere_para(self, destino, valor) -> bool:
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("transferência de {} para conta {}".format(valor, destino.numero))
            return True
