# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor_hora = input('Valor por hora: R$ ')
horas_mes = input('Horas trabalhadas: ')

try:
    valor_hora = float(valor_hora)
    horas_mes = int(horas_mes)
    salario_bruto = valor_hora * horas_mes

    if salario_bruto <= 900:
        ir = 'Isento'
        sindicato = salario_bruto * 3 / 100
        inss = salario_bruto * 10 / 100
        fgts = salario_bruto * 11 / 100
        salario_liquido = salario_bruto - sindicato - inss
        
        print()
        print(
            f'Salario Bruto ({valor_hora} x {horas_mes}): R$ {salario_bruto:.2f}\n'
            f'(-) IR: {ir}\n'
            f'(-) INSS (10%): R$ {inss:.2f}\n'
            f'FGTS (11%): R$ {fgts:.2f}\n'
            f'Total de descontos: R$ {sindicato + inss:.2f}\n'
            f'Salário liquido: R$ {salario_liquido:.2f}'
        )
    
    elif salario_bruto <= 1500:
        ir = salario_bruto * 5 / 100
        sindicato = salario_bruto * 3 / 100
        inss = salario_bruto * 10 / 100
        fgts = salario_bruto * 11 / 100
        total_descontos = ir + sindicato + inss
        salario_liquido = salario_bruto - total_descontos

        print()
        print(
            f'Salario Bruto ({valor_hora:.2f} x {horas_mes}hrs): R$ {salario_bruto:.2f}\n'
            f'(-) IR (5%): R$ {ir}\n'
            f'(-) INSS (10%): R$ {inss:.2f}\n'
            f'FGTS (11%): R$ {fgts:.2f}\n'
            f'Total de descontos: R$ {total_descontos:.2f}\n'
            f'Salário liquido: R$ {salario_liquido:.2f}'
        )
    
    elif salario_bruto <= 2500:
        ir = salario_bruto * 10 / 100
        sindicato = salario_bruto * 3 / 100
        inss = salario_bruto * 10 / 100
        fgts = salario_bruto * 11 / 100
        total_descontos = ir + sindicato + inss
        salario_liquido = salario_bruto - total_descontos

        print()
        print(
            f'Salario Bruto ({valor_hora} x {horas_mes}): R$ {salario_bruto:.2f}\n'
            f'(-) IR (10%): R$ {ir}\n'
            f'(-) INSS (10%): R$ {inss:.2f}\n'
            f'FGTS (11%): R$ {fgts:.2f}\n'
            f'Total de descontos: R$ {total_descontos:.2f}\n'
            f'Salário liquido: R$ {salario_liquido:.2f}'
        )
    
    else:
        ir = salario_bruto * 20 / 100
        sindicato = salario_bruto * 3 / 100
        inss = salario_bruto * 10 / 100
        fgts = salario_bruto * 11 / 100
        total_descontos = ir + sindicato + inss
        salario_liquido = salario_bruto - total_descontos

        print()
        print(
            f'Salario Bruto ({valor_hora} x {horas_mes}): R$ {salario_bruto:.2f}\n'
            f'(-) IR (20%): R$ {ir}\n'
            f'(-) INSS (10%): R$ {inss:.2f}\n'
            f'FGTS (11%): R$ {fgts:.2f}\n'
            f'Total de descontos: R$ {total_descontos:.2f}\n'
            f'Salário liquido: R$ {salario_liquido:.2f}'
        )

except:
    print('Digite valores corretos')