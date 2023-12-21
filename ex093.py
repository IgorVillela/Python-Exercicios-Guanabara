dados = dict()
lista = []

dados['Nome'] = input('Qual o nome do jogador? ')
partidas = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
for qtde in range(partidas):
    lista.append(int(input(f'Número de gols na {qtde + 1}ª partida: ')))
dados['Gols'] = lista[:]
dados['Total gols'] = sum(dados['Gols'])

print(dados)
print('=' * 40)
print(f"Nome: {dados['Nome']}\n"
      f"Gols: {dados['Gols']}\n"
      f"Total de gols: {dados['Total gols']}")
print('=' * 40)
print(f"O jogador {dados['Nome']} jogou {len(dados['Gols'])} partidas.")
for i, gols in enumerate(dados['Gols']):
    print(f'    => Na partida {i + 1}, fez {gols} gols.')
print(f"Foi um total de {dados['Total gols']}")
