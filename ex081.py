lista = []
opcao = 'S'

while True:
    try:
        valor = int(input('Digite um número: '))
    except ValueError:
        continue
    lista.append(valor)
    while True:
        opcao = input('Deseja inserir outro valor? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

lista.sort(reverse=True)
print('=' * 50)
print(f'Foram digitados {len(lista)} valores.\n'
      f'A lista ordenada de forma decrescente: {lista}')
print(f'O número 5 foi digitado {lista.count(5)} vezes.' if 5 in lista else 'O número 5 não foi digitado')
if 5 in lista:
    print('Posições do digito 5: ', end='')
    for i, item in enumerate(lista):
        if item == 5:
            print(f'{i + 1}ª', end='')
            if lista[i + 1] == 5:
                print(', ', end='')
