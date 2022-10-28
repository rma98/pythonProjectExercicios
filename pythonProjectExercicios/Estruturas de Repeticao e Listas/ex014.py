#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5!=5x4x3x2x1=120

#Utilizando a estrutura de repetição WHILE
n = int(input('Número: '))
c = n
f = 1
print(f'{"=" * 25}'
        f'\n\033[34mFATORIAL DE {n}!\033[m'
        f'\n{"=" * 25}')
while c > 0:
    print(f'{c} ', end="")
    print('X ' if c > 1 else '= ', end="")
    f *= c
    c -= 1
print(f'{f}')

#Utilizando a estrutura de repetição FOR
numero = int(input("\nDigite um número: "))
if numero > 0:
  fatorial = 1
  for item in range(1, numero+1):
    fatorial *= item
  print(f'{"=" * 25} '
        f'\n\033[34mFATORIAL DE {numero}! = {fatorial}\033[m'
        f'\n{"=" * 25}')

from math import factorial
#Utilizabdo MÓDULO
num = int(input('Número: '))
fat = factorial(num)
print(f'{"=" * 25} '
        f'\n\033[34mFATORIAL DE {num}! = {fat}\033[m'
        f'\n{"=" * 25}')
