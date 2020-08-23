pets = ['cachorro', 'gato', 'cachorro', 'peixinho dourado', 'gato', 'coelha', 'gato']
print("Animais de estimação", pets, sep="\n", end="\n\n")

#
# remover todos os gatos da lista
while 'gato' in pets:
    pets.remove('gato')

print("Animais de estimação", pets, sep="\n", end="\n\n")
