tupla = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'RB Bragantino', 'Fluminense', 'Athletico PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')

separador = '-=' * 18

primeiros = tupla[:5]
ultimos4 = tupla[-4:]
ordemalfa = sorted(tupla)
time = 'São Paulo'
nome = tupla[tupla.index(time)]
pos = tupla.index(time)

print(separador)
print(f'Primeiros 5 colocados: {primeiros}\n'
      f'{separador}\n'
      f'Últimos 4 colocados: {ultimos4}\n'
      f'{separador}\n'
      f'Lista times em ordem alfabética: {ordemalfa}\n'
      f'{separador}\n'
      f'Posição do time {nome} é {pos+1}º lugar\n'
      f'{separador}')
