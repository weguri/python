class TransacaoInvalida(Exception):
    def __init__(self, saldo_atual, retirada) -> None:
        super(TransacaoInvalida, self).__init__("Sua conta não tem {}".format(retirada))

        self.saldo_atual = saldo_atual
        self.qtd = retirada

    def excesso(self):
        return self.qtd - self.saldo_atual


""" 
    Exemplo de Uso 
    Supondo que fosse sistema transição de valores 
    E deseja criar a propria classe para lançar as excessões
"""
try:
    # Gerando um erro
    #   if é para só exemplificar
    if not False:
        raise TransacaoInvalida(10, 20)

    # Continua aqui

except TransacaoInvalida as e:
    print("Você não tem saldo suficiente, R${}".format(e.excesso()))
