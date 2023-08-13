# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit

celsius = input('Graus em Celsius: ')
celsius = int(celsius)
fahrenheit = (celsius * 1.8) + 32

print(f'{celsius}ºC convertido para Fahrenheit é: {fahrenheit}ºF')
