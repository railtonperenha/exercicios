altura = input('Qual é sua altura: ')
altura = float(altura)
sexo = input('Masculino ou Feminino: ')
sexo = sexo.capitalize()

if sexo == 'Masculino':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso_ideal:.2f}kg')
elif sexo == 'Feminino':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal:.2f}kg')
else:
    print('Digite o seu peso e o seu sexo!')