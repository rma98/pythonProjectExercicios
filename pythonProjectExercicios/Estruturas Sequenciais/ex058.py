# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = int(input('Ângulo: '))
print(f'Cosseno: {cos(radians(angulo)):.2f}'
      f'\nSeno: {sin(radians(angulo)):.2f}'
      f'\nTangente: {tan(radians(angulo)):.2f}')
