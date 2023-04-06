# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza -> Primeiro = Ana -> Último = Souza

nome_completo = input('Nome Completo: ').upper().split()
nome_separado = nome_completo
print(f'Primeiro = {nome_separado[0]}'
      f'\nSegundo = {nome_separado[-1]}')

# Outras formas de fazer

# 1
nome_completo = input('Nome Completo: ').title().split()
nome_separado = nome_completo
print(f'Primeiro = {nome_separado[0]}'
      f'\nSegundo = {nome_separado[-1]}')

# 2
nome_completo, *nome_separado = input('Nome Completo: ').upper().split()
print(f'Primeiro = {nome_separado[0]}'
      f'\nSegundo = {nome_separado[-1]}')

# 3
nome_completo = input('Nome Completo: ').upper().split()
print(f'Primeiro = {nome_completo[0]}'
      f'\nSegundo = {nome_completo[-1]}')

# 4
# def separar_nome(nome):
    # Separa o nome usando espaços e hífens
#    return re.findall(r'\w+', nome)

# nome_completo = input('Nome Completo: ')
# nome_separado = separar_nome(nome_completo)
# print(f'Primeiro = {nome_separado[0]}'
#      f'\nSegundo = {nome_separado[-1]}')
