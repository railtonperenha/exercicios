# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

from datetime import date

ano = input('Digite um ano para saber se ele é Bissexto, ou digite 0 para analisar o ano atual: ')

try:
    ano = int(ano)
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        mensagem = f'O ano de {ano} é um ano Bissexto!'
    else:
        mensagem = f'O ano de {ano} não é Bissexto.'

except:
    mensagem = 'Digite um ano válido!'

print(mensagem)