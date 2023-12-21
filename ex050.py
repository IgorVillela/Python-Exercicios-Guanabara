soma = 0
cont = 0

for i in range(6):
    n = int(input(f'{i + 1}º valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma total dos {cont} números pares é: {soma}')
