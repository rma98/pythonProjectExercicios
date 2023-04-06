# Faça um programa que receba o preço o produto, calcule e mostre o novo preço, sabendo-se que este sofreu um
# desconto de 10%.

preco_Produto = float(input("Preço do produto: R$"))
desconto = preco_Produto * 10/100
preco_Produto -= desconto
print(f"Novo Preço do produto após sofrer um desconto de 10%: R${preco_Produto:.2f}")

# Outras formas de fazer

# 1
def calcular_preco_com_desconto(preco, desconto):
    preco_com_desconto = preco - (preco * desconto)
    return preco_com_desconto

preco_produto = float(input("Preço do produto: R$"))
desconto = 0.1
novo_preco = calcular_preco_com_desconto(preco_produto, desconto)
print(f"Novo Preço do produto após sofrer um desconto de 10%: R${novo_preco:.2f}")

# 2
preco_produto = float(input("Preço do produto: R$"))
desconto = 0.1
novo_preco = (lambda preco, desc: preco - (preco * desc))(preco_produto, desconto)
print(f"Novo Preço do produto após sofrer um desconto de 10%: R${novo_preco:.2f}")

# 3
class Produto:
    def __init__(self, preco):
        self.preco = preco
    
    def aplicar_desconto(self, desconto):
        self.preco -= self.preco * desconto
    
    def __str__(self):
        return f"R${self.preco:.2f}"
    
preco_produto = float(input("Preço do produto: R$"))
desconto = 0.1
produto = Produto(preco_produto)
produto.aplicar_desconto(desconto)
print(f"Novo Preço do produto após sofrer um desconto de 10%: {produto}")
