#17. Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contando a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    res = input('Deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO:').strip().upper()[0]
    while res not in 'SN':
        res = input('Deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO:').strip().upper()[0]
    if res == 'N':
        break
print(f'{"-=" * 30}'
      f'\n{"No.":<4}{"NOME":<10}{"MÉDIA":>8}'
      f'\n{"-=" * 36}')
for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print(f'{"-=" * 35}')
    opcao = int(input('Mostrar notas de quais alunos? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(boletim) - 1:
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}')
print('<<<< VOLTE SEMPRE! <<<<')
