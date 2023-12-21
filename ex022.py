nome = input('Insira seu nome completo: ').strip()

print(f'Nome em letras maiúsculas: {nome.upper()}')
print(f'Nome em letras minúsculas: {nome.lower()}')
print(f'Total de letras (sem contar espaço): {len("".join(nome.strip().split()))}')
print(f'Total de letras primeiro nome: {len(nome.split()[0])}')
