#3. Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

tot= 0
soma = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            tot += 1
            soma += c
print(f'A soma de todos os {tot} valores solicitados é {soma}\n')

somando = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        somando += c
print(f'A soma de todos os {cont} valores solicitados é {somando}')
