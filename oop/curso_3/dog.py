class Dog:
    """Uma tentativa simples de modelar um cachorro"""

    def __init__(self, nome: str, idade: int):
        """Inicializar os atributos nome e idade"""
        self.nome = nome.title()
        self.idade = idade

    def sentar(self) -> None:
        """Simula um cachorro sentando em resposta a um comando."""
        print('Senta', self.nome, '!!!')

    def rolar(self) -> None:
        """Simula um cachorro rolando em resposta a um comando"""
        print('Rolar', self.nome)


"""Testa a class Dog"""

meu_dog = Dog('Lyla', 6)
meu_dog.sentar()
meu_dog.rolar()
