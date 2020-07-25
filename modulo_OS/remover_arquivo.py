import os

"""
Para deletar arquivo
    remove
"""


# Criar para testar
open("txt/vazio_teste.txt", "w").close()

# Exibir tudo que esta na pasta
os.listdir('txt')

# Deleta o arquivo da Pasta
os.remove("txt/vazio_teste.txt") # deletado

# Exibir tudo que esta na pasta
os.listdir('txt')