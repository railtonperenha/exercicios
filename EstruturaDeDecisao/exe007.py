# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = input('Primeiro Número: ')
numero2 = input('Segundo Número: ')
numero3 = input('Terceiro Número: ')

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    numero3 = float(numero3)
    if numero1 > numero2 and numero2 > numero3:
        print(f'O número "{numero1}" é o MAIOR e o número "{numero3}" é o MENOR')
    elif numero2 > numero3 and numero3 > numero1:
        print(f'O número "{numero2}" é o MAIOR e o número "{numero1}" é o MENOR')
    elif numero3 > numero2 and numero2 > numero1:
        print(f'O número "{numero3}" é o MAIOR e o número "{numero1}" é o MENOR')
except ValueError:
    print('Digite apenas Números')