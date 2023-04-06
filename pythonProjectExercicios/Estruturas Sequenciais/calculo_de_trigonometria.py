# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = int(input('Ângulo: '))
print(f'Cosseno: {cos(radians(angulo)):.2f}'
      f'\nSeno: {sin(radians(angulo)):.2f}'
      f'\nTangente: {tan(radians(angulo)):.2f}')

# Outras formas de fazer

# 1
from math import radians, sin, cos, tan

angulo = int(input('Ângulo: '))
angulo_radianos = radians(angulo)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f'Cosseno: {cos(radians(angulo)):.2f}\nSeno: {sin(radians(angulo)):.2f}\nTangente: {tan(radians(angulo)):.2f}')

# 2
from math import radians, sin, cos, tan

angulo = int(input('Ângulo: '))
angulo_radianos = radians(angulo)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

resultados = [('Cosseno', cosseno), ('Seno', seno), ('Tangente', tangente)]

for nome, valor in resultados:
    print(f'{nome}: {valor:.2f}')

# 3
from math import radians, sin, cos, tan

angulo = int(input('Ângulo: '))
angulo_radianos = radians(angulo)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

resultados = {'Cosseno': cosseno, 'Seno': seno, 'Tangente': tangente}

for nome, valor in resultados.items():
    print(f'{nome}: {valor:.2f}')
