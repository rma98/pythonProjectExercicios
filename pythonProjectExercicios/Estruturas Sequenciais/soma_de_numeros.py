# Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
print(f'{num1} + {num2} = {num1 + num2}')

# Outras formas de fazer

# 1
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
soma = sum([num1, num2])
print(f'{num1} + {num2} = {soma}')

# 2
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
soma = num1 + num2
print('{} + {} = {}'.format(num1, num2, soma))

# 3
num1 = input('Primeiro número: ')
num2 = input('Segundo número: ')
if num1.isnumeric() and num2.isnumeric():
    num1, num2 = int(num1), int(num2)
    print(f'{num1} + {num2} = {num1 + num2}')
else:
    print('Digite apenas valores inteiros')
