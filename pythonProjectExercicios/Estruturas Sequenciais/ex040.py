#40. Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para
# a primeira e peso 3 para a segunda.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media_Ponderada = (n1 * 2 + n2 * 3) / (2 + 3)
print(f"Média Ponderada: {media_Ponderada:.1f}")
