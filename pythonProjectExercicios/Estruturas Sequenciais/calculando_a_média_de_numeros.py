# Calcular a média de 4 números digitados pelo usuário

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
num4 = float(input("Número 4: "))
print(f"Média: {(num1 + num2 + num3 + num4) / 4:.1f}")

# Outras formas de fazer

# 1
numeros = []
for i in range(4):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
media = sum(numeros) / len(numeros)
print(f"A média é: {media:.1f}")

# 2
def media_quatro_numeros():
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    num3 = float(input("Número 3: "))
    num4 = float(input("Número 4: "))
    media = (num1 + num2 + num3 + num4) / 4
    print(f"Média: {media:.1f}")

media_quatro_numeros()

# 3
from functools import reduce

numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(4)]
media = reduce(lambda x, y: x + y, numeros) / len(numeros)
print(f"A média é: {media:.1f}")
