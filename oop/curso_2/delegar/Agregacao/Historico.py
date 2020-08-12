import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("Data abertura: {}".format(self.data_abertura))
        if len(self.transacoes) > 0:
            print("Transações: ")
            for t in self.transacoes:
                print(' - ', t)
