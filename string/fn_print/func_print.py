print("Lasanha", "Feijoada", "Contrafilé")

print("Lasanha", "Feijoada", "Contrafilé", sep="--------")

print("Lasanha", "Feijoada", "Contrafilé", end=" ....:")

a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')


#
# Neste exemplo o PRINT não exibi na tela
# O texto é gravado em um arquivo de TEXTO
#
sourceFile = open('txt/python.txt', 'w')

print('Desta forma o conteudo é colocado diretamente dentro do arquivo de texto',
      file=sourceFile)

sourceFile.close()
