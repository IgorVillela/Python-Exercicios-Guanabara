from random import choice
from time import sleep

cores = {'Verde': '\033[32m',
         'Vermelho': '\033[31m',
         'Amarelo': '\033[1;33m',
         'Titulo': '\033[1;30;44m',
         'Limpa': '\033[m'}

print(f"{cores['Amarelo']}-=-{cores['Limpa']}" * 5)
print(f"{cores['Titulo']}JOGO JOKENPÔ!{cores['Limpa']}".center(28, "="))
print(f"{cores['Amarelo']}-=-{cores['Limpa']}" * 5)

opcao = int(input('Escolha uma opção!\n'
                  '1 - Pedra\n'
                  '2 - Papel\n'
                  '3 - Tesoura\n'
                  'Opção: '))
if 1 < opcao > 3:
    print('Opção invalida!')
else:
    lista = ['Pedra', 'Papel', 'Tesoura']
    bot = choice(['Pedra', 'Papel', 'Tesoura'])

    print('+' * 16)
    print('JO...', end='')
    sleep(1)
    print('KEN...', end='')
    sleep(1)
    print('PÔ!!!')
    print('+' * 16)
    sleep(1)
    print(f'O bot escolheu {bot}!')

    if lista[opcao-1] == 'Pedra' and bot == 'Tesoura' or \
            lista[opcao-1] == 'Papel' and bot == 'Pedra' or \
            lista[opcao-1] == 'Tesoura' and bot == 'Papel':
        print(f"{lista[opcao-1]} vence {bot}. {cores['Verde']}Você ganhou!")
    elif lista[opcao-1] == bot:
        print(f"{lista[opcao-1]} empata com {bot}. {cores['Amarelo']}Empate")
    else:
        print(f"{lista[opcao-1]} perde para {bot}. {cores['Vermelho']}Você perdeu :(")
