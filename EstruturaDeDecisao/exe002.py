# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = input('Digite um número: ')

try:
    numero = int(numero)
    if numero < 0:
        print("O número digitado foi NEGATIVO")
    else:
        print ("O número digitado foi POSITIVO")
except ValueError:
    print('Digite um número inteiro!')
