#7. Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
