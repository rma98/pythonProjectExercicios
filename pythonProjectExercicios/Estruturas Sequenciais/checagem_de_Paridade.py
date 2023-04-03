# Pergunte um número ao usuário e imprima se ele é par.

numero = int(input("Número: "))
if numero % 2 == 0:
    print(True)
else:
    print(False)

# Outras formas de fazer

# 1
numero = int(input("Número: "))
if numero // 2 * 2 == numero:
    print(True)
else:
    print(False)

# 2
numero = int(input("Número: "))
if divmod(numero, 2)[1] == 0:
    print(True)
else:
    print(False)

# 3
numero = int(input("Número: "))
print(True) if numero % 2 == 0 else print(False)
