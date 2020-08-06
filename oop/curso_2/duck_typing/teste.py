# from oop.curso_2.duck_typing.duck_filme import FilmeDuck
from oop.curso_2.duck_typing.duck_livro import LivroDuck


def tstSimples(obj):
    # Não é considerado pythônico
    print(obj.exibir())


def tstIsInstance(obj):
    # Não é considerado pythônico
    if isinstance(obj, LivroDuck):
        print(obj.exibir())
    else:
        print('Não existe, metodo')


def tstMetodoLBYL(obj):
    # Não é considerado pythônico
    # LBYL
    if hasattr(obj, 'exibir'):
        if callable(obj.exibir):
            print(obj.exibir())
    else:
        print("Erro....")


def tstTryExcept(obj):
    """
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

tstSimples(escritor)
tstIsInstance(escritor)
tstMetodoLBYL(escritor)

# Exemplo pythônico
tstTryExcept(escritor)
