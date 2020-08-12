from oop.curso_2.delegar.Agregacao.cliente import Cliente
from oop.curso_2.delegar.Agregacao.conta import Conta

#
# Criando instancia
cliente_1 = Cliente("Maria", "Machado", "111111-12")
cliente_2 = Cliente("brigadeiro", "Manoel", "333333-34")

#
# Criando e instanciando
# Agregando a classe Cliente a conta
conta_1 = Conta('123-4', cliente_1, 2222.01)
conta_2 = Conta('321-1', cliente_2, 1112.03)

# Metodos
conta_1.depositar(100)
conta_1.saca(50)
conta_1.transfere_para(conta_2, 200)  # Agregando conta_2 em conta_1
conta_1.extrato()

conta_1.historico.imprime()

print('-' * 40)
print('-' * 40)

conta_2.historico.imprime()
