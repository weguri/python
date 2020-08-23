"""
open('nomeArq', ação)
    w - abre em modo de escrita, caso exista então sobrescrever
    r - modo de leitura
    a - modo de concatenação
    r+ - modo que permita ler e escrever arquivo
"""

filename = '../arquivos_txt/programacao.txt'
try:
    # Criar: modo W
    with open(filename, 'w') as file_obj:
        file_obj.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n')
        file_obj.write('Duis ut malesuada libero, non egestas nibh. Duis sagittis quis orci in suscipit.\n')

    # Abre e escreve no final
    with open(filename, 'a') as file_obj:
        file_obj.write('Morbi vulputate id arcu in interdum.\n')
        file_obj.write('Cras nibh risus, maximus a semper et, volutpat ac tellus.\n')

except FileNotFoundError as e:
    print('Arquivo, não existe')
