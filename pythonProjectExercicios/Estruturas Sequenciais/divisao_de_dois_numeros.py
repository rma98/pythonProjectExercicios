# Faça um programa que receba dois números, calcule e mostre a divisão do primeiro pelo segundo. Sabe-se que o
# segundo número não pode ser zero, portanto, não é necessário se preocupar com validações.

n1 = int(input("Primeiro Número: "))
n2 = int(input("Segundo Número: "))
print(f"{n1} / {n2} = {n1 / n2}")

# Outras formas de fazer

# 1
n1, n2 = map(int, input("Digite dois números separados por espaço: ").split())

# 2
print("{} / {} = {}".format(n1, n2, n1 / n2))

# 3
print(f"{n1} / {n2} = {n1 // n2}")
