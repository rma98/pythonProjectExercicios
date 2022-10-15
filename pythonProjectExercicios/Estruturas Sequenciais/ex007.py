#7. Pergunte três valores ao usuário e imprima se a soma do primeiro com o terceiro digitado é menor que o dobro do
#do segundo ou terceiro é maior que o dobro do primeiro.

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
valor3 = int(input("Valor 3: "))
if valor1 + valor3 < valor2 * 2 or valor3 > valor1 * 2:
    print(True)
else:
    print(False)
