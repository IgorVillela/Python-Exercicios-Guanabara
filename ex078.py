lista = []
separador = '=-' * 30

for i in range(5):
    while True:
        try:
            valor = int(input(f'Digite um valor para a posição {i + 1}: '))
        except ValueError:
            continue
        lista.append(valor)
        break
print(separador)
print(f'Valores digitados: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, item in enumerate(lista):
    if max(lista) == item:
        print(f'{i + 1}...', end=' ')
print()
print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')
for i, item in enumerate(lista):
    if min(lista) == item:
        print(f'{i + 1}...', end=' ')
