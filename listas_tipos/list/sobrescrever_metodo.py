class MinhaLista(list):
    """Sobrescrever o metodo append"""

    def append(self, *args):
        """
        extend
            Nesta modificação o append aceita mais de valor
        """
        self.extend(args)


"""
Neste exemplo
    acontece um erro: TypeError
        tst.append(2,3,4,43) - pois não pode adicionar mais de UM

tst = [1, 4]
tst.append(2,3,4,43)
print(tst)
"""

lista = MinhaLista()
lista.append(2, 5, 4, 1, 7, 8)  # Modificado para aceitar mais de uma valor
print(lista)
