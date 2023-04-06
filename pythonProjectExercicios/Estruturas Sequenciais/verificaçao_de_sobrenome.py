# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Nome Completo: ').upper().strip()
print('SILVA' in nome)

# Outras formas de fazer

# 1
nome = input('Nome Completo: ').upper().strip()
print(nome.find('SILVA') != -1)

# 2
nome = input('Nome Completo: ').upper().strip()
sobrenome = nome.split()[-1]
print(sobrenome == 'SILVA')

# 3
import re
nome = input('Nome Completo: ').upper().strip()
match = re.search(r'\bSILVA\b', nome)
print(match is not None)
