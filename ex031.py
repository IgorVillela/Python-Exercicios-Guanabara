distancia = float(input('Qual a distância para o destino em km? '))

if distancia <= 200:
    preco_passagem = 0.50 * distancia
else:
    preco_passagem = 0.45 * distancia
print(f'O preço da passagem é R$ {preco_passagem:.2f}')
