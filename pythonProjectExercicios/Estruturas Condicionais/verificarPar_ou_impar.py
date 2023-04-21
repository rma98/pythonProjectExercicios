# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou é ÍMPAR.

num = int(input('Número: '))
if num % 2 == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')

# Outras formas de fazer

# 1
num = int(input('Número: '))
if num & 1 == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')

# 2
num = int(input('Número: '))
if divmod(num, 2)[1] == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')

# 3
num = int(input('Número: '))
print(f'O número {num} é {"par" if num % 2 == 0 else "ímpar"}.')
