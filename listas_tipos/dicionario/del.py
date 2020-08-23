"""
del
    Remove o item com o nome de chave especificado.
    Possivel remover lista inteira
"""
carros = {
    "marca": "Ford",
    "modelo": "Mustang",
    "cor": "amarelo",
    "year": 1964
}

del carros['cor']

print(
    carros,
    sep="\n"
)

del carros

# print(carros)  # Traceback: NameError
