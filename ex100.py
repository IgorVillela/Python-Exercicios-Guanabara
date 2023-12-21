from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        sleep(0.5)
        n = randint(0, 10)
        print(n, end=' ')
        lista.append(n)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = list()
sorteia(num)
somaPar(num)
