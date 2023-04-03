# Leia um número inteiro e mostre uma mensagem indicando se este número é par-positivo, par-negativo, ímpar-positivo
# ou ímpar-negativo.

num = int(input("Número: "))
if num % 2 == 0 and num > -1:
    print(f"{num} -> par-positivo")
elif num % 2 != 0 and num > -1:
    print(f"{num} -> ímpar-positivo")
elif num % 2 == 0 and num < 0:
    print(f"{num} -> par-negativo")
else:
    print(f"{num} -> ímpar-negativo")

# Outras formas de fazer

# 1
num = int(input("Número: "))
parity = "par" if num % 2 == 0 else "ímpar"
sign = "positivo" if num >= 0 else "negativo"
print(f"{num} -> {parity}-{sign}")
