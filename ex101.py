from datetime import date


def voto(ano_nasc):
    idade = date.today().year - ano_nasc
    if idade < 18:
        resposta = 'VOTO NEGADO'
    elif idade < 65:
        resposta = 'VOTO OBRIGATÓRIO'
    else:
        resposta = 'VOTO OPCIONAL'
    print(f'Com {idade} anos: {resposta}')


print('-' * 30)
nascimento = 0
while True:
    try:
        nascimento = int(input('Em que ano você nasceu? '))
    except ValueError:
        continue
    break
voto(nascimento)
