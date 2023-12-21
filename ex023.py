num = int(input('Digite um número entre 0 e 9999: '))
num = str(num)

if len(num) == 4:
    print(f'Milhar: {num[0]}\nCentena: {num[1]}\nDezena: {num[2]}\nUnidade: {num[3]}')
elif len(num) == 3:
    print(f'Milhar: 0\nCentena: {num[0]}\nDezena: {num[1]}\nUnidade: {num[2]}')
elif len(num) == 2:
    print(f'Milhar: 0\nCentena: 0\nDezena: {num[0]}\nUnidade: {num[1]}')
elif len(num) == 1:
    print(f'Milhar: 0\nCentena: 0\nDezena: 0\nUnidade: {num[0]}')
elif len(num) == 0:
    print(f'Milhar: 0\nCentena: 0\nDezena: 0\nUnidade: 0')
else:
    print('O número digitado não está dentro da margem.')
