# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    if p > 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg'
      f'\nO menor peso lido foi de {menor}kg')

# Outras formas de fazer

# 1
pesos = []
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    pesos.append(peso)
maior = max(pesos)
menor = min(pesos)
print(f'O maior peso lido foi de {maior}kg'
      f'\nO menor peso lido foi de {menor}kg')

# 2
maior = float(input("Digite o peso da 1º pessoa: "))
menor = maior
for p in range(2, 6):
    peso = float(input(f'Digite o peso da {p}º pessoa: '))
    maior = max(maior, peso)
    menor = min(menor, peso)
print(f'O maior peso lido foi de {maior}kg'
      f'\nO menor peso lido foi de {menor}kg')
