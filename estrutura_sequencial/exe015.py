# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

valor_hora = input('Recebe por hora: R$ ') # Valor que o usuário recebe por hora
horas_trabalhadas = input('Horas trabalhadas esse mês: ') # Horas trabalhadas pelo usuário

valor_hora = float(valor_hora)
horas_trabalhadas = float(horas_trabalhadas)

salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = 11 # Imposto de renda desconta 11%
inss = 8 # INSS desconta 8%
sindicato = 5 # Sindicato desconta 5%

desconto_ir = imposto_renda / 100 * salario_bruto
desconto_inss = inss / 100 * salario_bruto
desconto_sindicato = sindicato / 100 * salario_bruto

descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - descontos

print(
    f'Salário bruto: R$ {salario_bruto:.2f}\n'
    f'Desconto IR (11%): R$ {desconto_ir:.2f}\n'
    f'Desconto INSS (8%): R$ {desconto_inss:.2f}\n'
    f'Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}\n'
    f'Salário liquido: R$ {salario_liquido:.2f}'
)
