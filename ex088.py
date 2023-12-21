from random import randint
from time import sleep

palpites = list()
dados = list()
n = 0

while True:
    try:
        n = int(input('Quantos jogos da MEGA SENA deseja simular? '))
    except ValueError:
        continue
    break

for i in range(n):
    for j in range(6):
        while True:
            valor = randint(1, 60)
            if valor in dados:
                valor = randint(1, 60)
            else:
                break
        dados.append(valor)
    dados.sort()
    palpites.append(dados[:])
    dados.clear()

print(f'{" SORTEANDO PALPITES ":=^30}')
for i, palpite in enumerate(palpites):
    sleep(1)
    print(f'{i + 1}º: {palpite}')
print(f'{" < BOA SORTE! > ":=^30}')
