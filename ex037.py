numero = int(input('Escreva um número qualquer: '))
opcao = int(input('Digite qual opção de conversão deseja.\n1 - para binário\n2 - para octal\n3 - para hexadecimal'
                  '\nOpção: '))

if opcao == 1:
    print('Opção escolhida foi para binário.')
    numero = bin(numero)[2:]
elif opcao == 2:
    print('Opção escolhida foi para octal.')
    numero = oct(numero)[2:]
elif opcao == 3:
    print('Opção escolhida foi para hexadecimal.')
    numero = hex(numero)[2:].upper()
else:
    print('Opção digitada não existe.')
print(f'Conversão: {numero}')
