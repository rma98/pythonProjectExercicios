#1. Reescreva a função leiaInt() feita no ex009 do diretório Funcoes, incluindo agora a possibilidade de digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from lendoNumeros import leiaInt, leiaFloat

n1 = leiaInt('Digite um número: ')
n2 = leiaFloat('Digite um número: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
