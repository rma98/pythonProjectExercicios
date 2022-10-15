#29. Pergunte dois valores: quanto ele recebe mensalmente a qual o valor padrão. Se ele receber mais que o valor padrão.
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
