# Faça um programa que recebe o peso de uma pesa em quilos, calcule e mostre esse peso em gramas.

peso = int(input("Peso: "))
print(f"{peso}kg convertido em gramas é: {peso * 1000}g")

# Outras formas de fazer

# 1
kg_to_g = 1000
peso = int(input("Peso: "))
print(f"{peso}kg convertido em gramas é: {peso * kg_to_g}g")

# 2
peso = float(input("Peso: "))
gramas = peso * 1000
print(f"{peso}kg convertido em gramas é: {round(gramas, 2)}g")

# 3
peso = int(input("Peso: "))
gramas = peso // 0.001
print(f"{peso}kg convertido em gramas é: {gramas}g")

# 4
# import numpy as np
# peso = int(input("Peso: "))
# gramas = np.multiply(peso, 1000)
# print(f"{peso}kg convertido em gramas é: {gramas}g")
