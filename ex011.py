largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura*altura
litro_tinta = area/2

print(f'Sua parede tem a dimensão de {largura} X {altura} e sua área é de {area} m².')
print(f'Para pintar essa parede, você precisará de {litro_tinta:.3f} L de tinta.')
