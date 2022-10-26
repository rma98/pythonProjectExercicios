#20. Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá esvrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5) #FAZ O COMPUTADOR "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no número {jogador}!')
