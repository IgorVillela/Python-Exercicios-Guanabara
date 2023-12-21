cores = {'Verde': '\033[32m',
         'Vermelho': '\033[31m',
         'Vermelho Destaque': '\033[30;41m',
         'Amarelo': '\033[1;33m',
         'Titulo': '\033[1;30;44m',
         'Limpa': '\033[m'}

print(f"{cores['Amarelo']}-=-{cores['Limpa']}" * 6)
print(f"{cores['Titulo']}ANALISADOR IMC{cores['Limpa']}".center(31, '='))
print(f"{cores['Amarelo']}-=-{cores['Limpa']}" * 6)

peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em m? '))
imc = peso/altura**2

print(f'Seu IMC deu {imc:.1f}')
if imc < 18.5:
    print(f"{cores['Vermelho']}Abaixo do peso")
elif imc < 25:
    print(f"{cores['Verde']}Peso ideal!")
elif imc < 30:
    print(f"{cores['Amarelo']}Sobrepeso")
elif imc <= 40:
    print(f"{cores['Vermelho']}Obesidade")
else:
    print(f"{cores['Vermelho Destaque']}Obesidade mórbida{cores['Limpa']}")
