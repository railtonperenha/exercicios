# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Digite M - Masculino ou F - Feminino: ')

    
letra = letra.capitalize()
if letra == 'M':
    print('O sexo é Masculino')
elif letra == 'F':
    print('O sexo é Feminino')
else:
    print('Sexo Inválido!')
