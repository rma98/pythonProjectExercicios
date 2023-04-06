# Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para
# a primeira e peso 3 para a segunda.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media_Ponderada = (n1 * 2 + n2 * 3) / (2 + 3)
print(f"Média Ponderada: {media_Ponderada:.1f}")

# Outras formas de fazer

# 1
notas = []
pesos = []
notas.append(float(input("Digite a primeira nota: ")))
notas.append(float(input("Digite a segunda nota: ")))
pesos.append(2)
pesos.append(3)
media_pond = sum([nota*peso for nota, peso in zip(notas, pesos)]) / sum(pesos)
print(f"Média ponderada: {media_pond:.1f}")

# 2
n1, n2 = map(float, input("Digite as duas notas: ").split())
media_pond = (n1*2 + n2*3) / 5
print(f"Média ponderada: {media_pond:.1f}")

# 3
def media_ponderada(n1, n2):
    return (n1*2 + n2*3) / 5

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media_pond = media_ponderada(n1, n2)
print(f"Média ponderada: {media_pond:.1f}")
