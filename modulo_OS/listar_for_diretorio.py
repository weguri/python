import os

# Pasta dos arquivos
pasta = "modulo_OS"

if os.path.isdir(pasta):
    
    # Lista diretorio
    for file_dir in os.listdir(pasta):

        name_df = "{}/{}".format(pasta, file_dir)  # caminho compreto

        if os.path.isdir(name_df):
            print("Diretório: %s\n" % file_dir)
        else:
            print("Arquivo:", file_dir)
else:
    print("\nPasta não localizada")