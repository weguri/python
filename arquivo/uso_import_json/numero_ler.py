import json

filename = '../../arquivo_txt/numero.json'
with open(filename) as f_obj:
    num_dados = json.load(f_obj)

print(num_dados)
