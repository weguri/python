""" 
Intervalo de índices
Você pode especificar um intervalo de índices especificando por onde começar e por onde terminar o intervalo.

Ao especificar um intervalo, o valor retornado será uma nova lista com os itens especificados.
"""

# Nota: A pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).
lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(lista[2:5])

# Retorna as 4 primeiras posições
print(lista[:4])

# Retorna da terceira posição até o fim
print(lista[3:])

# A string seria um tipo de lista de caracteres
print("Weliton Ferreira Figueiredo"[4:13])

# Retira a primeira e a ultima posição
print(lista[1:-1])
