def cadastrar():
    lista = list()
    flag = True
    print('-' * 40)
    print(f'{" CADASTRO DE PESSOAS ":-^40}')
    print('-' * 40)
    while flag:
        while True:
            nome = input('Digite o nome: ').title().strip()
            if nome and nome.replace(' ', '').isalpha():
                break
            else:
                print('Nome inválido. Tente novamente.')

        while True:
            try:
                idade = int(input('Digite a idade: '))
            except ValueError:
                print('Valor inválido. Tente novamente.')
                continue
            break

        lista.append([nome, idade])

        while True:
            while True:
                try:
                    resp = input('Deseja cadastrar mais pessoas? (S/N) ').strip().upper()[0]
                    if resp in 'SN':
                        if resp == 'S':
                            break
                        if resp == 'N':
                            flag = False
                            break
                    else:
                        print('Valor inválido. Tente novamente.')
                except IndexError:
                    print('Valor inválido. Tente novamente.')
                    continue
            break
    with open('Cadastro.txt', 'a') as arquivo:
        for pessoa in lista:
            arquivo.write(f'{pessoa[0]}, {pessoa[1]}\n')

    print(f'Dados {lista} cadastrados e salvos no arquivo Cadastro.txt')
    return lista


def deletar_linha():
    print('\033[1;31m-' * 40)
    print(f'{" DELETAR CADASTRO ":-^40}')
    print('-' * 40, end='')
    print('\033[m')
    try:
        with open('Cadastro.txt', 'r') as arquivo_leitura:
            linhas = arquivo_leitura.readlines()

        if not linhas:
            print('Nenhuma pessoa cadastrada para deletar.')
            return

        print('Pessoas cadastradas:')
        print('-' * 40)
        for i, linha in enumerate(linhas, 1):
            nome, idade = linha.strip().split(', ')
            print(f'{i} - Nome: {nome}, Idade: {idade}')
        print('-' * 40)

        try:
            numero_linha = int(input('\033[1;31mDigite o número da linha que deseja deletar: \033[m'))
        except ValueError:
            print('Valor inválido. Operação cancelada.')
            return

        if 1 <= numero_linha <= len(linhas):
            del linhas[numero_linha - 1]

            with open('Cadastro.txt', 'w') as arquivo_escrita:
                arquivo_escrita.writelines(linhas)

            print(f'\033[1;31mLinha {numero_linha} deletada com sucesso.\033[m')
        else:
            print('Número de linha inválido. Operação cancelada.')

    except FileNotFoundError:
        print('O arquivo Cadastro.txt não foi encontrado.')
