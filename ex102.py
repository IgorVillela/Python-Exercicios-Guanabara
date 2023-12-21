from time import sleep


def fatorial(num, show=True):
    """
    -> Calcula o fatorial de um número.
    :param num: Número do fatorial a ser calculado
    :param show: (opcional) Mostra ou não o processo de cálculo. Normalmente True
    """
    f = 1
    if show:
        print(f'O cálculo de {num}! é: ', end='')
        for i in range(num, 0, -1):
            f *= i
            if i != 1:
                sleep(0.5)
                print(i, end='')
                sleep(0.5)
                print(' x ', end='')
            else:
                sleep(0.5)
                print(i, end='')
        sleep(0.5)
        print(f' = ', end='')
        sleep(0.5)
        print(f)
    else:
        for i in range(num, 0, -1):
            f *= i
        print(f'Resultado de {num}! = {f}')


fatorial(5, show=False)
fatorial(5)
