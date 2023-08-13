# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = input('Metros para serem pintados: ')

try:
    metros_float = float(metros)
    litros = metros_float / 3
    lata = litros / 18
    lata = int(lata)
    valor = 80.00
    if litros % 18 == 0:
        lata
        valor
    elif litros % 18 != 0:
        lata = lata + 1
        valor = valor * lata
    print(
    f'Quantidade de latas: {lata}\n'
    f'Valor gasto: R$ {valor:.2f}'
)

except ValueError:
    print('Digite um valor!')