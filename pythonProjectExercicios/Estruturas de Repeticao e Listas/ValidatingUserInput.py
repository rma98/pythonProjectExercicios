# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = input('Informe o sexo \"\033[34mM\033[m\" OU \"\033[35mF\033[m\"\n').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Digitação INVÁLIDA! Tente novamente.\n \"\033[34mM\033[m\" OU \"\033[35mF\033[m\"\n ').strip().upper()[0]
print(f'O sexo informado é {sexo}')

# Outras formas de fazer

# 1
while True:
    sexo = input('Informe o sexo \"\033[34mM\033[m\" OU \"\033[35mF\033[m\"\n').strip().upper()[0]
    if sexo in 'MF':
        break
    print('Digitação INVÁLIDA! Tente novamente.')
print(f'O sexo informado é {sexo}')

# 2
sexo = input('Informe o sexo \"\033[34mM\033[m\" OU \"\033[35mF\033[m\"\n').strip().upper()
while not sexo.isalpha() or sexo not in 'MF':
    print('Digitação INVÁLIDA! Tente novamente.')
    sexo = input('Informe o sexo \"\033[34mM\033[m\" OU \"\033[35mF\033[m\"\n').strip().upper()
print(f'O sexo informado é {sexo[0]}')
