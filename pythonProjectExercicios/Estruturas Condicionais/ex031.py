#31. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de
# pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartaão: 20% de juros

preco_do_produto = float(input('Valor total das compras: R$'))
print(f'\033[7;37;40m{" " * 10} CONDIÇÃO DE PAGAMENTO {" " * 17}\033[m'
      f'\n\033[7;37;40m{" " * 2}1 -> À vista dinheiro/cheque: 10% de desconto{" " * 3}\033[m'
      f'\n\033[7;37;40m{" " * 2}2 -> À vista no cartão: 5% de desconto{" " * 10}\033[m'
      f'\n\033[7;37;40m{" " * 2}3 -> Em até 2x no cartão: preço normal{" " * 10}\033[m'
      f'\n\033[7;37;40m{" " * 2}4 -> 3x ou mais no cartaão: 20% de juros{" " * 8}\033[m')
opcao = int(input('Qual a forma de pagamento? '))
if opcao == 1:
      preco_do_produto -= preco_do_produto * 10 / 100
elif opcao == 2:
      preco_do_produto -= preco_do_produto * 5 / 100
elif opcao == 3:
      parcela = preco_do_produto / 2
      print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
      preco_do_produto += preco_do_produto * 20 / 100
      total_de_parcelas = int(input('Quantas parcelas? '))
      parcela = preco_do_produto / total_de_parcelas
      print(f'Sua compra será parcelada em {total_de_parcelas}x de R${parcela:.2f} com juros.')
else:
      print(f'\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente.\033[m')
print(f'Sua compra vai custar R${preco_do_produto:.2f} no final.')
