# Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo.
# Sabe-se que a soma dos ângulos de um triângulo é 180 graus.

angulo1 = int(input("Ângulo 1: "))
angulo2 = int(input("Ângulo 2: "))
print(f"Ângulo 3: {angulo1 + angulo2 - 180}")

# Outras formas de fazer

# 1
angulo1 = int(input("Ângulo 1: "))
angulo2 = int(input("Ângulo 2: "))
soma_angulos = angulo1 + angulo2
angulo3 = 180 - soma_angulos
print(f"Ângulo 3: {angulo3}")

# 2
def calcular_terceiro_angulo(angulo1, angulo2):
    return 180 - (angulo1 + angulo2)

angulo1 = int(input("Ângulo 1: "))
angulo2 = int(input("Ângulo 2: "))
angulo3 = calcular_terceiro_angulo(angulo1, angulo2)
print(f"Ângulo 3: {angulo3}")
