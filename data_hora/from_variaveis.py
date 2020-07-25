from include.variaveis import *
# from include.variaveis import data_hora, dia_semana

# Mesmo está variavel amazenando outra data
# Com o comando .today() retorna data atual
hoje = data_hora.today()
# hoje = data_hora

dia = hoje.day
mes = hoje.month
nome_mes = mes_extenso[hoje.month - 1]
ano = hoje.year

print("%d/%d/%d" % (dia, mes, ano))
print("%d de %s de %d" % (dia, nome_mes, ano))

print("Daqui 40 dias:", data_hora.fromordinal(hoje.toordinal() + 40))
print("Dia da semana:", dia_semana[hoje.weekday()])
# print(dia_semana)
# print(hoje.weekday())
