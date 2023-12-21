lista = list()
dados = list()
n = 0
soma = 0
soma3 = 0
maior_valor_2 = 0

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
for i, linha in enumerate(lista):
    for j, item in enumerate(linha):
        print(f'[{item:^3}]', end='')
        if item % 2 == 0:
            soma += item
        if j == 2:
            soma3 += item
        if i == 1:
            if j == 0 or item >= maior_valor_2:
                maior_valor_2 = item
    print()

print(f'A soma de todos os números pares é: {soma}')
print(f'A soma de todos os números da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {maior_valor_2}')
