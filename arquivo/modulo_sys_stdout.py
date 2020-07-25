import sys

try:
    ler_arquivo = open("txt/familia.txt", "r")

    for linha in ler_arquivo:
        # print(linha)
        # sys.stdout.write(linha)
        # sys.stdout.write("Nome: {}".format(linha))
        sys.stdout.write("Nome: %s" % linha)

    ler_arquivo.close
except:
    print("Erro para abrir o arquivo")
