maior_peso = 0
menor_peso = 0

for i in range(5):
    peso = float(input(f'Insira o peso da {i + 1}ª pessoa em kg: '))
    if i == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'Maior peso: {maior_peso} kg')
print(f'Menor peso: {menor_peso} kg')

# lista = []
#
# for i in range(5):
#     peso = float(input(f'Insira o peso da {i + 1}ª pessoa em kg: '))
#     lista.append(peso)
#     lista.sort()
# print(f'Maior peso: {lista[-1]} kg')
# print(f'Menor peso: {lista[0]} kg')
