linguagem_favorita = {
    "jose": "python",
    "wellington": "php",
    "elton": "c",
    "helbe": "python"
}

amigos = ['jose', 'elton']

for nome in linguagem_favorita.keys():
    print(nome.title())

    if nome in amigos:
        print("Olá, %s, vejo que sua linguagem favorita é %s!\n" %
              (nome.title(), linguagem_favorita[nome].title())
              )

if 'henrique' not in linguagem_favorita.keys():
    print("\nHenrique, por favor, responda à nossa enquete!")
