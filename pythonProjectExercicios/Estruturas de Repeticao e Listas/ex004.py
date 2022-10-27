#4. Desenvolva um programa que leia seis números e mostre a soma apenas daqueles que forem pares. Se o valor digitado
# ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        cont += 1
        soma += numero
print(f'Você informou {cont} números pares e a soma é {soma}')
