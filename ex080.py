lista = []

while len(lista) < 5:
    print('-' * 62)
    try:
        valor = int(input('Digite um valor: '))
    except ValueError:
        continue
    if not lista or valor >= lista[-1]:
        lista.append(valor)
        print('Primeiro valor adicionado...' if len(lista) == 1 else
              f'Valor {valor} adicionado na posição final...')
    else:
        for t, item in enumerate(lista):
            if valor <= item:
                lista.insert(t, valor)
                print(f'Valor adicionado na posição {t + 1}...' if t != 0 else
                      'Valor adicionado na primeira posição...')
                break

print(f'{" RESUMO ":=^62}')
print(f'Os valores digitados em ordem crescente foram: {lista}')
