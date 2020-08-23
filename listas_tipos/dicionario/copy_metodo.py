"""
copy
    Faça uma cópia de um dicionário com o copy() método:
"""
carros = {
    "marca": "Ford",
    "modelo": "Mustang",
    "cor": "amarelo",
    "year": 1964
}

novo_carros = carros.copy()

print(carros, end="\n\n")

# modificando dados
novo_carros["modelo"] = "Ecosport"
novo_carros["year"] = 2018
print("Novo carro", novo_carros, sep="\n")
