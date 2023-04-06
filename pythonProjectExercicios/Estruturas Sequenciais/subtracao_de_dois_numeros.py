# Faça um programa que receba dois números, calcule e mostre a subtração do primeiro pelo segundo.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print(f"{n1} - {n2} = {n1 - n2}")

# Outras formas de fazer

# 1
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
subtracao = n1 - n2
print(f"{n1} - {n2} = {subtracao}")

# 2
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
subtracao = n1 - n2
print("{} - {} = {}".format(n1, n2, subtracao))

# 3
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print("{} - {} = {}".format(n1, n2, n1 - n2))

# 4
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print(n1, "-", n2, "=", n1 - n2)
