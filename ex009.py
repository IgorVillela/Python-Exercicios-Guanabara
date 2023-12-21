n = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)
for s in range(1, 11, 1):
    print(f'{n} X {s:<2} = {n * s}')
print('-' * 12)
