#23. Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print(f'{"=" * 17}'
      f'\nCAIXA ELETRÔNICO'
      f'\n{"=" * 17}')
valor_saque = int(input('Qual será o valor a ser sacado: R$'))
tot = valor_saque
ced_atual = 50
tot_ced = 0
while True:
      if tot >= ced_atual:
            tot -= ced_atual
            tot_ced += 1
      else:
            if tot_ced > 0:
                  print(f'Total de {tot_ced} cédulas de R${ced_atual}')
            if ced_atual == 50:
                  ced_atual = 20
            elif ced_atual == 20:
                  ced_atual = 10
            elif ced_atual == 10:
                  ced_atual = 1
            tot_ced = 0
            if tot == 0:
                  break
