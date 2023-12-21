print('-' * 17)
print('PROGRAMA FATORIAL')
print('-' * 17)

n = int(input('Digite um número: '))
resultado = 1
contagem = n

print(f'Calculando {n}! = ', end='')
while contagem > 0:
    resultado *= contagem
    print(f'{contagem}', end='')
    print(' x ' if contagem > 1 else ' = ', end='')
    contagem -= 1
print(f'{resultado}')

# for i in range(1, n + 1):
#     resultado *= i
# print(f'O fatorial de {n} é {resultado}')
