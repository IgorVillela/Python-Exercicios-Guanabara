from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
adivinho = int(input('Adivinhe um número entre 0 e 5! '))
valor = randint(0, 5)
print('PROCESSANDO...')
sleep(2)

print(f'Pensei em {valor} e você {adivinho}')
print('Você adivinhou certo!' if adivinho == valor else 'Você errou! =(')
