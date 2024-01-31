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
