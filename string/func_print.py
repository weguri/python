print("weliton", "ferreira", "figueiredo")

print("weliton", "ferreira", "figueiredo", sep="--------")

print("weliton", "ferreira", "figueiredo", end=" ....:")

a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')

# Informação gravado no TXT
sourceFile = open('txt/python.txt', 'w')
print('Desta forma o conteudo é colocado diretamente dentro do arquivo de texto', file=sourceFile)
sourceFile.close()
