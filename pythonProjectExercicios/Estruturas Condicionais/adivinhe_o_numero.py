# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

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

# Outras formas de fazer

# 1
from random import randint
import time

computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

while True:
    jogador = int(input('Em que número eu pensei? '))
    if jogador == computador:
        print('Parabéns! Você acertou!')
        break
    else:
        print('Ops! Tente novamente...')
        time.sleep(1)

# 2
from random import randint
import time

def adivinhar_numero():
    computador = randint(0, 5)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    time.sleep(2)

    if jogador == computador:
        print('Parabéns! Você acertou!')
    else:
        print(f'Você errou! O número que eu pensei foi {computador}.')
    
adivinhar_numero()

# 3
import random

numeros = [0, 1, 2, 3, 4, 5]
computador = random.choice(numeros)

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))

if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! O número que eu pensei foi {computador}.')
