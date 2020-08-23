"""
'teste {posição}'.format(variavel)
    variavel: numerica ou string
        contem a informação
    posição
        Aonde inserida pedendendo do valor
        pode haver uma formatação

f'teste {variavel:formatação}'
    O valor poder pode ser formatado caso precise

Site com exemplos:
    https://mkaz.blog/code/python-string-format-cookbook/
    http://www.lamed-oti.com/school/rs/python/PythonStringFormatCookbook%20.pdf
"""

pi_number = 3.1415926

print("PI: {0} ou {0:0.2f}".format(pi_number))
print(f"PI: {pi_number} ou {pi_number:0.2f}")

"""
3,1415926   {:.2f}      3,14 2 casas decimais
3,1415926   {:+.2f}     +3,14 2 casas decimais com sinal
-1          {:+.2f}     -1,00 2 casas decimais com sinal
2.71828     {:.0f}      3 Sem casas decimais
5           {:0>2d}     05 Número de preenchimento com zeros (preenchimento à esquerda, largura 2)
5           {:x<4d}     5xxx Número do bloco com x's (preenchimento direito, largura 4)
10          {:x<4d}     10xx Número do bloco com x's (preenchimento direito, largura 4)
1000000     {:,}        1.000.000 Formato numérico com separador de vírgula
0,25        {:0,2%}     5,00% Porcentagem do formato
1000000000  {:.2e}      1,00e + 09 Notação expoente
13          {:10d}      13 alinhado à direita (padrão, largura 10)
13          {:<10d}     13 alinhado à esquerda (largura 10)
13          {:^10d}     13 alinhado ao centro (largura 10)
"""
