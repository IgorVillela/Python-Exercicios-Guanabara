tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

opcao = 'S'

n = ''
while True:
    try:
        n = int(input('Digite um valor entre 0 e 20: '))
    except ValueError:
        continue
    if n in range(0, 21):
        print(f'O número digitado {n} em extenso equivale a {tupla[n]}')
        while True:
            opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
            if opcao not in 'SN':
                continue
            else:
                break
    if opcao == 'N':
        break
