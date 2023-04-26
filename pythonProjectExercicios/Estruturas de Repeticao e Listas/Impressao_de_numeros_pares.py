# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' -> ')
print('FIM\n')

# Outras formas de fazer

# 1
for c in range(1, 51, 2):
    print(f'{c+1}', end=" -> ")
print('FIM')

# 2
c = 1
while c <= 50:
    if c % 2 == 0:
        print(c, end=' -> ')
    c += 1
print('FIM\n')

# 3
numeros = list(range(1, 51))
pares = [num for num in numeros if num % 2 == 0]
for num in pares:
    print(num, end=' -> ')
print('FIM\n')

# 4
for c in range(2, 51, 2):
    print(c, end=' -> ')
print('FIM\n')
