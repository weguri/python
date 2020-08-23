"""
dict
    Metodo que define um dicionario pode usado para criar uma copia
"""
carros = {
    "marca": "Ford",
    "modelo": "Mustang",
    "cor": "amarelo",
    "year": 1964
}

novo_carros = dict(carros)

print(novo_carros)
