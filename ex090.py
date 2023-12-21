aluno = dict()

aluno['Nome'] = input('Nome do aluno: ')
while True:
    try:
        aluno['Média'] = float(input(f'Qual foi a média de {aluno["Nome"]}: '))
    except ValueError:
        continue
    if 0 <= aluno['Média'] <= 10:
        break

print(f'O nome do aluno é {aluno["Nome"]}\n'
      f'A média é igual a {aluno["Média"]}')

if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'DE RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'

print(aluno)
print(f'O aluno está {aluno["Situação"]}')
