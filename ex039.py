from datetime import date

sexo = input('Qual o seu sexo? (M/F) ').upper()

if sexo == 'F':
    print('Não há necessidade de alistamento militar.')
elif sexo == 'M':
    nascimento = int(input('Qual o ano de nascimento? '))
    ano_atual = date.today().year
    dif = ano_atual - nascimento
    alistamento = abs(18 - dif)

    if dif < 18:
        print(f'Você tem {dif} anos, ainda vai se alistar. Faltam {alistamento} anos para o alistamento militar.\n'
              f'Seu alistamento será em {ano_atual + alistamento}')
    elif dif == 18:
        print(f'Você tem {dif} anos, está na hora de se alistar! BRASIL!')
    else:
        print(f'Você tem {dif} anos, o prazo de alistamento já passou fazem {alistamento} anos.\n'
              f'Seu alistamento foi em {ano_atual - alistamento}.\n'
              f'Espero que tenha servido ou sido dispensado, hein...')
else:
    print('Digito inválido. Reinicie.')
