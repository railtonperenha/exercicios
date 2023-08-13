# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

largura = input('Largura: ')
altura = input('Altura: ')

largura = float(largura)
altura = float(altura)

dobro_area = (largura * altura) * 2

print(f'O dobro da área digitada é {dobro_area}')
