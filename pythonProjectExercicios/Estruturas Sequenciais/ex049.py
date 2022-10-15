# Faça um programa que receba o peso de uma pessoa, calcule e mostre:
# -> o novo peso, se a pessoa engordar 15% sobre o peso digitado.
# -> o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

peso = float(input("Peso: "))
aumento = peso * 15/100
perca = peso * 20/100
print(f"Se engordou: {peso + aumento}kg\nSe emagreceu: {peso - perca}kg")
