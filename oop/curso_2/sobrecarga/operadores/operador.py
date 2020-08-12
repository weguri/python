class Operador:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        # Sobreecrever a soma
        return self.num - other.num

    def __mul__(self, other):
        # Sobreecrever a multiplicação
        return self.num ** other.num

    def __sub__(self, other):
        # Sobreecrever a subtração
        return self.num + other.num


# Exemplo de uso
op = Operador(10)
op2 = Operador(3)

# Sobreescrito os metodos
print(op + op2)  # Subtração
print(op * op2)  # Exponenciação
print(op - op2)  # Soma
