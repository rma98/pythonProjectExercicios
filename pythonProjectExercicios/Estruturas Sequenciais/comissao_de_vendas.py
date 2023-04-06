# Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário
# fixo de um funcionário e o valor de suas vendas, calcule a comissão e seu salário final.

salario_Fixo = float(input("Salário Fixo: R$"))
comissao = 4/100
valor_Total_Vendas = 0
valor_Do_Produto = float(input("O produto X custa: R$"))
comprar = "S"
while comprar == "S":
    valor_Total_Vendas += valor_Do_Produto
    comprar = input("Comprar novamente? Digite \"S\" para continuar:").upper()
comissao *= valor_Total_Vendas
print(f"Comissão: R${comissao:.2f}\nTotal do valor das vendas: R${valor_Total_Vendas:.2f}"
      f"\nSalário: R${salario_Fixo + comissao:.2f}")

# Outras formas de fazer

# 1
salario_Fixo = float(input("Salário Fixo: R$"))
comissao = 4/100
valor_Total_Vendas = 0
valor_Do_Produto = float(input("O produto X custa: R$"))
comprar = input("Comprar novamente? Digite \"S\" para continuar:").upper()

if comprar == "S":
    while True:
        valor_Total_Vendas += valor_Do_Produto
        comprar = input("Comprar novamente? Digite \"S\" para continuar:").upper()
        if comprar != "S":
            break

comissao *= valor_Total_Vendas
print(f"Comissão: R${comissao:.2f}\nTotal do valor das vendas: R${valor_Total_Vendas:.2f}"
      f"\nSalário: R${salario_Fixo + comissao:.2f}")

# 2
def calcula_salario(salario_fixo):
    comissao = 4/100
    valor_Total_Vendas = 0
    valor_Do_Produto = float(input("O produto X custa: R$"))
    comprar = input("Comprar novamente? Digite \"S\" para continuar:").upper()

    if comprar == "S":
        valor_Total_Vendas += valor_Do_Produto
        calcula_salario_aux = calcula_salario(salario_fixo)
        valor_Total_Vendas += calcula_salario_aux[0]
        comissao = comissao * (valor_Total_Vendas + calcula_salario_aux[0])
    else:
        comissao = comissao * valor_Total_Vendas

    salario_final = salario_fixo + comissao
    return [valor_Total_Vendas, salario_final]

salario_Fixo = float(input("Salário Fixo: R$"))
resultado = calcula_salario(salario_Fixo)
print(f"Comissão: R${resultado[1] - salario_Fixo:.2f}\nTotal do valor das vendas: R${resultado[0]:.2f}"
      f"\nSalário: R${resultado[1]:.2f}")

# 3
salario_Fixo = float(input("Salário Fixo: R$"))
comissao = 4/100
valor_Total_Vendas = 0
produtos = []

while True:
    valor_Do_Produto = float(input("Digite o valor do produto X (ou 0 para sair): R$"))
    if valor_Do_Produto == 0:
        break
    produtos.append(valor_Do_Produto)

valor_Total_Vendas = sum(produtos)
comissao *= valor_Total_Vendas
salario_final = salario_Fixo + comissao

print(f"Comissão: R${comissao:.2f}\nTotal do valor das vendas: R${valor_Total_Vendas:.2f}"
      f"\nSalário: R${salario_final:.2f}")

# 4
def calcula_salario(salario_Fixo):
    comissao = 4/100
    valor_Total_Vendas = 0
    valor_Do_Produto = 1  # Inicializa com um valor diferente de zero para entrar no loop
    while valor_Do_Produto != 0:
        valor_Do_Produto = float(input("Digite o valor do produto X (ou 0 para sair): R$"))
        valor_Total_Vendas += valor_Do_Produto
    comissao *= valor_Total_Vendas
    salario_final = salario_Fixo + comissao
    return [valor_Total_Vendas, salario_final]

salario_Fixo = float(input("Salário Fixo: R$"))
resultado = calcula_salario(salario_Fixo)
print(f"Comissão: R${resultado[1] - salario_Fixo:.2f}\nTotal do valor das vendas: R${resultado[0]:.2f}"
      f"\nSalário: R${resultado[1]:.2f}")
