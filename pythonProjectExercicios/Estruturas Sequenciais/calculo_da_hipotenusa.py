# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.

from math import hypot

print('='*12, 'ATRAVÉS DE IMPORTAÇÃO', '='*12)
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
print(f'Comrpimento da hipotenusa: {hypot(cateto_oposto, cateto_adjacente):.2f}')

print('='*12, 'FÓRMULA MATEMÁTICA', '='*12)
print(f'A hipotenusa vai medir: {(cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2):.2f}')

# Outras formas de fazer

# 1
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5
print(f'Comrpimento da hipotenusa: {hipotenusa:.2f}')

# 2
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = pow(cateto_oposto ** 2 + cateto_adjacente ** 2, 0.5)
print(f'Comrpimento da hipotenusa: {hipotenusa:.2f}')

# 3
import math
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
print(f'Comrpimento da hipotenusa: {hipotenusa:.2f}')
