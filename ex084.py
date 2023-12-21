lista = list()
dados = list()
peso_max = peso_min = 0

while True:
    dados.append(input('Insira o nome: ').capitalize())
    while True:
        try:
            dados.append(float(input('Insira o peso em kg: ')))
        except ValueError:
            continue
        break
    lista.append(dados[:])
    dados.clear()
    opcao = 'S'
    while True:
        opcao = input('Deseja cadastrar outra pessoa? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print(f'{" RESUMO ":=^50}')
print(f'No total foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de ', end='')
for i, p in enumerate(lista):
    if i == 0 or p[1] >= peso_max:
        peso_max = p[1]
    if i == 0 or p[1] <= peso_min:
        peso_min = p[1]

print(f'{peso_max:.2f} kg. Peso de ', end='')
for p in lista:
    if peso_max == p[1]:
        print(f'[{p[0]}]', end=' ')
print()

print(f'O menor peso foi {peso_min:.2f} de ', end='')
for p in lista:
    if peso_min == p[1]:
        print(f'[{p[0]}]', end=' ')
