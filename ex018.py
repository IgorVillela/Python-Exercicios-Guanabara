from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo em graus: '))
rad = radians(ang)

print(f'O ângulo de {ang}º possuí:'
      f'\nSENO: {sin(rad):.2f} rad'
      f'\nCOSSENO: {cos(rad):.2f} rad'
      f'\nTANGENTE: {tan(rad):.2f} rad')
