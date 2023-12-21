from datetime import date

ano_atual = date.today().year
cadastro = dict()

cadastro['Nome'] = input('Insira o nome: ')
cadastro['Nascimento'] = int(input('Insira o ano de nascimento: '))
cadastro['CTPS'] = int(input('Insira o nº da carteira de trabalho (0 se não tiver): '))

if cadastro['CTPS'] != 0:
    cadastro['Idade'] = ano_atual - cadastro['Nascimento']
    cadastro['Ano contratação'] = int(input('Qual foi o ano de contratação? '))
    cadastro['Salário'] = float(input('Qual o salário? R$ '))
    cadastro['Idade aposentadoria'] = cadastro['Idade'] + (35 - (ano_atual - cadastro['Ano contratação']))
    print('=' * 40)
    # print(cadastro)
    print(f'Nome: {cadastro["Nome"]}\n'
          f'Idade: {cadastro["Idade"]} anos\n'
          f'CTPS: {cadastro["CTPS"]}\n'
          f'Ano contratação: {cadastro["Ano contratação"]}\n'
          f'Salário: R$ {cadastro["Salário"]:.2f}\n'
          f'Aposentadoria com idade: {cadastro["Idade aposentadoria"]} anos')
else:
    print('=' * 40)
    cadastro['Idade'] = ano_atual - cadastro['Nascimento']
    print(f'Nome: {cadastro["Nome"]}\n'
          f'Idade: {cadastro["Idade"]} anos\n'
          f'CTPS: {cadastro["CTPS"]}')

