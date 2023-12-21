from random import randint
from time import sleep
from operator import itemgetter

jogos = dict()
lista = list()

print('Valores sorteados:')
for i in range(4):
    jogos["Jogador"] = i + 1
    jogos["Dado"] = randint(1, 6)
    lista.append(jogos.copy())
    sleep(0.5)
    print(f'    O jogador {jogos["Jogador"]} tirou {jogos["Dado"]}')
    sleep(0.5)
    jogos.clear()

lista_ordenada = sorted(lista, key=lambda k: k['Dado'], reverse=True)
# lista_ordenada = sorted(lista, key=itemgetter('Dado'), reverse=True)
# print(lista_ordenada)
print('Ranking dos jogadores:')
for i, jogos in enumerate(lista_ordenada):
    print(f'    {i + 1}º lugar: Jogador {jogos["Jogador"]} com {jogos["Dado"]}')
