from random import randint
from time import sleep

contagem = 0

print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 19)
adivinho = int(input('Adivinhe um número entre 0 e 10! '))
valor = randint(0, 10)
print('PROCESSANDO...')
sleep(2)
contagem += 1
while adivinho != valor:
    if adivinho > valor:
        adivinho = int(input('Menos... tente mais uma vez. '))
        contagem += 1
        print('PROCESSANDO...')
        sleep(2)
    if adivinho < valor:
        adivinho = int(input('Mais... tente mais uma vez. '))
        contagem += 1
        print('PROCESSANDO...')
        sleep(2)
print('Você adivinhou certo!')
print(f'Você precisou jogar {contagem} vezes para vencer o robô!')
