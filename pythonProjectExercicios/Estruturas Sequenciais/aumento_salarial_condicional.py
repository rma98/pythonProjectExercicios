# Pergunte dois valores: quanto ele recebe mensalmente a qual o valor padrão.
# Se ele receber mais que o valor padrão, ganhará 11,7% de aumento e logo depois um desconto de 5,4% nessa ordem caso
# contrário receberá 3.9% de desconto seguido de 13,06% de aumento. Imprima o valor do novo salário.

valor_Mensamente = float(input("Valor mensal: "))
valor_Padrao = float(input("Valor padrão: "))
if valor_Padrao < valor_Mensamente:
    porcento = 11.7/100
    porcento2 = 5.4/100
    aumento = valor_Mensamente * porcento
    desconto = valor_Mensamente * porcento2
    print(f"Novo salário: R${valor_Mensamente + aumento - desconto:.2f}")
else:
    porcento = 3.9/100
    porcento2 = 13.06/100
    aumento = valor_Mensamente * porcento
    desconto = valor_Mensamente * porcento2
    print(f"Novo salário: R${valor_Mensamente + aumento - desconto:.2f}")

# Outras formas de fazer

# 1
valor_Mensamente = float(input("Valor mensal: "))
valor_Padrao = float(input("Valor padrão: "))
porcento, porcento2 = (11.7/100, 5.4/100) if valor_Padrao < valor_Mensamente else (3.9/100, 13.06/100)
aumento = valor_Mensamente * porcento
desconto = valor_Mensamente * porcento2
novo_salario = valor_Mensamente + aumento - desconto
print(f"Novo salário: R${novo_salario:.2f}")

# 2
def calcular_aumento_e_desconto(salario, taxa_aumento, taxa_desconto):
    aumento = salario * taxa_aumento
    desconto = salario * taxa_desconto
    return aumento, desconto

valor_Mensamente = float(input("Valor mensal: "))
valor_Padrao = float(input("Valor padrão: "))
if valor_Padrao < valor_Mensamente:
    porcento_aumento, porcento_desconto = 11.7/100, 5.4/100
else:
    porcento_aumento, porcento_desconto = 3.9/100, 13.06/100
aumento, desconto = calcular_aumento_e_desconto(valor_Mensamente, porcento_aumento, porcento_desconto)
novo_salario = valor_Mensamente + aumento - desconto
print(f"Novo salário: R${novo_salario:.2f}")

# 3
valor_Mensamente = float(input("Valor mensal: "))
valor_Padrao = float(input("Valor padrão: "))
taxas = {
    valor_Padrao < valor_Mensamente: {'aumento': 11.7/100, 'desconto': 5.4/100},
    valor_Padrao >= valor_Mensamente: {'aumento': 3.9/100, 'desconto': 13.06/100}
}
porcento_aumento = taxas[True]['aumento']
porcento_desconto = taxas[True]['desconto']
aumento = valor_Mensamente * porcento_aumento
desconto = valor_Mensamente * porcento_desconto
novo_salario = valor_Mensamente + aumento - desconto
print(f"Novo salário: R${novo_salario:.2f}")
