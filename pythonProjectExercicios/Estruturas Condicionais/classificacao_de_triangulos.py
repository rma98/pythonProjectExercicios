# Desenvolva um programa que leia o comprimento de três rotas e diga ao usuário se elas podem ou não formar um triângulo.
# Qual tipo de triângulo será formado:
# -> equilátero: todos os lados iguais.
# -> isósceles: dois lados iguais.
# -> escaleno: todos os lados diferentes.

print('-=-'*20)
print('\033[7;37;40mANALISADOR DE TRIÂNGULO\033[m')
print('-=-'*20)

reta_a = int(input('Primeira reta: '))
reta_b = int(input('Segunda reta: '))
reta_c = int(input('Terceira reta: '))

if reta_a < reta_b + reta_c and reta_b < reta_a + reta_c and reta_c < reta_a + reta_b:
    print('\033[32mPodem formar um triângulo!\033[m', end=' ')
    if reta_a == reta_b == reta_c:
        print(f'\033[33mEQUILÁTERO!\033[33m')
    elif reta_a != reta_b !=reta_c != reta_a:
        print(f'\033[34mESCALENO!\033[m')
    else:
        print(f'\033[36mISÓCELES!\033[m')
else:
    print('\033[33mNão podem formar triângulo!\033[m')

# Outras formas de fazer
print('-=-'*20)
print('\033[7;37;40mANALISADOR DE TRIÂNGULO\033[m')
print('-=-'*20)

reta_a, reta_b, reta_c = sorted([int(input('Primeira reta: ')), int(input('Segunda reta: ')), int(input('Terceira reta: '))])

if reta_a + reta_b > reta_c:
    print('\033[32mPodem formar um triângulo!\033[m', end=' ')
    if reta_a == reta_b == reta_c:
        print(f'\033[33mEQUILÁTERO!\033[m')
    elif reta_a != reta_b !=reta_c != reta_a:
        print(f'\033[34mESCALENO!\033[m')
    else:
        print(f'\033[36mISÓCELES!\033[m')
else:
    print('\033[33mNão podem formar triângulo!\033[m')
