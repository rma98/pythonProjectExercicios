# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Preço do produto: R$'))
desc = preco_produto * 5/100
preco_produto -= desc
print(f'O novo preço de do produto com 5% de desconto é de: R${preco_produto:.2f}')]

# Outras formas de fazer

# 1
preco_produto = float(input('Preço do produto: R$'))
desc = preco_produto * 5/100
preco_com_desc = preco_produto - desc
preco_com_desc = round(preco_com_desc, 2)
print(f'O novo preço de do produto com 5% de desconto é de: R${preco_com_desc:.2f}')

# 2
preco_produto = float(input('Preço do produto: R$'))
preco_produto -= preco_produto * 5/100
print(f'O novo preço de do produto com 5% de desconto é de: R${preco_produto:.2f}')

# 3
preco_produto = float(input('Preço do produto: R$'))
desc = preco_produto * 5/100
preco_com_desc = preco_produto - desc
print('O novo preço do produto com 5% de desconto é de: R${:.2f}'.format(preco_com_desc))

# 4
from math import fsum
preco_produto = float(input('Preço do produto: R$'))
preco_com_desc = fsum([preco_produto, -preco_produto * 5/100])
print(f'O novo preço de do produto com 5% de desconto é de: R${preco_com_desc:.2f}')
