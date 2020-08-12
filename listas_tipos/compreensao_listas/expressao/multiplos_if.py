"""
Por exemplo: gostaríamos de saber os Múltiplos Comuns de 5 e 6.
Utilizando múltiplos if's e list comprehensions, podemos criar o seguinte 
    código:
"""
resultado = [numero for numero in range(100)
             if numero % 5 == 0 if numero % 6 == 0]


print(resultado)
