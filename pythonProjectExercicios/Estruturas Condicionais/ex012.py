#12. Pergunte ao usuário dois valores: quanto ele recebe mensalmente e qual o valor padrão. Se ele recebeer mais que o
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
