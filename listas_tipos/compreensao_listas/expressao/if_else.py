"""
Para cada item da lista, aplique o resultado 
    resultado_if se a expressão expr for verdadeira, 
    caso contrário, aplique resultado_else.
"""
resultado = ["A" if numero % 5 == 0 else "B" for numero in range(16)]

print(resultado)