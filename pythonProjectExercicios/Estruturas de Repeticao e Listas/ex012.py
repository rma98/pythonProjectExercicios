#12. O computador irá "pensar" em número entre 0 e 10. E o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

computador = randint(0, 10) #FAZ O COMPUTADOR "PENSAR"
print('\033[34m-=-\033[m'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('\033[34m-=-\033[m'*20)
jogador = int(input('Em que número eu pensei? ')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print(f'Parabéns você conseguiu me vencer!'
          f'\nO jogador acertou na primeira tentativa.')
else:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
#else:
#    print(f'Ganhei! Eu pensei no número {computador} e não no número {jogador}!')
palpite = 1
while jogador != computador:
    jogador = int(input('Em que número eu pensei? '))  # JOGADOR TENTA ADIVINHAR
    print('PROCESSANDO...')
    sleep(2)
    palpite += 1
    if jogador == computador:
        print('Parabéns você conseguiu me vencer!')
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Foram necessários {palpite} palpites até o jogador conseguir adivinhar.')
