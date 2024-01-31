from .cadastro import *
from .lista import *


def menu_principal():
    print('\033[1;33m-' * 40)
    print(f'{" SISTEMA DE CADASTRO ":=^40}')
    print('-' * 40, end='')
    print('\033[m')
    while True:
        print('O que deseja fazer?')
        try:
            opc = int(input(
                '''
\t1 - Novos cadastros
\t2 - Deletar cadastro
\t3 - Listar pessoas cadastradas
\t0 - Encerrar programa

Opção: '''))
        except:
            print('Valor inválido. Tente novamente.')
            continue
        if opc == 1:
            cadastrar()
        elif opc == 2:
            deletar_linha()
        elif opc == 3:
            ler_arquivo()
        elif opc == 0:
            break
        else:
            print('Valor inválido. Tente novamente.')
        print('-' * 40)
    print('\033[1;33m-' * 40)
    print(f'{" PROGRAMA ENCERRADO ":=^40}')
    print('-' * 40, end='')
    print('\033[m')
