cidade = input('Insira o nome de uma cidade: ').strip()

if 'SANTO' in cidade.upper().split()[0]:
    print('A cidade começa com SANTO no nome!')
else:
    print('A cidade NÃO começa com SANTO no nome')
