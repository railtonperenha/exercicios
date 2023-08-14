# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for numero in range(3):
    numero = input(f'Número {numero + 1}: ')
    numero = int(numero)
    lista.append(numero)

print()
lista.sort(reverse = True)
print(lista)
