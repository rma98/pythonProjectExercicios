#41. Faça um programa que receba o preço o produto, calcule e mostre o novo preço, sabendo-se que este sofreu um
# desconto de 10%.

preco_Produto = float(input("Preço do produto: R$"))
porcento = 10/100
desconto = preco_Produto * porcento
preco_Produto -= desconto
print(f"Novo Preço: R${preco_Produto:.2f}")
