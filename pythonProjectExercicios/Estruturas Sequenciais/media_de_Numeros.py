# Calcular a média de 4 números digitados pelo usuário e imprimir se ele é par e positivo.

num1 = float(input("Número 1:"))
num2 = float(input("Número 2:"))
num3 = float(input("Número 3:"))
num4 = float(input("Número 4:"))
media = (num1 + num2 + num3 + num4) / 4
if media % 2 == 0 and media >= -1:
    print(True)
else:
    print(False)
print(media)

# Outras formas de fazer

# 1
if media % 2 == 0:
    if media >= -1:
        print(True)
else:
    print(False)

# 3
print(media % 2 == 0 and media >= -1)

# 4
if media % 2 == 0 and media >= -1:
    print("A média é par e maior ou igual a -1.")
else:
    print("A média não é par ou é menor que -1.")
