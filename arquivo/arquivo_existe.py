import pathlib
import os

"""
(Python 3.4+)
pathlib módulo que fornece uma interface orientada a 
objetos para lidar com caminhos de sistema de arquivos.
"""

path = pathlib.Path('../arquivo_txt/lorem_ipsum.txt')

print(path.exists())
print(path.is_file())

"""
Forma mais antiga
"""
PATH = '../arquivo_txt/lorem_ipsum.txt'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print("O arquivo existe e é legível")
else:
    print("O arquivo está faltando ou não é legível")
