from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def desde_ano_nascimento(cls, nome, ano_nascimento):
        """
        Como fosse segundo construtor, neste exemplo
        chama o construtor da propria classe
        """
        return cls(nome, date.today().year - ano_nascimento)

    def exibir(self):
        print("A idade de %s é: %s" % (self.nome, self.idade))


"""
Exemplo de uso 
"""

pessoa1 = Pessoa('Adam', 38)  # construtor __init__
pessoa1.exibir()

pessoa2 = Pessoa.desde_ano_nascimento('John', 1981)  # seria tipo o segundo construtor
pessoa2.exibir()
