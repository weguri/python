class ClasseNew:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


# criar umas instancia sem passar valor
inst = ClasseNew.__new__(ClasseNew)

# Erro
#   Traceback, pois não tem valor associado 
# inst.nome

dados = {"nome": "Antonio", "idade": 33}

for key, value in dados.items():
    setattr(inst, key, value)

print(inst.nome, inst.idade)
