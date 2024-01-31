def leiaDinheiro():
    n = ''
    while True:
        try:
            n = input('Insira um valor: R$ ').strip().replace(',', '.')
            n = float(n)
        except ValueError:
            print(f'\033[31mERRO: \"{n}\" é um preço inválido!\033[m')
            continue
        break
    return n
