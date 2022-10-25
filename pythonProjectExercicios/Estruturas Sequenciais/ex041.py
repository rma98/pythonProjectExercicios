#41. Faça um programa que receba o preço o produto, calcule e mostre o novo preço, sabendo-se que este sofreu um
# desconto de 10%.

preco_Produto = float(input("Preço do produto: R$"))
desconto = preco_Produto * 10/100
preco_Produto -= desconto
print(f"Novo Preço do produto após sofrer um desconto de 10%: R${preco_Produto:.2f}")

#41.1 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Preço do produto: R$'))
desc = preco_produto * 5/100
preco_produto -= desc
print(f'O novo preço de do produto com 5% de desconto é de: R${preco_produto:.2f}')

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_do_funcionario = float(input('Salário do funcionário: R$'))
aumento = salario_do_funcionario * 15/100
salario_do_funcionario += aumento
print(f'O novo salário do funcionário com 15% de aumento é de: R${salario_do_funcionario:.2f}')
