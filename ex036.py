casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
amort = int(input('Em quantos anos pretende pagar? '))

pagamento = casa / (amort * 12)

if pagamento >= salario * 0.3:
    print(f'A prestação mensal de R$ {pagamento:,.2f}/mês excede os 30% do salário (R$ {salario * 0.3:.2f}). '
          f'\nEmpréstimo NEGADO.')
else:
    print(f'A prestação mensal de R$ {pagamento:,.2f}/mês está de acordo.\nEmpréstimo APROVADO.')
