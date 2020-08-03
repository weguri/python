""" 
Classe basica
    __init__ 
        Construtor, recebendo dois Parâmetro 
        Toda vez que cria uma instância, da classe
            tem que passar dois valores

    resetar
        Função criada pelo, programador
"""

class SintaxeM:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def resetar(self):
        self.x, self.y = 0, 0
    
    def trocar_valor(self):
        self.x = self.y
        self.y = self.x


# Criando uma instancia
s = SintaxeM(11, 333)

# Exibindo o valor do atributo
print(s.x, s.y)

# Chamando o metodo
s.resetar()
# SintaxeM.resetar(s) # Resulta na mesmo coisa que linha acima

# Exibindo o valor do atributo
print(s.x, s.y)
