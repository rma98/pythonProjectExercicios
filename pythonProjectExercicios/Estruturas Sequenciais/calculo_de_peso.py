# Faça um programa que receba o peso de uma pessoa, calcule e mostre:
# -> o novo peso, se a pessoa engordar 15% sobre o peso digitado.
# -> o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

peso = float(input("Peso: "))
aumento = peso * 15/100
perca = peso * 20/100
print(f"Se engordou: {peso + aumento}kg\nSe emagreceu: {peso - perca}kg")

# Outras formas de fazer

# 1
peso = float(input("Peso: "))
aumento = perca = peso * 0.15
print(f"Se engordou: {peso + aumento:.2f}kg\nSe emagreceu: {peso - perca:.2f}kg")

# 2
peso = float(input("Peso: "))
aumento = peso * 0.15
perda = peso * 0.20
print(f"Se engordou: {peso + aumento:.2f}kg\nSe emagreceu: {peso - perda:.2f}kg")

# 3
peso = float(input("Peso: "))
aumento = peso * 0.15
perda = peso * 0.20
peso_engordou = peso + aumento
peso_emagreceu = peso - perda
print(f"Se engordou: {peso_engordou:.2f}kg\nSe emagreceu: {peso_emagreceu:.2f}kg")

# 4
peso = float(input("Peso: "))
aumento = round(peso * 0.15, 2)
perda = round(peso * 0.20, 2)
print(f"Se engordou: {round(peso + aumento, 2)}kg\nSe emagreceu: {round(peso - perda, 2)}kg")
