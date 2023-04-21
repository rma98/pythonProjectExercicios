# Leia um número inteiro e mostre uma mensagem indicando  se este número é par-positivo, par-negativo,
# ímpar-positivo ou ímpar-negativo.

n1 = int(input("Número: "))
if n1 % 2 == 0 and n1 > -1:
    print("Par-positivo!")
elif n1 % 2 == 0 and n1 < 0:
    print("Par-negativo!")
elif n1 % 2 != 0 and n1 > -1:
    print("Ímpar-positivo!")
else:
    print("Ímpar-negativo!")

# Outras formas de fazer

# 1
n1 = int(input("Número: "))
if n1 % 2 == 0:
    if n1 >= 0:
        print("Par-positivo!")
    else:
        print("Par-negativo!")
else:
    if n1 >= 0:
        print("Ímpar-positivo!")
    else:
        print("Ímpar-negativo!")
