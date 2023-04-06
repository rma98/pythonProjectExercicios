# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira.
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

import math

numero = float(input('Digite um número: '))
print(f'O valor digitado foi {numero} e a sua porção inteira é: {math.trunc(numero)}'
      f'\nArredondamento para baixo de {numero} -> floor: {math.floor(numero)}'
      f'\nArredondamento para cima de {numero} -> ceil: {math.ceil(numero)}'
      f'\nNúmero real FLOAT: {numero} -> Número inteiro INT: {int(numero)}')

# Outras formas de fazer

# 1
numero = float(input('Digite um número: '))

print("O valor digitado foi {} e a sua porção inteira é: {}".format(numero, int(numero)))
print("Arredondamento para baixo de {} -> floor: {}".format(numero, math.floor(numero)))
print("Arredondamento para cima de {} -> ceil: {}".format(numero, math.ceil(numero)))
print("Número real FLOAT: {} -> Número inteiro INT: {}".format(numero, int(numero)))
