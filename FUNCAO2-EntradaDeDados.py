def leiaInt(msg):
    n = str(input(msg))
    while n.isnumeric() == False:
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        n = str(input('Digite um número: '))
    else:
        return n
       



# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')