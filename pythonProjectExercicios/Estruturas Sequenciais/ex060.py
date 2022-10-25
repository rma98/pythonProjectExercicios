# O mesmo professor do desafio anterior quer sortear a ordem da apresentação dos trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno_1 = input('Nome do primeiro aluno: ')
aluno_2 = input('Nome do segundo aluno: ')
aluno_3 = input('Nome do terceiro aluno: ')
aluno_4 = input('Nome do quarto aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_alunos)
print(f'A ordem de apresentação será: {lista_alunos}')
print('='*12)
for alunos in lista_alunos:
    print(f'{alunos}')
print('='*12)
