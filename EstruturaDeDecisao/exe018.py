# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numero1 = input('Primeiro Número: ')
numero2 = input('Segundo Número: ')
numero3 = input('Terceiro Número: ')

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    numero3 = float(numero3)
    soma = numero1 + numero2 + numero3

    if numero1 < numero2 and numero2 < numero3:
        mensagem = 'O terceiro número é o maior'
        mensagem += f'\nA soma deles é de: {soma}'
    
    elif numero2 < numero1 and numero3 < numero1:
        mensagem = 'O primeiro número é o maior'
        mensagem += f'\nA soma deles é de: {soma}'
    elif numero2 > numero1 and numero2 > numero3:
        mensagem = 'O segundo número é o maior'
        mensagem += f'\nA soma deles é de: {soma}'
except:
    mensagem = 'Digite apenas números!'
print(mensagem)