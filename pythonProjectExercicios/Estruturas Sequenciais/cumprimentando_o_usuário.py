# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Seu nome: ')
print(f'Olá {nome}! Prazer em te conhecer!')

# Outras formas de fazer

# 1
nome = input('Seu nome: ')
mensagem = 'Olá {}! Prazer em te conhecer!'.format(nome)
print(mensagem)

# 2
nome = input('Seu nome: ')
mensagem = 'Olá ' + nome + '! Prazer em te conhecer!'
print(mensagem)

# 3
nome = input('Seu nome: ')
mensagem = 'Olá %s! Prazer em te conhecer!' % nome
print(mensagem)
