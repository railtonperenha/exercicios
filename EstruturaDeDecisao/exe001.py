# Faça um Programa que peça dois números e imprima o maior deles.

numero1 = input('Primeiro Número: ')
numero2 = input('Segundo Número: ')

try:
    if numero1 > numero2:
        numero1 = int(numero1)
        numero2 = int(numero2)
        print(f'O número {numero1} é maior!')
    else:
        numero1 = int(numero1)
        numero2 = int(numero2)
        print(f'O número {numero2} é maior!')
except ValueError:
    print('Digite um número inteiro!')
