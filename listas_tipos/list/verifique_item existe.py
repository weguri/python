""" 
in
    Para determinar se um item especificado está presente em uma lista, use a inpalavra-chave:

not in
    negação da informação
"""

frutas = ["oxicoco", "maça", "kiwi", "melon", "abacaxi", "banana", "mango", "ananás"]

print("Verificando com in")
if "banana" in frutas:
    print("Fruta: Banana")
else:
    print("Não existe")

print("\nVerificando com not in")
if "banana" not in frutas:
    print("Verdadeiro")
else:
    print("Não existe")

print("\nVerificando se esta vazia")
lista_vazia = []
if lista_vazia:
    print("Não esta vazia")
else:
    print("Lista vazia")
