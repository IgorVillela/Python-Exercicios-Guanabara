d = float(input('Distância em metros: '))

print(f'A distância {d:.0f} metros equivale a: \n'
      f'{d/1000} km \n'
      f'{d/100} hm \n'
      f'{d/10} dam \n'
      f'{d*10} dm \n'
      f'{d*100:.0f} cm \n'
      f'{d*1000:.0f} mm')
