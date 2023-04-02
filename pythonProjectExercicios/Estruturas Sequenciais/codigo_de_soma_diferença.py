# Criar um algoritmo que pergunta dois números ao usuário e informa a soma deles é maior que a subtração deles.

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
if valor1 + valor2 > valor1 - valor2:
    print(True)
else:
    print(False)

# Outras formas de fazer

# 1
valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
print(True if valor1 + valor2 > valor1 - valor2 else False)

# 2
valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
print(bool(valor1 + valor2 > valor1 - valor2))

# 3
valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
print(valor1 + valor2 >= valor1 - valor2)

# 4
valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
resultado = valor1 + valor2 > valor1 - valor2
print(resultado)
