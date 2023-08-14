# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez

nota1 = input('Primeira Nota: ')
nota2 = input('Segunda nota: ')

try:
    nota1 = float(nota1)
    nota2 = float(nota2)

    media = (nota1 + nota2) / 2
    if media < 7:
        print(f'Sua média foi de {media}: REPROVADO')
    elif media >= 7 and media <= 9:
        print (f'Sua média foi de {media}: APROVADO')
    else:
        print (f'Sua média foi de {media}: APROVADO COM DISTINÇÃO')
except ValueError:
    print('Digite as notas corretamente!')
