def voto(ano_nasc):
    from datetime import date
    idade = date.today().year - ano_nasc
    if idade < 16:
        resposta = 'NÃO VOTA'
    elif idade >= 70 or idade < 18:
        resposta = 'VOTO OPCIONAL'
    else:
        resposta = 'VOTO OBRIGATÓRIO'
    print(f'Com {idade} anos: {resposta}')


#  Programa principal
print('-' * 30)
nascimento = 0
while True:
    try:
        nascimento = int(input('Em que ano você nasceu? '))
    except ValueError:
        continue
    break
voto(nascimento)
