# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('\033[7;37;40mCONTAGEM REGRESSIVA\033[m')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[31mBUM BUM POOW!!!\033[m')

# Outras formas de fazer

# 1
def countdown(n):
    if n == 0:
        print('BUM BUM POOW!!!')
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

print('\033[7;37;40mCONTAGEM REGRESSIVA\033[m')
countdown(10)

# 2
import time

print('\033[7;37;40mCONTAGEM REGRESSIVA\033[m')
countdown = list(range(10, 0, -1))
countdown.append('BUM BUM POOW!!!')

for item in countdown:
    if isinstance(item, int):
        print(item)
        time.sleep(1)
    else:
        print('\033[31m%s\033[m' % item)

# 3
import time

def countdown(n):
    while n > 0:
        yield n
        time.sleep(1)
        n -= 1
    yield 'BUM BUM POOW!!!'

print('\033[7;37;40mCONTAGEM REGRESSIVA\033[m')
for item in countdown(10):
    if isinstance(item, int):
        print(item)
    else:
        print('\033[31m%s\033[m' % item)
