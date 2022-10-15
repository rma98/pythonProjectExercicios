#44. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: Área = ((base maior + base menor) * altura) / 2

base_Maior = int(input("Base Maior: "))
base_Menor = int(input("Base Menor: "))
altura = int(input("Altura: "))
print(f"A área do trapézio é: {((base_Maior + base_Menor) * altura) / 2}")
