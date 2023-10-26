# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = input('Primeiro Lado: ')
lado2 = input('Segundo Lado: ')
lado3 = input('Terceiro Lado: ')

try:
    lado1 = int(lado1)
    lado2 = int(lado2)
    lado3 = int(lado3)

    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
        mensagem = 'Forma um triangulo!'
        if lado1 == lado2 == lado3:
            mensagem += '\nTriangulo Equilatero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            mensagem += '\nTriangulo Isosceles'
        else:
            mensagem += '\nTriangulo Escaleno'
except:
    mensagem = 'Digite apenas números!'
print(mensagem)
