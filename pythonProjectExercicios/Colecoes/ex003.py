#3. Crie um programa que vai gerar cinco números aleatórios e cololar em uma tupla. Depois disso, mostre a listagem dos
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros_aleatorios = ((randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)))
print(f'Os valores sorteados foram: ', end="")
for numeros in numeros_aleatorios:
    print(f'{numeros} ', end="")
print(f'\nO maior valor digitado foi {max(numeros_aleatorios)}'
      f'\nO menor valor digitado foi {min(numeros_aleatorios)}')
