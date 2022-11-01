#2. Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol 2017, na ordem
# de colocação. Depois mostre:
# a -> Apenas os 5 primeiros colocados.
# b -> Os últimos 4 colocados da tabela.
# c -> Uma lista com os times em ordem alfabética.
# d -> Em que posição na tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluninense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'\n\033[33m{"=" * 30}\033[m'
      f'\n\033[1;30mTABELA DO BRASILEIRÃO 2017{" " * 4}\033[m'
      f'\n\033[33m{"=" * 30}\033[m')
for pos, time in enumerate(times):
    print(f'{pos + 1} {time}')
print(f'{"=" * 66}'
      f'\n\033[32mOS CINCO PRIMEIROS COLOCADOS\033[m'
      f'\n{times[:5]}'
      f'\n{"=" * 66}'
      f'\n\033[31mOS QUATRO ÚTIMOS COLOCADOS\033[m'
      f'\n{times[16:]}'
      f'\n{"=" * 66}'
      f'\n\033[33mLISTA COM OS TIMES EM ORDEM ALFABÉTICA\033[m'
      f'\n{sorted(times)}'
      f'\n{"=" * 66}'
      f'\n\033[34mPOSIÇÃO NA TABELA EM QUE ESTÁ O TIME DA CHAPECOENSE\033[m'
      f'\nO time da Chapecoense está na {times.index("Chapecoense")+1}º posição.')
