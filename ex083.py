exp = input('Digite uma expressão: ')
lista = []

# if exp.count('(') == exp.count(')') or '(' and ')' not in exp:
#     print('A expressão é válida!')
# else:
#     print('A expressão é inválida...')

for letra in exp:
    if letra == '(' or letra == ')':
        lista.append(letra)

if lista.count('(') == lista.count(')') or not lista:
    print('A expressão é válida!')
else:
    print('A expressão é inválida...')
