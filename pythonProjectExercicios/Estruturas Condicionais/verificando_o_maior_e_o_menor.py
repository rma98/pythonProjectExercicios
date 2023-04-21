# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

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

# Outras formas de fazer

# 1
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
menor = min(n1, n2, n3)
maior = max(n1, n2, n3)
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

# 2
numeros = [int(input('Digite um número: ')) for _ in range(3)]
menor = min(numeros)
maior = max(numeros)
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
