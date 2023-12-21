tupla_palavras = (
    "Esta", "e", "uma", "tupla", "de", "exemplo", "contendo", "mais", "de", "50",
    "palavras", "Cada", "elemento", "desta", "tupla", "contribui", "para", "a", "contagem", "desejada",
    "As", "tuplas", "sao", "estruturas", "de", "dados", "imutaveis", "em", "Python", "Elas", "sao",
    "definidas", "usando", "parenteses", "e", "podem", "conter", "diferentes", "tipos", "de", "dados",
    "Neste", "caso", "as", "palavras", "sao", "strings", "formando", "uma", "descricao", "simples"
)

contagem = 0

for i in tupla_palavras:
    print(f'A palavra "{i}" contém ', end='')
    if 'a' or 'e' or 'i' or 'o' or 'u' in i.lower():
        cont_a = i.lower().count('a')
        cont_e = i.lower().count('e')
        cont_i = i.lower().count('i')
        cont_o = i.lower().count('o')
        cont_u = i.lower().count('u')
        total = cont_a + cont_e + cont_i + cont_o + cont_u
        print(f'{total} vogais. ', end='')
        if cont_a != 0:
            print(f'"a": {cont_a} ', end='')
        if cont_e != 0:
            print(f'"e": {cont_e} ', end='')
        if cont_i != 0:
            print(f'"i": {cont_i} ', end='')
        if cont_o != 0:
            print(f'"o": {cont_o} ', end='')
        if cont_u != 0:
            print(f'"u": {cont_u} ', end='')
        print('')
        print('Vogais: ', end='')
        for letra in i:
            if letra.lower() in 'aeiou':
                print(letra.lower(), end=' ')
        print('')
    else:
        print(f'0 vogais.')
