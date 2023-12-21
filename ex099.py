from time import sleep


def maior(*num):
    print('-=' * 23)
    print('Analisando os valores passados...')
    n_maior = 0
    for i, n in enumerate(num):
        sleep(0.25)
        print(n, end=' ')
        if i == 0:
            n_maior = n
        else:
            if n > n_maior:
                n_maior = n
    print(f'Foram informados {len(num)} valores ao todo.'
          if len(num) > 1 or len(num) == 0 else
          f'Foi informado {len(num)} valor ao todo.')
    print(f'O maior número é: {n_maior}.'
          if n_maior != 0 else
          'Não há maior valor.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
