lista = []
lista_par = []
lista_impar = []

while True:
    try:
        valor = int(input('Digite um valor: '))
    except ValueError:
        continue
    lista.append(valor)
    while True:
        opcao = input('Deseja inserir mais valores? [S/N] ').strip().upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
    print('-' * 40)

for num in lista:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print('=' * 40)
print(f'Digitos inseridos: {lista}\n'
      f'Digitos pares: {lista_par}\n'
      f'Digitos ímpares: {lista_impar}')
