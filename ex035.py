cores = {'Verde': '\033[32m',
         'Vermelho': '\033[31m',
         'Amarelo': '\033[1;33m',
         'Titulo': '\033[1;30;44m',
         'Limpa': '\033[m'}

print(f"{cores['Amarelo']}-=-{cores['Limpa']}" * 8)
print(f"{cores['Titulo']}ANALISADOR DE TRIÂNGULOS{cores['Limpa']}")
print(f"{cores['Amarelo']}-=-{cores['Limpa']}" * 8)

a = float(input('Linha 1 em cm: '))
b = float(input('Linha 2 em cm: '))
c = float(input('Linha 3 em cm: '))

if b + c > a and a + c > b and a + b > c:
    print(f"{cores['Verde']}As retas {a:.2f} cm, {b:.2f} cm e {c:.2f} cm,"
          f" conseguem formar um triângulo!{cores['Limpa']}")
else:
    print(f"{cores['Vermelho']}Não é possível formar um triângulo com as retas fornecidas...{cores['Limpa']}")
