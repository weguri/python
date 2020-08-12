frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie vel lectus id varius.'

print("Cada espaço vira uma posição\n", frase.split(), end="\n\n")

# Duas formas iguais
# split(None) ou split()
#
print("Divide em 5 partes\n", frase.split(" ", 5), end="\n\n")

print("Divide com base no ponto\n", frase.split("."), end="\n\n")
