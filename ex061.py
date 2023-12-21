n = float(input('Insira um valor: '))
r = float(input('Escolha a razão: '))
contagem = 0

print('Sua P.A. é:')
print(n, end=' > ')
while contagem < 9:
    n += r
    contagem += 1
    print(n, end=' > ')
print('FIM')
