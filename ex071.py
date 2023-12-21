saque = 0
resto = 0
cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0

print('-' * 30)
print(f'{" CAIXA ELETRÔNICO ":=^30}')
print('-' * 30)

while True:
    try:
        saque = int(input('Quanto deseja sacar? R$ '))
    except ValueError:
        continue
    cedulas_50 = saque // 50
    resto = saque - cedulas_50 * 50
    if resto != 0:
        cedulas_20 = resto // 20
        resto -= cedulas_20 * 20
    if resto != 0:
        cedulas_10 = resto // 10
        resto -= cedulas_10 * 10
    if resto != 0:
        cedulas_1 = resto
        resto -= cedulas_1
    break
print(f'{" RESUMO ":=^30}')
print(f'Quantidade de cédulas a serem entregues:\n'
      f'R$ 50,00: {cedulas_50}\n'
      f'R$ 20,00: {cedulas_20}\n'
      f'R$ 10,00: {cedulas_10}\n'
      f'R$ {"1,00":>5}: {cedulas_1}')
