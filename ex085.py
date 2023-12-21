lista = [[], []]
n = 0

for i in range(7):
    while True:
        try:
            n = int(input(f'Insira o {i + 1}º valor: '))
        except ValueError:
            continue
        break
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print(f'{" RESUMO ":=^30}')
print(f'Números pares: {lista[0]}\n'
      f'Números ímpares: {lista[1]}')
