from datetime import date

nascimento = int(input('Qual ano que você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'Idade: {idade} anos')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
