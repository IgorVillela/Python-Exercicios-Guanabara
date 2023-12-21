from time import sleep

lista_geral = list()
lista_alunos = list()
notas = list()

while True:
    nome = input('Digite o nome do aluno: ')
    lista_alunos.append(nome)
    while True:
        try:
            n1 = float(input('Digite a 1ª nota do aluno: '))
        except ValueError:
            continue
        notas.append(n1)
        break
    while True:
        try:
            n2 = float(input('Digite a 2ª nota do aluno: '))
        except ValueError:
            continue
        notas.append(n2)
        break
    lista_alunos.append(notas[:])
    lista_geral.append(lista_alunos[:])
    lista_alunos.clear()
    notas.clear()
    opcao = 'S'
    while True:
        opcao = input('Deseja registrar outro aluno? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            print('=' * 40)
            break
    if opcao == 'N':
        break

print(f'{"Nº":<5}{"NOME":<20}{"MÉDIA":^10}')
print('-' * 40)
for i, aluno in enumerate(lista_geral):
    nome, nota = aluno
    print(f'{i + 1:<5}{nome:<20}{sum(nota)/len(nota):^10.1f}')

print('-' * 40)
n_aluno = 0
while True:
    try:
        n_aluno = int(input('Mostrar notas de qual aluno? (999 encerrar): '))
    except ValueError:
        continue
    if n_aluno == 999:
        break
    else:
        print('-' * 40)
        try:
            print(f'Aluno/a: {lista_geral[n_aluno - 1][0]}\n'
                  f'1ª Nota: {lista_geral[n_aluno - 1][1][0]}\n'
                  f'2ª Nota: {lista_geral[n_aluno - 1][1][1]}')
        except IndexError:
            print('Aluno não encontrado.')

print('ENCERRANDO...')
sleep(2)
print(f'{" PROGRAMA ENCERRADO ":=^40}')
