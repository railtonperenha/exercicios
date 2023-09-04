# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('''
    [M] Matutino
    [V] Vespertino
    [N] Noturno
      '''
)
periodo = input('Qual periodo você estuda ?: ').upper()

if periodo == 'M':
    print(f'Seu periodo é Matutino!')
elif periodo == 'V':
    print(f'Seu periodo é Vespertino!')
elif periodo == 'N':
    print('Seu periodo é Noturno!')
else:
    print('\033[1;4mErro!\nDigite apenas M, N ou V.\033[m')