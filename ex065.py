contagem = 0
soma = 0
maior = 0
menor = 0
continuar = 'S'

while continuar == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    contagem += 1
    if contagem == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        else:
            menor = n
    continuar = input('Deseja continuar inserindo valores? [S/N] ').upper().strip()
media = soma / contagem

print(f'Dos {contagem} números digitados, temos:\nMédia: {media}\nMaior número: {maior}\nMenor número: {menor}')
