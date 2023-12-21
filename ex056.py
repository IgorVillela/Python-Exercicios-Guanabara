lista_nome = []
lista_idade = []
# homem_mais_velho = ''
# idade_homem_velho = 0
lista_sexo = []
contagem_mulheres_jovens = 0

for i in range(4):
    print('-' * 10)
    print(f'{i+1}ª pessoa')
    print('-' * 10)
    nome = input('Insira o nome: ').strip()
    lista_nome.append(nome)
    idade = int(input('Insira a idade: '))
    lista_idade.append(idade)
    sexo = input('Insira o sexo (M/F): ').upper().strip()
    lista_sexo.append(sexo)
    if sexo == 'F' and idade < 20:
        contagem_mulheres_jovens += 1
    # if idade > idade_homem_velho and sexo == 'M':
    #     idade_homem_velho = idade
    #     homem_mais_velho = nome

indice_homem_velho = max((idade, i) for i, idade in enumerate(lista_idade) if lista_sexo[i] == 'M')[1]

homem_mais_velho = lista_nome[indice_homem_velho]

print(f'A média de idade do grupo é: {sum(lista_idade) / len(lista_idade)} anos')
print(f'O nome do homem mais velho de {lista_idade[indice_homem_velho]} anos é: {homem_mais_velho}')
print(f'A quantidade de mulheres com menos de 20 anos é: {contagem_mulheres_jovens}')
