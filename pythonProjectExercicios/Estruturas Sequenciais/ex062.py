# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um números: 1834 -> Unidade:4 -> Dezena: 3 -> Centena -> Milhar: 1.

numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Analisando o número {numero}'
      f'\nUnidade: {unidade}'
      f'\nDezena {dezena}'
      f'\nCentena {centena}'
      f'\nMilhar {milhar}')
