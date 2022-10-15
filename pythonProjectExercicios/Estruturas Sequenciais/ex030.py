#30. Pergunte ao usuário três números (A, B, C). Se o primeiro for maior que a soma dos outros dois e o terceiro for
# menor que a subtração entre A e B, deve imprimir o produto entre os 3 valores caso contrário deve imprimir o seguinte
# cálculo A**C+B.

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if a > b + c and c < a - b:
    print(f"Produto: {a * b * c}")
else:
    print(a**c+b)
