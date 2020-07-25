from oop.classes import ContaBanco as cb

cliente = cb.ContaBanco("Weliton", "2342-33", 1000.01)

cliente.relatorio()

cliente.depositar(333)

cliente.relatorio()

cliente.saque(732.82)

cliente.relatorio()
