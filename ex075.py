cont = 0
tupla = ()
index = ""
tupla_pares = ()

while cont < 4:
    try:
        n = int(input('Digite um valor: '))
    except ValueError:
        continue
    cont += 1
    tupla += (n,)
    if n % 2 == 0:
        tupla_pares += (n,)
    if 3 in tupla:
        index = tupla.index(3)

print(f'{" RESUMO ":-^40}')
print(tupla)
print(f'Vezes que o número 9 foi digitado: {tupla.count(9)}\n'
      f'Posição do primeiro número 3: {f"{index + 1}ª posição" if index != "" else "N/A"}')
if tupla_pares:
    print('Os números pares são: ', end='')
    for i in tupla_pares:
        print(i, end=' ')
else:
    print('Números pares: N/A')
