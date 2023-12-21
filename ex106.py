from time import sleep


def titulo(texto, cor='Verde'):
    if cor == 'Verde':
        cor = '\033[1;42m'
    elif cor == 'Azul':
        cor = '\033[1;44m'
    elif cor == 'Branco':
        cor = '\033[30;40m'
    elif cor == 'Vermelho':
        cor = '\033[1;41m'
    tamanho = len(texto) + 4
    print(f'{cor}~' * tamanho)
    print(texto.center(tamanho))
    print('~' * tamanho)
    print('\033[m', end='')


def ajuda():
    while True:
        print('\033[m', end='')
        titulo('SISTEMA DE AJUDA PyHELP')
        duvida = input('Função ou Biblioteca > ')
        if duvida == 'fim':
            titulo('ATÉ LOGO', cor='Vermelho')
            sleep(1)
            break
        titulo(f'Acessando o manual do comando "{duvida}"', cor='Azul')
        sleep(1)
        print('\033[7;40m', end='')
        help(duvida)
        print('\033[m', end='')
        sleep(1)


ajuda()
