def leiaInt(texto):
    print('-' * 20)
    while True:
        try:
            digito = input(texto)
            if isinstance(int(digito), int):
                return digito
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        break


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
