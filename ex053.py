frase = input('Insira uma frase sem acentos: ').strip().upper()
palavras = frase.split()
join = ''.join(palavras)

if join == join[::-1]:
    print('\033[32m')
    print(f'O inverso da frase {join} é {join[::-1]}, portanto é um palíndromo!')
else:
    print('\033[31m')
    print(f'O inverso da frase {join} é {join[::-1]}, portanto não é um palíndromo...')
