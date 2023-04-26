# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

tot= 0
soma = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            tot += 1
            soma += c
print(f'A soma de todos os {tot} valores solicitados é {soma}\n')

# Outras formas de fazer

# 1
tot = 0
soma = 0
c = 1
while c < 501:
    if c % 2 != 0 and c % 3 == 0:
        tot += 1
        soma += c
    c += 1
print(f'A soma de todos os {tot} valores solicitados é {soma}\n')

# 2
numeros = [n for n in range(1, 501) if n % 2 != 0 and n % 3 == 0]
tot = len(numeros)
soma = sum(numeros)
print(f'A soma de todos os {tot} valores solicitados é {soma}\n')

# 3
somando = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        somando += c
print(f'A soma de todos os {cont} valores solicitados é {somando}')
