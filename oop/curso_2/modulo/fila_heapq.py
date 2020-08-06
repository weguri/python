import heapq


class FilaDePrioridade:
    """ 
    FilaDePrioridade
    Lista de prioridade para execulção
    """

    def __init__(self):
        self.fila = []
        self.indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice += 1

    def remover(self):
        return heapq.heappop(self.fila)[-1]


class Item:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "{}".format(self.nome)


""" 
Classe FilaDePrioridade ordena do maior para o menos
Quando for utilizado o metodo inserir()
deve ser passado a prioridade de execução
quando chamar o medoto remover este mais alto que vair 
ser removido da pilha de execução
"""

# fila = FilaDePrioridade()
# fila.inserir(Item("Sergio"), 3)
# fila.inserir(Item("Maria"), 1)
# fila.inserir(Item("João"), 4)

# print(fila.remover())