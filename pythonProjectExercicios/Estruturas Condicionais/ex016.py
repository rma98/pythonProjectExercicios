#16. Faça um programa que receba o valor da venda, escolha a condição de pagamento no menu e mostre o total da venda
# final conforme condições a seguir:
# -> 01 - A vista - Desonct0 de 10%
# -> 02 - A prazo 30 dias - Desconto 5%
# -> 03 - A prazo 60 dias - Mesmo preço
# -> 04 -A prazo 90 dias - Acréscimo de 5%
# -> 05 - Com cartão de Débito - Desconto de 8%
# -> 06 - Com cartão de Crédito - Desconto de 7%

valor_Da_Venda = float(input("Valor da venda: R$"))
codigo = int(input("Código: "))
if codigo == 1:
    porcento = 10/100
    desconto = valor_Da_Venda * porcento
    valor_Da_Venda -= desconto
    print(f"Total da venda: R${valor_Da_Venda:.2f}")
elif codigo == 2:
    porcento = 5/100
    deconto = valor_Da_Venda * porcento
    valor_Da_Venda -= deconto
    print(f"Total da venda: R${valor_Da_Venda:.2f}")
elif codigo == 3:
    print(f"Total do valor da venda: R${valor_Da_Venda:.2f}")
elif codigo == 4:
    porcento = 5/100
    acrescimo = valor_Da_Venda * porcento
    valor_Da_Venda += acrescimo
    print(f"Total da venda: R${valor_Da_Venda:.2f}")
elif codigo == 5:
    porcento = 8/100
    desconto = valor_Da_Venda * porcento
    valor_Da_Venda -= desconto
    print(f"Total do valor da venda: R${valor_Da_Venda:.2f}")
elif codigo == 6:
    porcento = 7/100
    desconto = valor_Da_Venda * porcento
    valor_Da_Venda -= desconto
    print(f"Total do valor da venda: R${valor_Da_Venda:.2f}")
