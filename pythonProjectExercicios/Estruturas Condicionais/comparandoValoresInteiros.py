# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# -> O primeiro valor é maior
# -> O segundo valor é maior
# -> Não existe valor maior, os dois são iguais

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
maior = num1
if num2 > num1:
    maior = num2
    print(f'\033[35mO SEGUNDO valor é maior\033[m')
elif num1 == num2:
    print('\033[36mNão existe valor maior, os dois são iguais!\033[m')
else:
    print(f'\033[34mO PRIMEIRO valor é maior\033[m')

# Outras formas de fazer

# 1
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
maior = max(num1, num2)

if num1 == num2:
    print('\033[36mNão existe valor maior, os dois são iguais!\033[m')
else:
    print(f'\033[34mO {maior} é maior\033[m')

# 2
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
maior = num1 if num1 > num2 else num2

if num1 == num2:
    print('\033[36mNão existe valor maior, os dois são iguais!\033[m')
else:
    print(f'\033[34mO {maior} é maior\033[m')
