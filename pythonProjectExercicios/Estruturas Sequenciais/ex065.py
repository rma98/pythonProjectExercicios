# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza -> Primeiro = Ana -> Último = Souza

nome_completo = input('Nome Completo: ').upper().split()
nome_separado = nome_completo
print(f'Primeiro = {nome_separado[0]}'
      f'\nSegundo = {nome_separado[-1]}')
