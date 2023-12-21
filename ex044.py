print(f"{'LOJA VILLELA':=^40}")

preco = float(input('Qual o preço do produto? R$ '))
opcao = int(input('Qual a opção de pagamento?\n'
                  '1 - à vista dinheiro/cheque\n'
                  '2 - à vista no cartão\n'
                  '3 - 2x no cartão\n'
                  '4 - 3x ou mais no cartão\n'
                  'Opção: '))

if opcao == 1:
    preco_novo = preco * 0.9
    print(f'O preço a se pagar é R$ {preco_novo:.2f}')
elif opcao == 2:
    preco_novo = preco * 0.95
    print(f'O preço a se pagar é R$ {preco_novo:.2f}')
elif opcao == 3:
    print(f'O preço a se pagar é R$ {preco:.2f} em 2 parcelas de R$ {preco / 2:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? (3 até 12) '))
    if 3 <= parcelas <= 12:
        preco_novo = preco * 1.20
        preco_parcelado = preco_novo / parcelas
        print(f'O preço a se pagar é R$ {preco_novo:.2f}, em {parcelas} parcelas de R$ {preco_parcelado:.2f}')
    else:
        print('Parcelamento fora da margem.')
else:
    print('Opção selecionada não existe. Tente novamente.')
