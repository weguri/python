meus_familiares = {
    "filho1": {
        "nome": "José",
        "ano": 2001
    },
    "filho2": {
        "nome": "Maria",
        "ano": 2010
    },
    "filho3": {
        "nome": "Lucia",
        "ano": 1992
    }
}

print(meus_familiares["filho3"]["nome"], end="\n\n")  # Apresenta: Lucia

for meus in meus_familiares:
    print(meus)
    for meu in meus_familiares[meus]:
        print("\t", meus_familiares[meus][meu])

    print("")
