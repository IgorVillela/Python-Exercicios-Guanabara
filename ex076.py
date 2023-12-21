tupla = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.90)

print('_' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('_' * 50)

for i, item in enumerate(tupla):
    if i == len(tupla):
        break
    if i % 2 == 0:
        print(f'{tupla[i]:.<40}R${tupla[i+1]:>8.2f}')

print('_' * 50)
