from time import sleep

n1 = float(input('Digite o primeiro valor. '))
n2 = float(input('Digite o segundo valor. '))
opcao = 0

while opcao != 5:
    opcao = int(input('Qual ação deseja realizar?\n'
                      '[1] - Somar\n'
                      '[2] - Multiplicar\n'
                      '[3] - Maior\n'
                      '[4] - Novos números\n'
                      '[5] - Sair do programa\n'
                      'Opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma é {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação é {n1} x {n2} = {multiplicacao}')
    elif opcao == 3:
        if n1 == n2:
            print('Os números são iguais. Não há maior.')
        else:
            lista = [n1, n2]
            lista.sort()
            print(f'O maior número entre {n1} e {n2} é {lista[1]}')
    elif opcao == 4:
        n1 = float(input('Digite o primeiro valor. '))
        n2 = float(input('Digite o segundo valor. '))
    elif opcao == 5:
        print('ENCERRANDO PROGRAMA...')
        sleep(2)
    else:
        print('Ação não existe. Tente novamente.')
    print('=' * 37)
print('FIM DE PROGRAMA')
