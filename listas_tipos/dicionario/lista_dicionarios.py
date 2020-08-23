"""
dict:
    Criar uma dicionario, depois adicionar na list
"""
alien_0 = dict(cor='verde', pontos=5)
alien_1 = dict(cor='amarelo', pontos=10)
alien_2 = dict(cor='vermelho', pontos=15)

# Criar uma lista
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('-' * 30)

# Criar uma lista vazia para armazenar alienigenas
aliens = list()

# criar 30 alienigenas
for alien_numero in range(30):
    new_alien = {'cor': 'verde', 'pontos': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print(aliens)

print('-' * 30)

# Altera os 3 primeiros
for alien in aliens[0:3]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['speed'] = 'medium'
        alien['pontos'] = 10
    elif alien['cor'] == 'amarelo':
        alien['cor'] = 'vermelho'
        alien['speed'] = 'fast'
        alien['pontos'] = 15

# Mostrar os 5 primeiros alienigenas
for alien in aliens[:10]:
    print(alien)
print("...")

print("Total de alien:", len(aliens))
