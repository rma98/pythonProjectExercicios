# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira.
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

import math

numero = float(input('Digite um número: '))
print(f'O valor digitado foi {numero} e a sua porção inteira é: {math.trunc(numero)}'
      f'\nArredondamento para baixo de {numero} -> floor: {math.floor(numero)}'
      f'\nArredondamento para cima de {numero} -> ceil: {math.ceil(numero)}'
      f'\nNúmero real FLOAT: {numero} -> Número inteiro INT: {int(numero)}')
