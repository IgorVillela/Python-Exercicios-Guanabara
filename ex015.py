d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
custo = d * 60 + 0.15 * km

print(f'O total a se pagar é R$ {custo:.2f}')
