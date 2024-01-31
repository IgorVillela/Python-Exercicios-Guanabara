def notas(*notas, sit=False):
    """
    -> Faz um relatório das notas de vários alunos.
    :param notas: Nota final do aluno (pode inserir várias notas).
    :param sit: Valor opcional, mostra a situação da média das notas da sala.
    :return: Dicionário com os valores analisados da turma.
    """
    resumo = dict()
    resumo['Total'] = len(notas)
    resumo['Maior nota'] = max(notas)
    resumo['Menor nota'] = min(notas)
    media = round(sum(notas)/len(notas), 1)
    resumo['Média total'] = media
    if sit:
        if media > 7:
            resumo['Situação'] = 'BOA'
        elif media > 5:
            resumo['Situação'] = 'RAZOÁVEL'
        else:
            resumo['Situação'] = 'RUIM'
    return resumo


#  Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
resp = notas(3, 9.5, 6, sit=True)
print(resp)
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
