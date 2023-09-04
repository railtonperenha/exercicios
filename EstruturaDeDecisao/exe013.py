# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('''
[1] Domingo
[2] Segunda-Feira
[3] Terça-Feira
[4] Quarta-Feira
[5] Quinta-Feira
[6] Sexta-Feira
[7] Sábado
''')
dia = input('Digite um número correspondente: ')

try:
    dia = int(dia)
    if dia == 1:
        dia_semana = 'Domingo'
    
    elif dia == 2:
        dia_semana = 'Segunda-Feira'

    elif dia == 3:
        dia_semana = 'Terça-Feira'
    
    elif dia == 4:
        dia_semana = 'Quarta-Feira'

    elif dia == 5:
        dia_semana = 'Quinta-Feira'

    elif dia == 6:
        dia_semana = 'Sexta-Feira'

    elif dia == 7:
        dia_semana = 'Sábado'
    
    print()
    print(dia_semana)
except:
    print('Valor Inválido!!')