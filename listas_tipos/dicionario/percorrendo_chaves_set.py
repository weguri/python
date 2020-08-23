"""
set:
    Em torno de uma lista que contenha itens duplicados, Python
    identifica os itens únicos na lista e cria um conjunto a partir desses itens.

    O set() usado em conjunto ao values(), extrai o valor unico.
"""
linguagem_favorita = {
    "jose": "python",
    "wellington": "php",
    "elton": "c",
    "helbe": "python"
}

print("Os seguintes idiomas foram mencionados:")
for nome in set(linguagem_favorita.values()):  # Apresenta somente valores únicos
    print("-", nome.title())
