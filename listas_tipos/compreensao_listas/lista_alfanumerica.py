"""
str:
    Converte para string

upper:
    transforma tudo para maiúscula, sendo texto

"""
lista_alfanumerica = ['abacate', 'b', 'c', 1, 2, 3]

resultado = [str(item).upper() for item in lista_alfanumerica]

print(resultado)
