n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print(f'Sua média é {media:.1f}')
if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
