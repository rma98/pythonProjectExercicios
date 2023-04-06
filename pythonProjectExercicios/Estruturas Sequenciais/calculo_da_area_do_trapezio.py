# Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: Área = ((base maior + base menor) * altura) / 2.

base_Maior = int(input("Base Maior: "))
base_Menor = int(input("Base Menor: "))
altura = int(input("Altura: "))
print(f"A área do trapézio é: {((base_Maior + base_Menor) * altura) / 2}")

# Outras formas de fazer

# 1
base_maior = int(input("Base maior: "))
base_menor = int(input("Base menor: "))
altura = int(input("Altura: "))

area = (base_maior + base_menor) * altura / 2

print(f"A área do trapézio é: {area}")

# 2
def area_trapezio(base_maior, base_menor, altura):
    return (base_maior + base_menor) * altura / 2

base_maior = int(input("Base maior: "))
base_menor = int(input("Base menor: "))
altura = int(input("Altura: "))

area = area_trapezio(base_maior, base_menor, altura)

print(f"A área do trapézio é: {area}")

# 3
base_maior, base_menor, altura = map(int, input("Entre com a base maior, base menor e altura, separados por espaços: ").split())

print(f"A área do trapézio é: {((base_maior + base_menor) * altura) / 2}")
