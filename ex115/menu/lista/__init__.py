def ler_arquivo():
    try:
        with open('Cadastro.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print('Nenhuma pessoa cadastrada.')
                return

            print('-' * 40)
            print('PESSOAS CADASTRADAS'.center(40))
            print('-' * 40)
            for i, linha in enumerate(linhas, 1):
                nome, idade = linha.strip().split(', ')
                print(f'{i} - Nome: {nome}, Idade: {idade}')
    except FileNotFoundError:
        print('O arquivo Cadastro.txt não foi encontrado.')
