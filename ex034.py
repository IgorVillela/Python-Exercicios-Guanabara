salario = float(input('Qual o salário do funcionário? R$ '))

if salario <= 1250:
    aumento = 15
    salario_novo = salario * (100 + aumento) / 100
else:
    aumento = 10
    salario_novo = salario * (100 + aumento) / 100
print(
    f'O salário do funcionário teve um aumento de {aumento}% e passou de R$ {salario:.2f} para R$ {salario_novo:.2f}.')
