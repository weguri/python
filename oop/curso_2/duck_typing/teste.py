from oop.curso_2.duck_typing.duck_filme import FilmeDuck
from oop.curso_2.duck_typing.duck_livro import LivroDuck


def tst_simples(obj):
    # Não é considerado pythônico
    print(obj.exibir())


def tst_isinstance(obj):
    # Não é considerado pythônico
    if isinstance(obj, LivroDuck):
        print(obj.exibir())
    else:
        print('Não existe, metodo')


def tst_metodo_lbyl(obj):
    # Não é considerado pythônico
    # LBYL
    if hasattr(obj, 'exibir'):
        if callable(obj.exibir):
            print(obj.exibir())
    else:
        print("Erro....")


def tst_try_except(obj):
    """
    EAFP - Easier to ask for forgiveness than permission
            (Mais fácil pedir perdão do que permissão)
    Exemplo....: pythônico
    :param obj:
    :return:
    """
    try:
        print(obj.exibir())
    except AttributeError as err:
        print(err)


escritor = LivroDuck("Aprenda Python Grátis",
                     "06/08/2020", "www.python.pro.br")

filme = FilmeDuck("Python Ação", "06/08/2020", "www.python.org")

tst_simples(escritor)
tst_isinstance(escritor)
tst_metodo_lbyl(escritor)

print('-' * 30)

# Exemplo Pythônico
tst_try_except(escritor)
tst_try_except(filme)
