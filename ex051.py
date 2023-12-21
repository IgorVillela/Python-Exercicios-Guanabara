n = float(input('Insira um valor: '))
r = float(input('Escolha a razão: '))

print('Sua P.A. é:')
print(n, end=' > ')
for i in range(9):
    n += r
    print(n, end=' > ')
print('FIM')
