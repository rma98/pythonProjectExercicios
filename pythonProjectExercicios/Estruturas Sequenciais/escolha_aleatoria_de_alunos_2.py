# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.

from random import choice, randint

aluno_1 = input('Nome do primeiro aluno: ')
aluno_2 = input('Nome do segundo aluno: ')
aluno_3 = input('Nome do terceiro aluno: ')
aluno_4 = input('Nome do quarto aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista_alunos)
print(f'O aluno escolhido foi: {escolhido}')

# Outras formas de fazer

# 1
import random

alunos = []
for i in range(4):
    nome = input(f'Digite o nome do aluno {i+1}: ')
    alunos.append(nome)

escolhido = random.choice(alunos)
print(f'O aluno escolhido foi: {escolhido}')

# 2
from random import randint

aluno_1 = input('Nome do primeiro aluno: ')
aluno_2 = input('Nome do segundo aluno: ')
aluno_3 = input('Nome do terceiro aluno: ')
aluno_4 = input('Nome do quarto aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = lista_alunos[randint(0, len(lista_alunos)-1)]
print(f'O aluno escolhido foi: {escolhido}')
