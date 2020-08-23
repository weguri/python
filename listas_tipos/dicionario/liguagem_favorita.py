linguagem_favorita = {
    'jose': ['python', 'ruby', 'java'],
    'wellington': ['php', 'java'],
    'elton': ['c'],
    'helbe': ['python', 'haskell']
}

"""
1º For 
    listar as chaves

2º For 
    listar os valores dentro dos colchetes  
    
"""

for nome, linguas in linguagem_favorita.items():
    letra_s, plural = 's', 'são'
    if len(linguas) == 1:
        letra_s, plural = '', 'é'

    print("\nA{0} língua{0} favorita{0} de {1} {2}:".format(letra_s, nome.title(), plural))

    for lingua in linguas:
        print("\t", lingua.title())


# import requests
# s = requests.Session()
# r = s.get("https://viacep.com.br/ws/61921345/json/?callback=callback_cep")
# print(r.text)
