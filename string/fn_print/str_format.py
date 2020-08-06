# Variavel na string formatada
print(
    "Primeira info {a}\nSegunda info {b}".format(a="....Saida 1...", b=".....Saida 2...")
)

print(
    "Repitindo informação, {p}, outra {p}, mais uma {p}".format(p="Segior")
)

print(
    "Saida simples: {}, {}, {}".format(1, 222, 333)
)

"""
{0:04d}
    {1º:2º3º4º} - define a posição e a formatação
        1º referente ao valor dentro do metodo format
        2º valor a ser preenchido ex: numero ou caracter ou espaço
        3º numero de caracter
        4º tipo de converção
"""
print(
    "\nBinary: {0:04b}\nFloat: {0:03f}\nChar: {0:c}\nDecimal: {0:8d}".format(65)
)
