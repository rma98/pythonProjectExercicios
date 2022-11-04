#21. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será guardado
# em um dicionário, incluindo o total de gols feitos durante o campeonato.
# Aprimorando desafio para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

time = list()
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}:')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        res = input('Quer continuar [S/N] ').strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('-=' * 30)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE! >>')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador["gols"]):
#     print(f'   => Na partida {i + 1}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')
