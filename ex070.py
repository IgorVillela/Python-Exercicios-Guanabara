total = preco = 0
ticket_1000 = 0
menor_preco = 0
nome_produto_mais_barato = ''

print('=' * 30)
print(f'{" LOJA DO IGU ":=^30}')
print('=' * 30)

while True:
    nome_produto = input('Nome do produto: ').strip()
    while True:
        try:
            preco = float(input('Preço do produto: R$ '))
        except ValueError:
            continue
        else:
            break
    total += preco
    if preco > 1000:
        ticket_1000 += 1
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        nome_produto_mais_barato = nome_produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
    print('-' * 30)
    if opcao == 'N':
        break
print(f'{" RESUMO ":=^30}')
print(f'Total gasto: R$ {total:,.2f}\n'
      f'Quantidade de produtos acima de R$ 1000,00: {ticket_1000}\n'
      f'Produto mais barato: {nome_produto_mais_barato}')
