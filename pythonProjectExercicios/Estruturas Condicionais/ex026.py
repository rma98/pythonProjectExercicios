#26. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -> 1 para binário
# -> 2 para octal
# -> 3 para hexadecimal

numero = int(input('Digite um número: '))
print(f'\033[7;37;40m{" " * 10} TABELA DE CONVERSÃO {" " * 7}\033[m'
      f'\n\033[7;37;40m{" " * 2}1 -> BINÁRIO{" " * 24}\033[m'
      f'\n\033[7;37;40m{" " * 2}2 -> OCTAL{" " * 26}\033[m'
      f'\n\033[7;37;40m{" " * 2}3 - > HEXADECIMAL{" " * 19}\033[m')
escolha = int(input('Qual será a base de conversão? '))
if escolha == 1:
      print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif escolha == 2:
      print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif escolha == 3:
      print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
      print('NENHUMA DAS OPÇÕES ACIMA!')
