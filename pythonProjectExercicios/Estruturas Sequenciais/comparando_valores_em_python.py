# Pergunte dois valores ao usuário e imprima se o primeiro valor digitado é maior que o segundo.

valor1 = int(input("Valor 1:"))
valor2 = int(input("Valor 2:"))
print("O primeiro valor digitado é maior que o segundo: ", end='')
if valor1 > valor2:
    print(True)
else:
    print(False)

# Outras formas de fazer

# 1
valor1 = int(input("Valor 1:"))
valor2 = int(input("Valor 2:"))
maior = valor1 if valor1 > valor2 else valor2
print("O maior valor digitado é:", maior)

# 2
valor1 = int(input("Valor 1:"))
valor2 = int(input("Valor 2:"))
maior = max(valor1, valor2)
print("O maior valor digitado é:", maior)

# 3
valores = [int(input("Valor " + str(i+1) + ":")) for i in range(2)]
maior = max(valores)
print("O maior valor digitado é:", maior)
