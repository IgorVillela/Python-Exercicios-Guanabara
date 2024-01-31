def leiaInt(texto):
    print('-' * 20)
    while True:
        try:
            digito = input(texto)
            if isinstance(int(digito), int):
                return digito
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        break


#  Programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
