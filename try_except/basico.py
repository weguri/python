"""
except
    Caso não coloque nada na frente do except vai pegar todos erros 
        Mais não tem como saber o que disparou o erro
"""

try:
    print(2 / 0)
except ZeroDivisionError as ziro:
    print("Erro:", ziro)