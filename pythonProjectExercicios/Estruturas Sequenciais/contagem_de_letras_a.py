# Faça um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A".
# -> Em que posição ela aparece a primeira vez.
# -> Em que posição ela aparece a última vez.

frase = input('Frase: ').upper().strip()

print(f'A letra \"A\" aparece {frase.count("A")} vezes na frase'
      f'\nA primeira letra \"A\" apareceu na posição {frase.find("A")+1}'
      f'\nA última letra \"A\" apareceu na posição {frase.rfind("A")+1}')

# Outras formas de fazer

# 1
frase = input('Frase: ').upper().strip()

count = 0
first_occurrence = None
last_occurrence = None

for i, letra in enumerate(frase):
    if letra == 'A':
        if first_occurrence is None:
            first_occurrence = i + 1
        last_occurrence = i + 1
        count += 1

print(f'A letra "A" aparece {count} vezes na frase')
print(f'A primeira letra "A" apareceu na posição {first_occurrence}')
print(f'A última letra "A" apareceu na posição {last_occurrence}')

# 2
frase = input('Frase: ').upper().strip()

count = len([letra for letra in frase if letra == 'A'])
first_occurrence = frase.find('A') + 1
last_occurrence = frase.rfind('A') + 1

print(f'A letra "A" aparece {count} vezes na frase')
print(f'A primeira letra "A" apareceu na posição {first_occurrence}')
print(f'A última letra "A" apareceu na posição {last_occurrence}')
