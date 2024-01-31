def aumentar(n, percent, formatado=True):
    res = n*(1 + percent / 100)
    if formatado:
        return moeda(res)
    else:
        return res


def diminuir(n, percent, formatado=True):
    res = n*(1 - percent / 100)
    if formatado:
        return moeda(res)
    else:
        return res


def dobro(n, formatado=True):
    res = n*2
    if formatado:
        return moeda(res)
    else:
        return res


def metade(n, formatado=True):
    res = n/2
    if formatado:
        return moeda(res)
    else:
        return res


def moeda(n):
    return f'R$ {n:.2f}'.replace('.', ',')


def resumo(n, aumento, reduz):
    espacamento = len(f'Preço analisado: \t{moeda(n)}') + 2
    print('-' * espacamento)
    print(f'{" RESUMO DO VALOR ".center(espacamento)}')
    print('-' * espacamento)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento)}')
    print(f'{reduz}% de redução: \t{diminuir(n, reduz)}')
    print('-' * espacamento)
