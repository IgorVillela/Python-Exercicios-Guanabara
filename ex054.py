from datetime import date
ano_hoje = date.today().year
lista_maior = []
lista_menor = []

for i in range(7):
    nasc = int(input(f'Insira a data de nascimento da {i + 1}ª pessoa: '))
    idade = ano_hoje - nasc
    if idade >= 18:
        lista_maior.append(nasc)
    else:
        lista_menor.append(nasc)

print(f'Maior de idade: {lista_maior}')
print(f'Menor de idade: {lista_menor}')
print(f'Das datas de nascimento digitadas, {len(lista_maior)} pessoas são maior de idade e '
      f'{len(lista_menor)} pessoas são menor de idade.')
