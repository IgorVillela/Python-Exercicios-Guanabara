entrada = input('Digito: ')
print('Esse valor é do tipo primitivo: ', type(entrada))
print('Só tem espaço? ', entrada.isspace())
print('É um número? ', entrada.isnumeric())
print('É um alfanumerico? ', entrada.isalnum())
print('É alfabético? ', entrada.isalpha())
print('Só tem letras maiúsculas? ', entrada.isupper())
print('Só tem letras minúsculas? ', entrada.islower())
print('Está capitalizada? ', entrada.istitle())
