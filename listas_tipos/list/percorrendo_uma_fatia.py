"""
[:3]
    Exibe as posições 0, 1, 3
"""
frutas = ["oxicoco", "maça", "kiwi", "melon", "abacaxi", "banana", "mango", "ananás"]

for fruta in frutas[:3]:
    print(fruta.title())

#
# Lista tado a lista
for fruta in frutas:
    print(f"Minha lista de frutas: {fruta.title()}")
