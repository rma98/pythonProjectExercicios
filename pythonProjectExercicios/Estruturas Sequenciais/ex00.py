# Crie um programa que escreva "Olá, Mundo!" na tela.

print('Olá, Mundo!')

# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Seu nome: ')
print(f'Olá {nome}! Prazer em te conhecer!')

# Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
print(f'{num1} + {num2} = {num1 + num2}')

# Faça um programa que leia algo pelo usuário e mostre na tela seu tipo primitivo e todas as informações possíveis sobre
# ela.

infor = input('Digite algo: ')
print(f'Tipo primitivo: {type(infor)}\nSó tem espaços? {infor.isspace()}\nÉ um número? {infor.isnumeric()}'
      f'\nÉ alfabético? {infor.isalpha()}\nÉ alfanumérico? {infor.isalnum()}\nEstá em maiúsculos? {infor.isupper()}'
      f'\nEstá em minúsculos? {infor.islower()}\nEstá capitalizada? {infor.istitle()}')
