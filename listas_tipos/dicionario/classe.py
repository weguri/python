class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor


d = dict()
obj = MinhaClasse(20)

d[obj] = 'marcos'
d["info"] = "Elena"

# Retorno: {<__main__.MinhaClasse object at 0x7f6d1d587070>: 'marcos', 'info': 'Elena'}
print(d.get(obj))
