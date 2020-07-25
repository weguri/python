import include.variaveis as my_var

"""
Acessando as variaveis de outro arquivo
"""

try:
    print(
        my_var.primeiro_nome,
        my_var.sobrenome
    )
except ModuleNotFoundError:
    print("Modulo importado não localizado")
