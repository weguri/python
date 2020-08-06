from oop.curso_2.heranca.humano.Pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str):
        super().__init__(nome, idade)
        self.cpf = cpf
    
    def imprimir(self) -> str:
        return f'{self.nome}, CPF: {self.cpf}'
