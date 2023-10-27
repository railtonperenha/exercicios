import math

# Solicitar os valores de a, b e c ao usuário
a = input('Digite o valor de a: ')

try:
    a = float(a)
    if a == 0:
        mensagem = 'Isso não é uma equação de segundo grau!'
    else:
        b = input('Digite o valor de b: ')
        b = float(b)
        c = input('Digite o valor de c: ')
        c = float(c)
    
        # Calcula o delta
        delta = b**2 - 4 * a * c

        # Verifica o valor de delta
        if delta < 0:
            mensagem = 'A equação não possui raízes reais.'
        elif delta == 0:
            raiz = -b / (2 * a)
            mensagem = f'A equação possui uma raiz real: {raiz}'
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            mensagem = f'A equação possui duas raízes reais: {raiz1} e {raiz2}'
except ValueError:
    mensagem = 'Valor inválido! Tente novamente.'

print(mensagem)
