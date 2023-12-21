n = int(input('Insira um valor: '))
lista = []

if n <= 0 or n == 1:
    print(f'O valor {n} não é primo!')
else:
    for i in range(2, n):
        contagem = i
        if n % contagem == 0:
            lista.append(contagem)
    if len(lista) != 0:
        print(f'O número {n} não é primo!')
        print(f'O número {n} é divisível por {lista}')
    else:
        print(f'O número {n} é primo!')
