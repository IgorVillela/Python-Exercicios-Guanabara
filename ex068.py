from random import randint
from time import sleep

print('-+-' * 4)
print('PAR OU ÍMPAR')
print('-+-' * 4)

contagem = 0
n = 0

while True:
    while True:
        escolha = input('Escolha PAR ou ÍMPAR [P/I]: ').strip().upper().replace('Í', 'I')[0]
        if escolha in 'PI':
            break
        else:
            continue
    while True:
        try:
            n = int(input('Escolha um valor entre 0 e 10: '))
        except ValueError:
            continue
        else:
            break
    computador = randint(0, 10)
    if n not in range(0, 11):
        print('Escolha um valor válido.')
    else:
        soma = n + computador
        for i in range(1, 4):
            print(f'{i}...')
            sleep(0.5)
            if i == 3:
                print('e...!')
                sleep(1)
                print('JÁ!')
                sleep(0.5)
                print(f'O computador jogou {computador} e você {n}.', end=' ')
        if soma % 2 == 0:
            print(f'{soma} é PAR.')
            if escolha == 'P':
                print('Você venceu!\nVamos jogar mais uma vez...')
                contagem += 1
            else:
                print('Você perdeu... ;(')
                break
        else:
            print(f'{soma} é ÍMPAR.')
            if escolha == 'I':
                print('Você venceu!\nVamos jogar mais uma vez...')
                contagem += 1
            else:
                print('Você perdeu... ;(')
                break
print(f'Você venceu {contagem} vezes consecutivas!')
