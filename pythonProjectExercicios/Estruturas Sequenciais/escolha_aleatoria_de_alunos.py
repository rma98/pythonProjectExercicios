# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.

from random import randint

aluno_1 = input('Nome do primeiro aluno: ')
aluno_2 = input('Nome do segundo aluno: ')
aluno_3 = input('Nome do terceiro aluno: ')
aluno_4 = input('Nome do quarto aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

aleatorio = randint(1, 4)
if aleatorio == 1:
    print(f'O aluno escolhido foi: {aluno_1}')
elif aleatorio == 2:
    print(f'O aluno escolhido foi: {aluno_2}')
elif aleatorio == 3:
    print(f'O aluno escolhido foi: {aluno_3}')
elif aleatorio == 4:
    print(f'O aluno escolhido foi: {aluno_4}')

# Outras formas de fazer

# 1
from random import choice

lista_alunos = ['aluno_1', 'aluno_2', 'aluno_3', 'aluno_4']
aluno_escolhido = choice(lista_alunos)

print(f'O aluno escolhido foi: {aluno_escolhido}')

# 2
from random import sample

lista_alunos = ['aluno_1', 'aluno_2', 'aluno_3', 'aluno_4']
aluno_escolhido = sample(lista_alunos, 1)[0]

print(f'O aluno escolhido foi: {aluno_escolhido}')

# 3
# import numpy as np

# lista_alunos = ['aluno_1', 'aluno_2', 'aluno_3', 'aluno_4']
# aluno_escolhido = np.random.choice(lista_alunos)

# print(f'O aluno escolhido foi: {aluno_escolhido}')
