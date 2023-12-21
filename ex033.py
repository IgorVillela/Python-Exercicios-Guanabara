n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

lista = [n1, n2, n3]
lista.sort()

print(f'O maior número é: {lista[2]}\nO menor número é: {lista[0]}')
