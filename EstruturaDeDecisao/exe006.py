# Faça um Programa que leia três números e mostre o maior deles.

numero1 = input('Primeiro Número: ')
numero2 = input('Segundo Número: ')
numero3 = input('Terceiro Número: ')

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    numero3 = float(numero3)
    if numero1 > numero2 and numero2 > numero3:
        print(f'O PRIMEIRO número é MAIOR')
    elif numero2 > numero3 and numero3 > numero1:
        print(f'O SEGUNDO número é MAIOR!')
    else:
        print(f'O TERCEIRO número é MAIOR!')
except ValueError:
    print('Digite apenas números!')
