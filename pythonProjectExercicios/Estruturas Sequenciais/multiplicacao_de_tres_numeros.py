# Faça um programa que recebe três números, calcule e mostre a multiplicação desses números.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
print(f"{n1} x {n2} x {n3} = {n1 * n2 * n3}")

# 1
numeros = []
for i in range(3):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
resultado = numeros[0] * numeros[1] * numeros[2]
print(f"{numeros[0]} x {numeros[1]} x {numeros[2]} = {resultado}")

# 2
def produto_numeros(n1, n2, n3):
    return n1 * n2 * n3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

resultado = produto_numeros(num1, num2, num3)

print(f"{num1} x {num2} x {num3} = {resultado}")

# 3
from functools import reduce

numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(3)]
resultado = reduce(lambda x, y: x * y, numeros)
print(f"{numeros[0]} x {numeros[1]} x {numeros[2]} = {resultado}")
