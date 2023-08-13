# Faça um Programa que peça as 4 notas bimestrais e mostre a média

prova1 = input('Primeira Prova: ')
prova2 = input('Segunda Prova: ')
prova3 = input('Terceira Prova: ')
prova4 = input('Quarta Prova: ')

prova1 = float(prova1)
prova2 = float(prova2)
prova3 = float(prova3)
prova4 = float(prova4)

media = (prova1 + prova2 + prova3 + prova4) / 4

print(f'Média: {media:.1f}')