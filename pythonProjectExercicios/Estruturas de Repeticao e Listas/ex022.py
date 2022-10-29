#22. Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# a -> Qual é o total gasto na compra.
# b-> Quantos produtos custam mais de R$1000.
# c -> Qual é o nome do produto mais barato.

res = 'S'
cont = tot_gastos = tot_produto1000 = menor = preco_menor_produto = 0
while res == 'S':
    print(f'{"=" * 10}'
          f'\nMY STORE'
          f'\n{"=" * 10}')
    nome_do_produto = input('Nome do produto: ').strip()
    preco_do_produto = float(input('Preço do produto: R$'))
    cont += 1
    print(f'{"=" * 35}'
          f'\n\033[32m{cont}º PRODUTO CADASTRADO COM SUCESSO.\033[m'
          f'\n{"=" * 35}')
    res = input('Deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    while res not in 'SN':
        res = input('Deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    tot_gastos += preco_do_produto
    if preco_do_produto > 1000:
        tot_produto1000 += 1
    if cont == 1:
        preco_menor_produto = preco_do_produto
        menor = nome_do_produto
    else:
        if preco_do_produto < preco_menor_produto:
            preco_menor_produto = preco_do_produto
            menor = nome_do_produto
print(f'\n{"=" * 30}'
      f'\n\033[31mFIM DO PROGRAMA\033[m'
      f'\n{"=" * 30}'
      f'\nO total gasto na compra é de \033[31mR${tot_gastos:.2f}\033[m'
      f'\n{tot_produto1000} produtos custando mais de \033[32mR$1000.00 reais.\033[m'
      f'\nO produto mais barato foi \033[33m{menor} que custa R${preco_menor_produto:.2f} reais.\033[m')
