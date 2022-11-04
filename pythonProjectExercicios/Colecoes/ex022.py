#22. crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# a -> Quantas pessoas foram cadastradas.
# b -> A média de idade do grupo.
# c -> Uma lista com todas as mulheres.
# d -> Uma lista com todas as pessoas com idade acima da média.

from datetime import datetime

galera = []
pessoa = {}
soma = media = 0
atual = datetime.now().year
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo: [M/F]\n').upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas \"M\" ou \"F\".')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        res = input('Deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: \n').strip().upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas \"S\" ou \"N\".')
    if res == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'[{p["Nome"]}]', end=' ')
print()
print(f'Lista da pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
