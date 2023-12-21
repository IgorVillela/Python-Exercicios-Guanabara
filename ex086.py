lista = list()
dados = list()
n = 0

for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                n = int(input(f'Insira um valor na linha {linha + 1} e coluna {coluna + 1}: '))
            except ValueError:
                continue
            break
        dados.append(n)
    lista.append(dados[:])
    dados.clear()

print(f'{" MATRIZ ":=^30}')
for linha in lista:
    for i, item in enumerate(linha):
        print(f'[{item:^5}]', end='')
    print()
