# Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo.
# Sabe-se que a soma dos ângulos de um triângulo é 180 graus.

angulo1 = int(input("Ângulo 1: "))
angulo2 = int(input("Ângulo 2: "))
print(f"Ângulo 3: {angulo1 + angulo2 - 180}")
