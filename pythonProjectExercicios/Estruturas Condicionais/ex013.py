#13. Pergunte ao usuário se três números (A, B, C). Se o primeiro for maior que a soma dos outros dois e o terceiro for
# for menor que que a subtração entre A e B, deve imprimir o produto entre os 3 valores, caso contrário deve imprimir o
# seguinte cáculo A**C+B.

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if a > b + c and c < a - b:
    print(f"Prdouto: {a * b * c}")
else:
    print(f"A ** C + B = {a ** c + b}")

#13.1 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'Maior: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'Maior: {n2}')
else:
    print(f'Maior: {n3}')
if n1 < n2 and n1 < n3:
    print(f'Menor: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'Menor: {n2}')
else:
    print(f'Menor: {n3}')
#VERIFICANDO QUEM É MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
#VERIFICANDO QUEM É MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
