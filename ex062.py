n = float(input('Insira um valor: '))
r = float(input('Escolha a razão: '))
contagem = 1
termos = 10
q_termos = termos

print('Sua P.A. é:')
print(n, end=' > ')
while termos != 0:
    while contagem < q_termos:
        n += r
        print(n, end=' > ')
        contagem += 1
    print('PAUSA')
    termos = int(input('\nGostaria de ver mais quantos termos? (digite 0 para encerrar): '))
    q_termos += termos
print(f'P.A. finalizada com {contagem} termos mostrados.')
print('FIM')
