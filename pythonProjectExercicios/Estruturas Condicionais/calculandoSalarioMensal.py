# Pergunte ao usuário dois valores: quanto ele recebe mensalmente e qual o valor padrão. Se ele receber mais que o
# valor padrão, ganhará 11.7% de aumento e logo depois um desconto de 5.4% nessa ordem; caso contrário receberá 3.9%
# de desconto seguido de 13.06% de aumento. Imprima o valor do novo salário.

valor_Mensal = float(input("Valor mensal: R$"))
valor_Padrao = float(input("Valor padrão: R$"))
if valor_Mensal > valor_Padrao:
    porcento = 11.7/100
    porcento2 = 5.4/100
    aumento = valor_Mensal * porcento
    desconto = valor_Mensal * porcento2
    valor_Mensal += aumento - desconto
    print(f"Aumento: R${aumento:.2f}\nDesconto: R${desconto:.2f}\nSalário: R${valor_Mensal:.2f}")
else:
    porcento = 3.9/100
    porcento2 = 13.06/100
    aumento = valor_Mensal * porcento2
    desconto = valor_Mensal * porcento
    valor_Mensal += aumento - desconto
    print(f"Aumento: R${aumento:.2f}\nDesconto: R${desconto:.2f}\nSalário: {valor_Mensal:.2f}")

# Outras formas de fazer

# 1
valor_Mensal = float(input("Valor mensal: R$"))
valor_Padrao = float(input("Valor padrão: R$"))

porcento = (11.7/100, 5.4/100) if valor_Mensal > valor_Padrao else (3.9/100, 13.06/100)

aumento = valor_Mensal * porcento[0]
desconto = valor_Mensal * porcento[1]
valor_Mensal += aumento - desconto

print(f"Aumento: R${aumento:.2f}\nDesconto: R${desconto:.2f}\nSalário: R${valor_Mensal:.2f}")

# 2
valor_Mensal = float(input("Valor mensal: R$"))
valor_Padrao = float(input("Valor padrão: R$"))

porcento = 11.7/100 if valor_Mensal > valor_Padrao else 3.9/100
porcento2 = 5.4/100 if valor_Mensal > valor_Padrao else 13.06/100

aumento = valor_Mensal * porcento
desconto = valor_Mensal * porcento2
valor_Mensal += aumento - desconto

print(f"Aumento: R${aumento:.2f}\nDesconto: R${desconto:.2f}\nSalário: R${valor_Mensal:.2f}")

# 3
def calcular_aumento_desconto(valor_Mensal, porcento_aumento, porcento_desconto):
    aumento = valor_Mensal * porcento_aumento
    desconto = valor_Mensal * porcento_desconto
    novo_valor = valor_Mensal + aumento - desconto
    return aumento, desconto, novo_valor

valor_Mensal = float(input("Valor mensal: R$"))
valor_Padrao = float(input("Valor padrão: R$"))

if valor_Mensal > valor_Padrao:
    porcento_aumento = 11.7/100
    porcento_desconto = 5.4/100
else:
    porcento_aumento = 13.06/100
    porcento_desconto = 3.9/100

aumento, desconto, valor_Mensal = calcular_aumento_desconto(valor_Mensal, porcento_aumento, porcento_desconto)

print(f"Aumento: R${aumento:.2f}\nDesconto: R${desconto:.2f}\nSalário: R${valor_Mensal:.2f}")
