# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas as letras minúsculas
# -> Quantas letrass ao todo sem considerar os epaços
# -> Quantas letras tem o primeiro nome

nome_completo = input('Nome Completo: ').strip()
primeiro_nome = nome_completo.split()
print(f'Analisando seu nome...'
      f'\nSeu nome em maiúsculas é: {nome_completo.upper()}'
      f'\nSeu nome em minúsculas é: {nome_completo.lower()}'
      f'\nSeu nome tem ao todo {len(nome_completo) - nome_completo.count(" ")} letras: '
      f'\nSeu primeiro nome é: {primeiro_nome[0]} e ao todo contém {len(primeiro_nome[0])} letras')
