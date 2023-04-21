# Pergunte ao usuário se três números (A, B, C). Se o primeiro for maior que a soma dos outros dois e o terceiro for
# menor que que a subtração entre A e B, deve imprimir o produto entre os 3 valores, caso contrário deve imprimir o
# seguinte cálculo A**C+B.

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if a > b + c and c < a - b:
    print(f"Prdouto: {a * b * c}")
else:
    print(f"A ** C + B = {a ** c + b}")

# Outras formas de fazer

# 1
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

def calculate_result(a, b, c):
    if a > b + c and c < a - b:
        return a * b * c
    else:
        return a ** c + b

result = calculate_result(a, b, c)
print(result)

# 2
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

result = a * b * c if a > b + c and c < a - b else a ** c + b
print(result)
