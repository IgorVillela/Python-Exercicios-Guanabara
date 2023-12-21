while True:
    print('-=-' * 24)
    n = int(input('Digite um valor para ver sua tabuada (valor negativo para parar o programa): '))
    print('-=-' * 24)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i:<2} = {n * i}')
print('Programa encerrado.')
