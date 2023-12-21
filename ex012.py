p = float(input('Qual é o preço do produto? R$ '))
desconto = 5  # Valor em %
novo_p = p * (100 - desconto) / 100

print(f'O produto que custava R$ {p:.2f}, na promoção com desconto de 5% vai custar R$ {novo_p:.2f}.')
