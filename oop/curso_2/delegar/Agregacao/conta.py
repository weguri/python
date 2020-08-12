class ContaAgregacao:
    """
    Agregando a classe Cliente a classe Conta
    """

    def __init__(self, numero, cliente, saldo, limite):
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
