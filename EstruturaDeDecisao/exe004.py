# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')
letra = str(letra.capitalize())

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f'{letra} é uma VOGAL!')
else:
    print(f'{letra} é uma CONSOANTE')