# Desenvolva um programa que leia seis números e mostre a soma apenas daqueles que forem pares. Se o valor digitado
# ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        cont += 1
        soma += numero
print(f'Você informou {cont} números pares e a soma é {soma}')

# Outras formas de fazer

# 1
numeros = []
for i in range(1, 7):
    numero = int(input(f'Digite o {i}º valor: '))
    numeros.append(numero)

pares = [n for n in numeros if n % 2 == 0]
soma_pares = sum(pares)

print(f'Você informou {len(pares)} números pares e a soma é {soma_pares}')

# 2
soma = 0
cont = 0
while cont < 6:
    numero = int(input(f'Digite o {cont+1}º valor: '))
    if numero % 2 == 0:
        cont += 1
        soma += numero

print(f'Você informou 6 números pares e a soma é {soma}')
