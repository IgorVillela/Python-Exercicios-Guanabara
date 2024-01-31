def leiaInt(texto):
    print('-' * 30)
    while True:
        try:
            digito = int(input(texto))
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar o número.\033[m')
            return 0
        return digito


def leiaFloat(texto):
    print('-' * 30)
    while True:
        try:
            digito = float(input(texto))
        except ValueError:
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar o número.\033[m')
            return 0
        return digito


#  Programa principal
n1 = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número inteiro {n1}')

n2 = leiaFloat('Digite um número float: ')
print(f'Você digitou o número real {n2}')
