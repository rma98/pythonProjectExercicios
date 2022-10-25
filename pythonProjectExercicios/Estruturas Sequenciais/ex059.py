# Um professor quer sortear um dos seus quatros aLunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.

from random import choice, randint

aluno_1 = input('Nome do primeiro aluno: ')
aluno_2 = input('Nome do segundo aluno: ')
aluno_3 = input('Nome do terceiro aluno: ')
aluno_4 = input('Nome do quarto aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista_alunos)
print(f'O aluno escolhido foi: {escolhido}')

'''
aleatorio = randint(1, 4)
if aleatorio == 1:
    print(f'O aluno escolhido foi: {aluno_1}')
elif aleatorio == 2:
    print(f'O aluno escolhido foi: {aluno_2}')
elif aleatorio == 3:
    print(f'O aluno escolhido foi: {aluno_3}')
elif aleatorio == 4:
    print(f'O aluno escolhido foi: {aluno_4}')
'''
