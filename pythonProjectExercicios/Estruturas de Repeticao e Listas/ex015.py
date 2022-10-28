#15. Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# sequência de Fibonacci.

print(f'\033[34m{"-=" *15}\033[m'
      f'\n\033[1mSEUQÊNCIA DE FIBONACCI'
      f'\n\033[34m{"-=" *15}\033[m')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end="")
inicio = 3
while inicio <= n:
    t3 = t1 + t2
    print(f'{t3} ', end="-> ")
    t1 = t2
    t2 = t3
    inicio += 1
print('FIM')
