#6. Pergunte dois valores ao usuário e imprima se o primeiro valor digitado é maior que o segundo.

valor1 = int(input("Valor 1:"))
valor2 = int(input("Valor 2:"))
print("O primeiro valor digitado é maior que o segundo: ", end='')
if valor1 > valor2:
    print(True)
else:
    print(False)
