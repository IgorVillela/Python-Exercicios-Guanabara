from random import randint

tupla = ()

for i in range(5):
    n = randint(1, 101)
    tupla += (n,)

print('Os valores sorteados foram: ', end='')
for i in tupla:
    print(i, end=' ')
print('')

print(f'Maior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')
