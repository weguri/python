import os

"""
Entra dentro do diretorio
"""

# Entra no diretorio informado
os.chdir("data_hora")

# Exibe o diretorio altual
print(os.getcwd())

# Volta um diretorio
os.chdir("../")
