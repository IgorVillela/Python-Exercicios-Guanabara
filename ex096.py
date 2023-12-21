def area(l, c):
    area = l * c
    print(f'Área do terreno de {l} x {c} é {area} m².')


l = c = 0
print(f'{" CONTROLE DE TERRENOS ":^40}')
print('-' * 40)
while True:
    try:
        l = float(input('LARGURA (m): '))
    except ValueError:
        continue
    break
while True:
    try:
        c = float(input('COMPRIMENTO (m): '))
    except ValueError:
        continue
    break
area(l, c)
