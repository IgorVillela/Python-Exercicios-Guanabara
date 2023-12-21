sexo = input('Digite o sexo: [M/F] ').upper().strip()

while sexo not in 'MF':
    print('Dígito não reconhecido. Tente novamente.')
    sexo = input('Digite o sexo: [M/F] ').upper().strip()
print(f'Sexo {sexo} registrado com sucesso!')
print('FIM')
