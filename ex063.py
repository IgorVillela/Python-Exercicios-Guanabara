# n = int(input('Digite um número: '))
# contagem = 0
# lista = [0, 1]
#
# if n == 0:
#     print('FIM')
# elif n == 1:
#     print(lista[0])
# elif n == 2:
#     print(lista)
# else:
#     while contagem != n - 2:
#         c = lista[contagem] + lista[contagem + 1]
#         lista.append(c)
#         contagem += 1
#     print(lista)
#     print('FIM')

n1 = 0
n2 = 1
nn = 0
contagem = 2

qtde = int(input('Quantos termos da sequência de Fibonacci você quer ver? (0 para sair) '))

if qtde == 0:
    print('Programa encerrado.')
elif qtde == 1:
    print(n1, '> FIM')
elif qtde == 2:
    print(f'{n1} > {n2} > FIM')
else:
    print(f'{n1} > {n2}', end=' > ')
    while contagem < qtde:
        nn = n1 + n2
        n1 = n2
        n2 = nn
        print(nn, end='')
        contagem += 1
        if contagem < qtde:
            print(' > ', end='')
        else:
            print(' > FIM')
