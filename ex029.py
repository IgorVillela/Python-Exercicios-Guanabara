velocidade = int(input('Qual a velocidade do carro em km/h? '))

if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f'Sua velocidade foi {velocidade} km/h, {velocidade-80} km/h acima do permitido!'
          f' Sua multa é de R$ {multa:.2f}.')
else:
    print('Você não foi multado =D')
