# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Em que cidade você nasceu: ').upper().strip()
print(cidade[:5] == 'SANTO')

# Outras formas de fazer

# 1
cidade = input('Em que cidade você nasceu: ').lower().strip()
print(cidade[:5] == 'santo')

# 2
cidade = input('Em que cidade você nasceu: ').strip()
print(cidade.startswith('SANTO'))

# 3
cidade = input('Em que cidade você nasceu: ').strip()
comeca_com_santo = cidade[:5] == 'SANTO'
print(comeca_com_santo)

# 4
cidade = input('Em que cidade você nasceu: ').strip()
if cidade[:5] == 'SANTO':
    print('Você nasceu em Santo!')
else:
    print('Você não nasceu em Santo.')
