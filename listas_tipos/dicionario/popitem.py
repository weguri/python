"""
popitem()
    método remove o último item inserido (nas versões anteriores à 3.7, um item aleatório é removido):
"""

carros = {
    "marca": "Ford",
    "modelo": "Mustang",
    "cor": "amarelo",
    "year": 1964
}

# Remover a ultima posição, atrubuir a uma variavel
#       retorno:
#             ('year', 1964)
s = carros.popitem()
print(s)

print(
    "-" * 30,
    carros,
    sep="\n"
)