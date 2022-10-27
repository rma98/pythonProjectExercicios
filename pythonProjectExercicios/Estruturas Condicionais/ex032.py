#32. Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print(f'O computador escolheu {itens[computador]}')
jogador = int(input('\033[7;37;40mSuas opções:\033[m\n\033[33m0-> PEDRA\033[m\n\033[32m1-> PAPEL\033[m\n\033[34m2-> TESOURA\033[m'
                    '\n\033[36mQual é a sua jogada?\033[m '))
print(f'JO')
sleep(1)
print(f'KEN')
sleep(1)
print(f'PÔ!!')
sleep(1)
print('=' * 25)
print(f'Computador jogou {itens[computador]}\n'
      f'Jogador jogou {itens[jogador]}')
print('=' * 25)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VEMCE')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
