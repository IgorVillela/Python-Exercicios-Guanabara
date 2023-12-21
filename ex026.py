frase = input('Escreva uma frase: ').strip().upper()

print(f'Quantidades de letras "A": {frase.count("A")}')
print(f'Posição da primeira letra "A": {frase.find("A")+1}')
print(f'Posição da última letra "A": {frase.rfind("A")+1}')
