# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = input('Salário do Funcionário: R$ ')

try:
    salario = float(salario)
    if salario < 280:
        percentual = 20
        aumento_salario = salario * percentual / 100 # Aumento de 20%
        novo_salario = salario + aumento_salario
    
    elif salario < 700:
        percentual = 15
        aumento_salario = salario * percentual / 100 # Aumento de 15%
        novo_salario = salario + aumento_salario
    
    elif salario < 1500:
        percentual = 10
        aumento_salario = salario * percentual / 100 # Aumento de 10%
        novo_salario = salario + aumento_salario
    else:
        percentual = 5
        aumento_salario = salario * percentual / 100 # Aumento de 5%
        novo_salario = salario + aumento_salario
    
    print()
    print(
    f'Salário antes do reajuste: R$ {salario:.2f}\n'
    f'Percentual de aumento: {percentual:.0f}%\n'
    f'Valor do aumento: R$ {aumento_salario:.2f}\n'
    f'Novo salário: R$ {novo_salario:.2f}'
)
except:
    print('Digite o salário desejado!')