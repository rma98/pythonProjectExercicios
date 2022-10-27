#1. Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artíficio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('\033[7;37;40mCONTAGEM REGRESSIVA\033[m')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[31mBUM BUM POOW!!!\033[m')
