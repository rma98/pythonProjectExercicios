# Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.

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

# Outras fornas de fazer

# 1
def inverter_string(texto):
    return texto[::-1]
frase = input('Digite uma frase: ').strip().upper()
junto = ''.join(frase.split())
inverso = inverter_string(junto)
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')

# 2
def inverter_string(texto):
    if len(texto) <= 1:
        return texto
    else:
        return inverter_string(texto[1:]) + texto[0]
frase = input('Digite uma frase: ').strip().upper()
junto = ''.join(frase.split())
inverso = inverter_string(junto)
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
