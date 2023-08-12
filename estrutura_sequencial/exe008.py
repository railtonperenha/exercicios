valor_hora = input('Valor ganho por hora: R$ ')
horas_trabalhadas = input('Horas trabalhadas: ')

valor_hora = float(valor_hora)
horas_trabalhadas = float(horas_trabalhadas)
salario = valor_hora * horas_trabalhadas

print(
    f'Valor recebido por hora {valor_hora:.2f}\n'
    f'Horas trabalhadas: {horas_trabalhadas} horas\n'
    f'Salário: R$ {salario:.2f}'.replace('.', ',')
)