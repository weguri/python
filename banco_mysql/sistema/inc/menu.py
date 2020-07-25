from banco_mysql.sistema.inc.atualizarcliente import AtualizarCliente
from banco_mysql.sistema.inc.excluir import Excluir
from banco_mysql.sistema.inc.listarclientes import ListarClientes
from banco_mysql.sistema.inc.conexao import Conexao
from banco_mysql.sistema.inc.cadastro import Cadastro
import sys

"""
Montagem do menu
"""


def Menu():
    try:
        opcaoEscolha = int(input(
            "Estolha uma opção:\n\n"
            "1) Cadastrar\n"
            "2) Alterar\n"
            "3) Excluir\n"
            "4) Pesquisar\n"
            "5) Listar todos\n"
            "6) Sair\n\n"
            "Opção..: "
        ))

        if opcaoEscolha < 1 or opcaoEscolha > 6:
            raise Exception("Opção Inválida, escolha entre 1 e 6")
        else:
            if opcaoEscolha == 1:
                Cadastro(Conexao())
            elif opcaoEscolha == 2:
                AtualizarCliente(Conexao())
            elif opcaoEscolha == 3:
                Excluir(Conexao())
            elif opcaoEscolha == 4 or opcaoEscolha == 5:
                ListarClientes(Conexao(), opcaoEscolha)
            elif opcaoEscolha == 6:
                # quit()
                sys.exit(1)
                # exit()
        Menu()
    except Exception as err:
        print("\n{}\n".format(err))
        input("")
