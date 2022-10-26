# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Em que cidade você nasceu: ').upper().strip()
print(cidade[:5] == 'SANTO')

#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Nome Completo: ').upper().strip()
print('SILVA' in nome)
