lista = list()
cadastro = dict()
soma = 0

while True:
    cadastro['Nome'] = input('Insira o nome: ')
    while True:
        cadastro['Sexo'] = input('Insira o sexo [M/F]: ').strip().upper()[0]
        if cadastro['Sexo'] in 'MF':
            break
    while True:
        try:
            cadastro['Idade'] = int(input('Insira a idade: '))
        except ValueError:
            continue
        break
    lista.append(cadastro.copy())
    cadastro.clear()
    while True:
        opcao = input('Deseja inserir outro cadastro? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print(f'{" RESUMO ":=^40}')
# print(lista)
print(f'- Foram cadastradas {len(lista)} pessoas.')
for pessoa in lista:
    soma += pessoa['Idade']
print(f'- Média de idade das pessoas cadastradas: {soma/len(lista)} anos')
print('- Pessoas do sexo feminino: ', end='')
for pessoa in lista:
    if pessoa['Sexo'] == 'F':
        print(f"[{pessoa['Nome']}]", end=' ')
print()
print(f'- Pessoas com idade superior a média {soma/len(lista)}: ', end='')
for pessoa in lista:
    if pessoa['Idade'] > soma/len(lista):
        print(f'|{pessoa}|', end=' ')
print()

print(f'{" FIM DE PROGRAMA ":=^40}')
