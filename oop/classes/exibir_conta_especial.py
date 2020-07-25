from oop.classes import ContaEspecial as cbe

cliente = cbe.ContaEspecial("Weliton", "2342-33", 1000.01, 2000.32)

cliente.relatorio()

cliente.saque(3000)

cliente.relatorio()

cliente.depositar(5000)

cliente.relatorio()
