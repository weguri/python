""" 
Unir dois conjuntos
    Existem várias maneiras de associar dois ou mais conjuntos no Python.

    Você pode usar o union()método que retorna um novo conjunto contendo 
    todos os itens de ambos os conjuntos ou o update() método que insere 
    todos os itens de um conjunto em outro

    Nota: 
        Ambos union() e update() excluirão quaisquer itens duplicados.
"""

set1 = {"a", "b", "c", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
