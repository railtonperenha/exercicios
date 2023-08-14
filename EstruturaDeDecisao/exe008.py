# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = input('Produto 1: R$ ')
produto2 = input('Produto 2: R$ ')
produto3 = input('Produto 3: R$ ')

try:
    produto1 = float(produto1)
    produto2 = float(produto2)
    produto3 = float(produto3)
    
    if produto1 < produto2 and produto1 < produto3:
        print(f'Você deve comprar o Produto 1, no valor de R$ {produto1:.2f}')
    elif produto2 < produto1 and produto2 < produto3:
        print(f'Você deve comprar o Produto 2, no valor de R$ {produto2:.2f}')
    elif produto3 < produto1 and produto3 < produto2:
        print(f'Você deve comprar o Produto 3, no valor de R$ {produto3:.2f}')
except:
    print('Digite apenas valores númericos!')
