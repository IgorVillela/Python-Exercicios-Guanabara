opcao = 0
soma = 0
contagem = 0

while opcao != 999:
    opcao = int(input('Digite um número para ser somado, ou 999 para encerrar. '))
    if opcao != 999:
        soma += opcao
        contagem += 1
print(f'Dos {contagem} números digitados, a soma total é {soma}.')
