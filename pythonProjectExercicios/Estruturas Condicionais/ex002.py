#2. Leia um número inteiro e mostre uma mensagem indicando  se este número número é par-positivo, par-negativo,
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

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou é ÍMPAR.

num = int(input('Número: '))
if num % 2 == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')
