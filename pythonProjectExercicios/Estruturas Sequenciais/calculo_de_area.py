# Faça um programa que calcule e mostre a área de um losango. Sabe-se que: Área = (diagonal maior * diagonal menor) / 2.

diagonal_Maior = int(input("Diagonal Maior: "))
diagonal_Menor = int(input("Diagonal Menor: "))
area = (diagonal_Maior * diagonal_Menor) / 2
print(f"Área do losango: {area}")

# Outras formas de fazer

# 1
diagonal_maior = int(input("Diagonal Maior: "))
diagonal_menor = int(input("Diagonal Menor: "))
lado = (diagonal_maior ** 2 + diagonal_menor ** 2) ** 0.5 / 2
area = diagonal_maior * diagonal_menor / 2
print(f"Área do losango: {area}")

# 2
def calcular_area(diagonal_maior, diagonal_menor):
    return diagonal_maior * diagonal_menor / 2

diagonal_maior = int(input("Diagonal Maior: "))
diagonal_menor = int(input("Diagonal Menor: "))
area = calcular_area(diagonal_maior, diagonal_menor)
print(f"Área do losango: {area}")

# 3
diagonais = [int(input(f"Diagonal {i}: ")) for i in ["Maior", "Menor"]]
area = diagonais[0] * diagonais[1] / 2
print(f"Área do losango: {area}")
