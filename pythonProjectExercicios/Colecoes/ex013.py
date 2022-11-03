#13. Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a -> Quantas pessoas foram cadastradas.
# b -> Uma listagem com as pessoas mais pesadas.
# c -> Uma listagem com as pessoas mais leves.

dados = []
galera = []
tot = mai_peso = men_peso = 0
res = ''
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai_peso = men_peso = dados[1]
    else:
        if dados[1] > mai_peso:
            mai_peso = dados[1]
        if dados[1] < men_peso:
            men_peso = dados[1]
    galera.append(dados[:])
    dados.clear()
    tot += 1
    res = input('Deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    while res not in 'SN':
        res = input('Deseja continuar? Aperte \"S\" para SIM ou \"N\ para NÃO: ').strip().upper()[0]
    if res == 'N':
        break
print(f'{"=-" * 30}'
      f'\nO total de pessoas cadastradas foram {tot}')
print(f'O maior peso foi de {mai_peso}kg. Peso de', end=' ')
for pessoa in galera:
    if pessoa[1] == mai_peso:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO menor peso foi de {men_peso}kg.', end=' ')
for pessoa in galera:
    if pessoa[1] == men_peso:
        print(f'[{pessoa[0]}]', end=' ')
