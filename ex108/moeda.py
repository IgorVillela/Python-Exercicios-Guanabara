def aumentar(n, percent):
    return moeda(n*(1 + percent / 100))


def diminuir(n, percent):
    return moeda(n*(1 - percent / 100))


def dobro(n):
    return moeda(n*2)


def metade(n):
    return moeda(n/2)


def moeda(n):
    return f'R$ {n:.2f}'.replace('.', ',')
