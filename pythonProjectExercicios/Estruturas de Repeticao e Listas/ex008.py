#8. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são de maiores.

from datetime import date
menores = 0
maiores = 0
for c in range(1, 8):
    ano_de_nascimento = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = date.today().year - ano_de_nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'{menores} pessoas ainda não atingiram a maioridade.'
      f'\n{maiores} pessoas já são maiores de idade.')
