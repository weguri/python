from oop.curso_2.delegar.Agregacao.cliente import Cliente
from oop.curso_2.delegar.Agregacao.conta_agregacao import ContaAgregacao

# Criando a Instância do classe Cliente
cliente = Cliente('Rodrigues', 'Oliveira', '11111222')

# Agregação a classe cliente na Instância minha_conta
minha_conta = ContaAgregacao('123-4', cliente, 120.0, 1000.0)

# Testar o exemplo

# .titular
#   Vai ter referencia ao objeto da classe Cliente
print(minha_conta.titular)

# Acessando o atributo da classe cliente
#
#   2 atribustos da classe cliente
#       nome
#       sobrenome
print(
    minha_conta.titular.nome,
    minha_conta.titular.sobrenome
)
