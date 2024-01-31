def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Número do fatorial a ser calculado
    :param show: (opcional) Mostra ou não o processo de cálculo. Normalmente True
    """
    from time import sleep
    f = 1
    if show:
        print(f'O cálculo de {num}! é: ', end='')
    for i in range(num, 0, -1):
        if show:
            if i != 1:
                sleep(0.25)
                print(i, end='')
                sleep(0.25)
                print(' x ', end='')
            else:
                sleep(0.25)
                print(i, end='')
                sleep(0.25)
                print(f' = ', end='')
                sleep(0.25)
        f *= i
    return f


#  Programa principal
print(fatorial(5, show=True))
print(fatorial(5))
