"""
pop
    O método remove o item com o nome de chave especificado.
    Possivel pegar o valor removido:
        x = pop("chave")


"""
carros = {
    "marca": "Ford",
    "modelo": "Mustang",
    "cor": "amarelo",
    "year": 1964
}

# Traceback: TypeError
# carros.pop()

# Retorna valor da posição que foi removida
s = carros.pop("cor")
print(s)

print(
    "-" * 30,
    carros,
    sep="\n"
)
