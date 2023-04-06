# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Número: '))
print(f'Antecessor: {num-1}\nSucessor: {num+1}')

# Outras formas de fazer

# 1
num = int(input('Número: '))
antecessor = num - 1
sucessor = num + 1
print(f'Antecessor: {antecessor}\nSucessor: {sucessor}')

# 2
num = int(input('Número: '))
antecessor = num - 1
sucessor = num + 1
print('Antecessor: {}\nSucessor: {}'.format(antecessor, sucessor))

# 3
def antecessor_e_sucessor(num):
    antecessor = num - 1
    sucessor = num + 1
    return antecessor, sucessor

num = int(input('Número: '))
antecessor, sucessor = antecessor_e_sucessor(num)
print(f'Antecessor: {antecessor}\nSucessor: {sucessor}')

# 4
num = int(input('Número: '))
antecessor, sucessor = num - 1, num + 1
print(f'Antecessor: {antecessor}\nSucessor: {sucessor}')
