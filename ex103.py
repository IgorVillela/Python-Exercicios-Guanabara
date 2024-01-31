def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#  Programa principal
print('-' * 30)
nome = input('Nome do jogador: ')
gols = 0
while True:
    try:
        gols = int(input('Número de gols: '))
    except ValueError:
        continue
    break
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
