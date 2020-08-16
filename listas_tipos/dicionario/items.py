d = {'jose': 22, 'roberto': 10, 'felipe': 44, 'julio': 1}

# Retorno: dict_items([('jose', 22), ('roberto', 10), ('felipe', 44), ('julio', 1)])
print(
    d.items()
)

print('-' * 30)

for (c, v) in d.items():
    print(c, v)
