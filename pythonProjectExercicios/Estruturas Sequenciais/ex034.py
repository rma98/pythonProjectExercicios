# Faça um programa que receba o valor da venda, escolha a condição de pagamento no menu e mostre o total da venda final
# conforme as condições a seguir:
# -> 01 - A vista - Desconto de 10%
# -> 02 - A prazo 30 dias - Desconto de 5%
# -> 03 - A prazo 60 dias - Mesmo preço
# -> 04 - A prazo 90 dias - Acréscimo de 5%
# -> 05 - Com cartão de Débito - Desconto de 8%
# -> 06 - Com cartão de Crédito - Desconto de 7%

valor_Da_Venda = float(input("Valor da venda R$: "))
codigo = int(input("Código: "))
if codigo == 1:
    porcento = 10/100
    desconto = valor_Da_Venda * porcento
    valor_Da_Venda -= desconto
    print(f"O total da venda foi de R${valor_Da_Venda:.2f}")
elif codigo == 2:
    porcento = 5/100
    desconto = valor_Da_Venda * porcento
    valor_Da_Venda -= desconto
    print(f"O total da venda foi de R${valor_Da_Venda:.2f}")
elif codigo == 3:
    print(f"O valor da venda foi de R${valor_Da_Venda:.2f}")
elif codigo == 4:
    porcento = 5/100
    acrescimo = valor_Da_Venda * porcento
    valor_Da_Venda += acrescimo
    print(f"O valor da venda foi de R${valor_Da_Venda:.2f}")
elif codigo == 5:
    porcento = 8/100
    desconto = valor_Da_Venda * porcento
    valor_Da_Venda -= desconto
    print(f"O valor da venda foi de R${valor_Da_Venda:.2f}")
elif codigo == 6:
    porcento = 7/100
    desconto = valor_Da_Venda * porcento
    valor_Da_Venda -= desconto
    print(f"O valor da venda foi de R${valor_Da_Venda:.2f}")
else:
    print("Código inválido!")
