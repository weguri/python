class ProdutoLista:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"nome:{self.nome} valor:{self.preco}"


""" EXEMPLO para adicionar classe na LIST """

chocolate = ProdutoLista("Chocolate", 2.33)
refrigerante = ProdutoLista("Refrigerante", 3.22)
feijao = ProdutoLista("Feijão", 5.88)

#
# Criar a lista com a classe ProdutoLista
lista_produto = [chocolate, refrigerante, feijao]

# append
arroz = ProdutoLista("Arroz", 5.11)
lista_produto.append(arroz)

# extend
queijo = ProdutoLista("Queijo", 9.22)
# lista_produto.extend(queijo)  # TypeError: 'ProdutoLista' object is not iterable
lista_produto.extend([queijo])  # para funcionar tem que colocar dentro dos []

#
leite = ProdutoLista("Leite", 2.51)
cafe = ProdutoLista("Café", 3.44)
meu_produto = [leite, cafe]
lista_produto.append(meu_produto)

#
# Resultado da lista
print("Exibir lista de produtos:", lista_produto, sep="\n")
