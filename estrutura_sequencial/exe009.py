# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)

fahrenheit = input('Graus em Fahrenheit: ')
fahrenheit = int(fahrenheit)

celsius = 5 * ((fahrenheit - 32) / 9)
print(f'{fahrenheit}ºF em graus Celsius, é {celsius:.0f}ºC')
