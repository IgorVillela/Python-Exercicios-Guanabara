real = float(input('Quanto dinheiro você possui? R$ '))
dolar = real/4.92
euro = real/5.36
iene = real/0.034

print(f'Com R$ {real} você pode comprar USD {dolar:.2f}, EUR {euro:.2f} ou JPY {iene:.2f}')
