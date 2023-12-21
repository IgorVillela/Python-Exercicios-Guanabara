def escreva(texto):
    comprimento = len(texto) + 4
    print('~' * comprimento)
    print(texto.center(comprimento))
    print('~' * comprimento)


escreva('Olá, mundo')
escreva('Curso de Python no YouTube')
escreva('CeV')
