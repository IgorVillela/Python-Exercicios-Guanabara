contagem_maior_18 = contagem_homem = contagem_mulher_menor_20 = idade = 0

while True:
    print('_' * 30)
    print(f'{"CADASTRO PESSOA":^30}')
    print('_' * 30)
    while True:
        try:
            idade = int(input('Insira a idade: '))
        except ValueError:
            continue
        else:
            break
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Insira o sexo [M/F]: ').strip().upper()[0]
    print('_' * 30)
    if idade >= 18:
        contagem_maior_18 += 1
    if sexo == 'M':
        contagem_homem += 1
    if sexo == 'F' and idade < 20:
        contagem_mulher_menor_20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja cadastrar mais uma pessoa? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^30}')
print(f'Pessoas com mais de 18 anos: {contagem_maior_18}\n'
      f'Total homens: {contagem_homem}\n'
      f'Total mulheres com menos de 20 anos: {contagem_mulher_menor_20}')
