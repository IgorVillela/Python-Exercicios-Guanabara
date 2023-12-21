dados = dict()
lista_gols = list()
lista_geral = list()
escolha = ''

while True:
    dados['Nome'] = input('Qual o nome do jogador? ')
    while True:
        try:
            dados['Partidas'] = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
        except ValueError:
            continue
        if dados['Partidas'] == 0:
            print('Não é possível cadastrar um jogador que não jogou nenhuma partida.')
            continue
        break
    for qtde in range(dados['Partidas']):
        lista_gols.append(int(input(f'  Número de gols na {qtde + 1}ª partida: ')))
    dados['Gols'] = lista_gols.copy()
    dados['Total gols'] = sum(dados['Gols'])
    lista_geral.append(dados.copy())
    dados.clear()
    lista_gols.clear()
    while True:
        opcao = input('Deseja cadastrar outro jogador? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print('=' * 45)
while True:
    print(f"{'cod.':<5}{'Nome':<15}{'Gols':<20}{'Total':<5}")
    print('-' * 45)
    for i, jogador in enumerate(lista_geral):
        print(f'{i + 1:<5}{jogador["Nome"]:<15}{str(jogador["Gols"]):<20}{jogador["Total gols"]:<5}')
    print('-' * 45)
    while True:
        try:
            escolha = int(input('Escolha o cod. do jogador que deseja ver mais detalhes (0 para encerrar): '))
        except ValueError:
            continue
        if escolha == 0:
            break
        if escolha in range(len(lista_geral) + 1):
            print(f'{" DETALHES ":=^40}')
            print(f"Nome: {lista_geral[escolha - 1]['Nome']}\n"
                  f"Gols: {lista_geral[escolha - 1]['Gols']}\n"
                  f"Total de gols: {lista_geral[escolha - 1]['Total gols']}")
            print(f"O jogador {lista_geral[escolha - 1]['Nome']} "
                  f"jogou {lista_geral[escolha - 1]['Partidas']} partidas.")
            for n, gols in enumerate(lista_geral[escolha - 1]['Gols']):
                print(f'    => Na partida {n + 1}, fez {gols} gols.' if gols > 1 or gols == 0 else
                      f'    => Na partida {n + 1}, fez {gols} gol.')
            print(f"Foi um total de {lista_geral[escolha - 1]['Total gols']} gols."
                  if lista_geral[escolha - 1]['Total gols'] > 1 or lista_geral[escolha - 1]['Total gols'] == 0 else
                  f"Foi um total de {lista_geral[escolha - 1]['Total gols']} gol.")
            print(f'{" FIM DE DETALHES ":=^40}')
            break
    if escolha == 0:
        print('>>> FIM DE PROGRAMA <<<')
        break
