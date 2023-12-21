from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if fim > inicio:
        cont = inicio
        while cont <= fim:
            sleep(0.25)
            print(cont, end=' ')
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.25)
            print(cont, end=' ')
            cont -= passo
        print('FIM!')


def separador():
    print('-=' * 30)


inicio = fim = passo = 0

separador()
contador(1, 10, 1)
separador()
contador(10, 0, 2)
separador()
print('Agora é sua vez de personalizar a contagem!')
while True:
    try:
        inicio = int(input('Início: '))
    except ValueError:
        continue
    break
while True:
    try:
        fim = int(input('Fim: '))
    except ValueError:
        continue
    break
while True:
    try:
        passo = int(input('Passo: '))
    except ValueError:
        continue
    break
contador(inicio, fim, passo)
