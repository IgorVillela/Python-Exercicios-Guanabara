def ficha(nome='', gols=0):
    if nome == '':
        nome = '<Desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
while True:
    try:
        gols = int(input('Número de gols: '))
    except ValueError:
        gols = 0
    break

ficha(nome, gols)
