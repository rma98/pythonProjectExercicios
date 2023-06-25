# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite o valor: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[33m', end=" ")
        tot += 1
    else:
        print(f'\033[31m', end=" ")
    print(f'{c}', end=" ")
print(f'\n\033[0mO número {numero} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print(f'E por isso ele não é PRIMO!')

# Outras formas de fazer

# 1
is_primo = True
for c in range(2, int(numero**0.5) + 1):
    if numero % c == 0:
        is_primo = False
        break

if numero <= 1:
    is_primo = False

if is_primo:
    print('O número é PRIMO!')
else:
    print('O número não é PRIMO!')

# 2
is_primo = all(numero % c != 0 for c in range(2, numero))
if numero <= 1:
    is_primo = False

if is_primo:
    print('O número é PRIMO!')
else:
    print('O número não é PRIMO!')
