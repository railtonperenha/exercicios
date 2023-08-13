# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

import math
raio = input('Digite o raio de um circulo: ')

raio = float(raio)
pi = math.pi
area = pi * (raio ** 2)

print(f'A área desse círculo é de {area:.2f}')
