# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre: 
# - O produto do dobro do primeiro com metade do segundo .
# - A soma do triplo do primeiro com o terceiro.
# - O terceiro elevado ao cubo.


numero1 = input('Primeiro número inteiro: ')
numero2 = input('Segundo número inteiro: ')
numero3 = input('Número real: ')

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = float(numero3)

produto_dobro = (numero1 * 2) + (numero2 / 2)
soma_primeiro = (numero1 * 3) + numero3
cubo = numero3 ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {produto_dobro}')
print(f'A soma do triplo do primeiro com o terceiro: {soma_primeiro}')
print(f'O terceiro elevado ao cubo: {cubo:.1f}')