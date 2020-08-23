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

novo_carros = dict(carros)  # Uma copia
print(novo_carros)

#
# O construtor dict ()
# Também é possível usar o construtor dict () para fazer um novo dicionário:
velho_carros = dict(marca="Chevrolet", modelo="Mustang", cor="branco", ano=1973)

print("\nO construtor dict ()\n", velho_carros)
