"""
__slots__
    Não permiter criar atributos fora da classe
    Supondo que sem slots esta classe tenha tamanho de ~200 bytes
    pois os dados são montados, tipo um dicionario e ainda tenha toda definição dos
    tipos float, int mesmo que estiver zerado
    slots não deixa com que a classe seja criada tipo um dicionario, sendo assim
    ele cria algo tipo uma tupla com tamanho fixo
"""


class ListaSlots:
    __slots__ = ('nome', 'email')

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saida(self) -> str:
        return f"{self.nome}, {self.email}"


"""
Exemplo teste
"""
list_slot = ListaSlots('Zé Maria', 'ze@teste.com')
print(
    list_slot.saida()
)

# Erro
# Isso não se pode ser feito pois classe já esta definido o tamanho de atrinutos
#   AttributeError: 'ListaSlots' object has no attribute 'senha'

# list_slot.senha = '123123' # AttributeError: 'ListaSlots' object has no attribute 'senha'
