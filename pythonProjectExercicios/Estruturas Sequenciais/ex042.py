#42. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário
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
