def notas(*notas, sit=False):
    """
    -> Faz um relatório das notas de vários alunos.
    :param notas: Nota final do aluno (pode inserir diversas notas).
    :param sit: Valor opcional, mostra a situação da média das notas da sala.
    :return: Dicionário com os valores analisados da turma.
    """
    resumo = dict()
    cont = maior = menor = soma = 0
    for i, nota in enumerate(notas):
        cont += 1
        soma += nota
        if i == 0:
            maior = nota
            menor = nota
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
    resumo['Total'] = cont
    resumo['Maior nota'] = maior
    resumo['Menor nota'] = menor
    media = soma/len(notas)
    resumo['Média total'] = media
    if sit:
        if media > 7:
            resumo['Situação'] = 'BOA'
        elif media > 5:
            resumo['Situação'] = 'RAZOÁVEL'
        else:
            resumo['Situação'] = 'RUIM'
    return resumo


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
resp = notas(3, 9.5, 6, 6.5, sit=True)
print(resp)
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
