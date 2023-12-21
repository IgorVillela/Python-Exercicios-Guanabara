soma = 0
lista = []
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        lista.append(i)
print(f'A soma total de números ímpares e divisíveis por 3 é: {soma}')
print(lista)
