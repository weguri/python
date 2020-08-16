"""
Sobre try e except
https://docs.python.org/pt-br/3/tutorial/errors.html


try:
    Neste ponto é processado, até quando estiver tudo certo

except:
    Existe um tratamento para quase todos os tipos de erros
    Caso não tenha tipo específico, resultado cai no except
    Exemplo:
        except ZeroDivisionError as err:

else:
    Caso não tenha nenhum erro

finally:
    sempre será executado
"""


def teste(tst):
    """
    Função só para fazer teste sobre os except
    """
    if tst == 1:
        raise ZeroDivisionError("Erro por difivão")
    if tst == 2:
        raise TypeError
    if tst == 3:
        raise ValueError("Valor errado")


try:
    """ Exemplo de uso - Exemplificando """

    teste(2)

except ZeroDivisionError as err:
    print(err, end="\n")
except TypeError:
    print("Tipo de informação errada", end="\n")
except ValueError as err:
    print(err, end="\n")
except:
    print("Erro geral", end="\n")
else:
    print("Quando não tem nenhum erro", end="\n")
finally:
    print("Sempre será executado", end="\n")
