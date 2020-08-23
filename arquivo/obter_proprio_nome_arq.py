import os
import sys

#
# Somente o nome do arquivo.ext
print(
    os.path.basename(__file__),
    end='\n\n'
)

#
# Nome e caminho, do arquivo
print(sys.argv[0], end='\n\n')

#
# Nome do proprio arquivo sendo manipulado
print(
    (('-' * 10) + '| Pegar nome do arquivo |' + ('-' * 10)),

    (__file__.split('/')[-1])[0:-3],
    (__file__.split('/')[-1]),
    (__file__.split('/')),
    __file__,
    sep='\n'
)
