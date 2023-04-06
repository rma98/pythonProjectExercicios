# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas as letras minúsculas
# -> Quantas letras ao todo sem considerar os espaços
# -> Quantas letras tem o primeiro nome

nome_completo = input('Nome Completo: ').strip()
primeiro_nome = nome_completo.split()
print(f'Analisando seu nome...'
      f'\nSeu nome em maiúsculas é: {nome_completo.upper()}'
      f'\nSeu nome em minúsculas é: {nome_completo.lower()}'
      f'\nSeu nome tem ao todo {len(nome_completo) - nome_completo.count(" ")} letras: '
      f'\nSeu primeiro nome é: {primeiro_nome[0]} e ao todo contém {len(primeiro_nome[0])} letras')

# Outras formas de fazer

# 1
nome_completo = input('Nome Completo: ').replace('  ', ' ').strip()

# 2
nome_completo = input('Nome Completo: ').strip()
primeiro_nome = nome_completo.split()[0].capitalize()

# 3
nome_completo = input('Nome Completo: ').strip()
letras_nome = len(nome_completo.replace(' ', ''))
primeiro_nome, *sobrenomes = nome_completo.split()
letras_primeiro_nome = len(primeiro_nome)
print(f"Seu nome tem ao todo {letras_nome} letras.")
print(f"Seu primeiro nome é {primeiro_nome} e tem {letras_primeiro_nome} letras.")
