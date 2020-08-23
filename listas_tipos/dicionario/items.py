dic_nomes = {'jose': 22, 'roberto': 10, 'felipe': 44, 'julio': 1}

# Retorno: dict_items([('jose', 22), ('roberto', 10), ('felipe', 44), ('julio', 1)])
print(
    dic_nomes.items()
)

print('-' * 30)

# Loop através de chaves e valores, usando o método items():
for chave, valor in dic_nomes.items():
    print(chave.title(), valor)
