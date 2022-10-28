#11. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = input('Informe o sexo \"\033[34mM\033[m\" OU \"\033[35mF\033[m\"\n').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Digitação INVÁLIDA! Tente novamente.\n \"\033[34mM\033[m\" OU \"\033[35mF\033[m\"\n ').strip().upper()[0]
print(f'O sexo informado é {sexo}')
