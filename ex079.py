lista = []
opcao = 'S'

while True:
    try:
        valor = int(input('Insira um valor: '))
    except ValueError:
        continue
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        opcao = input('Deseja continuar? [S/N] ').strip().upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print('-=' * 30)
lista.sort()
print(f'Os valores únicos digitados foram: ', end='')
for i, item in enumerate(lista):
    print(item, end='')
    if i < len(lista) - 1:
        print(', ', end='')
