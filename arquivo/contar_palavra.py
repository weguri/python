"""
filename
    Nome do arquivo e o caminho

contar_palavra
    Recupera quantas vezes a palavra aparece
    Ulizando o comando:
        vars.count('texto')

        lower()
            o comando converte para minúscula, neste caso utilizo tanto para
            texto que procuro e aonde procuro
"""


def contar_palavras(filename: str, contar_palavra: str):
    """Conta o número aproximado de palavras em arquivo"""

    try:
        with open(filename) as f_obj:
            conteudo = f_obj.read()
    except FileNotFoundError as e:
        # print("Arquivo, não existe")
        # pass - para não fazer,
        #       Falhando silenciosamente
        pass
    else:
        """Contar o número de palavras"""
        palavras = conteudo.lower().split()
        num_palavras = len(palavras)

        pal = palavras.count(contar_palavra.lower())

        print('\nO arquivo', filename, 'possui cerca de', str(num_palavras), 'alavras.')
        print('Total de ', contar_palavra, pal)


# Chamada simples
contar_palavras('../arquivo_txt/Heidi.txt', 'particular')

# Criar uma lista, como nome dos arquivos
#
lista_arquivo = ['Alice in Wonderland.txt', 'não existe.txt', 'Heidi.txt', 'History of Lace.txt']
for arq in lista_arquivo:
    contar_palavras('../arquivo_txt/' + arq, 'PARTICULAR')
