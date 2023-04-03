# Calcular a área do círculo de raio informado pelo usuário.

raio = int(input("Raio: "))
pi = 3.14
print(f"Área do circulo: {pi * raio * raio:.2f}")

# Outras formas de fazer

# 1
import math

raio = float(input("Raio: "))
area = math.pi * raio ** 2

print(f"Área do círculo: {area:.2f}")

# 2
raio = float(input("Raio: "))
area = 3.14 * pow(raio, 2)

print(f"Área do círculo: {area:.2f}")

# 3
def calcular_area(raio):
    return 3.14 * raio ** 2

raio = float(input("Raio: "))
area = calcular_area(raio)

print(f"Área do círculo: {area:.2f}")
