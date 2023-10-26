# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = input('Primeira Nota: ')
nota2 = input('Segunda Nota: ')

try:
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = (nota1 + nota2) / 2
    
    if media < 4:
        conceito = 'E'
        mensagem = 'REPROVADO!'
    elif media < 6:
        conceito = 'D'
        mensagem = 'REPROVADO'
    elif media < 7.5:
        conceito = 'C'
        mensagem = 'APROVADO!'
    elif media < 9:
        conceito = 'B'
        mensagem = 'APROVADO!'
    elif media < 10:
        conceito = 'A'
        mensagem = 'APROVADO!'
    else:
        conceito = 'Inválido'
except:
    print("Digite apenas números!")

print(f'Primeira Nota: {nota1}')
print(f'Segunda Nota: {nota2}')
print(f'Média de aproveitamento: {media}'.replace('.', ','))
print(f'Conceito: {conceito}')
print(f'{mensagem}')
