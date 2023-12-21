from math import hypot

co = float(input('Insira o cateto oposto em cm: '))
ca = float(input('Cateto adjacente em cm: '))

print(f'O triângulo com cateto oposto {co} e adjacente {ca} tem a hipotenusa {hypot(ca, co):.2f}')
