s = float(input('Qual o salário do Funcionário? R$ '))
aumento = 15  # Valor em %
novo_s = s * (100 + aumento) / 100

print(f'Um funcionário que ganhava {s:.2f}, com {aumento}% de aumento passará a receber R$ {novo_s:.2f}.')
