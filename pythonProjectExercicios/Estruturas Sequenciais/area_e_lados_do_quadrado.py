# Faça um programa que defina uma variável com área de um quadrado no valor de 256 e calcule o valor de cada lado do
# quadrado.

import math

area_Do_Quadrado = 256
print(f"Área do quadrado: {area_Do_Quadrado}\nValor de cada lado do quadrado: {math.sqrt(area_Do_Quadrado):.0f}"
      f"\nLado A 16 x 16 Lado B = {16 * 16}")

# Outras formas de fazer

# 1
import math

area_do_quadrado = 256
lado_do_quadrado = math.sqrt(area_do_quadrado)
lado_a = 16
lado_b = 16

print(f"Área do quadrado: {area_do_quadrado}\nValor de cada lado do quadrado: {lado_do_quadrado:.0f}"
      f"\nLado A {lado_a} x {lado_b} Lado B = {lado_a * lado_b}")

# 2
lado_do_quadrado = math.sqrt(256)
area_do_quadrado = lado_do_quadrado ** 2
lado_a = 16
lado_b = 16

print(f"Área do quadrado: {area_do_quadrado}\nValor de cada lado do quadrado: {lado_do_quadrado:.0f}"
      f"\nLado A {lado_a} x {lado_b} Lado B = {lado_a * lado_b}")

# 3
area_do_quadrado = 256
lado_do_quadrado = area_do_quadrado ** 0.5
lado_a = 16
lado_b = 16

print(f"Área do quadrado: {area_do_quadrado}\nValor de cada lado do quadrado: {lado_do_quadrado:.0f}"
      f"\nLado A {lado_a} x {lado_b} Lado B = {lado_a * lado_b}")

# 4
area_do_quadrado = 256
lado_do_quadrado = area_do_quadrado // 4
lado_a = 16
lado_b = 16

print(f"Área do quadrado: {area_do_quadrado}\nValor de cada lado do quadrado: {lado_do_quadrado}"
      f"\nLado A {lado_a} x {lado_b} Lado B = {lado_a * lado_b}")
