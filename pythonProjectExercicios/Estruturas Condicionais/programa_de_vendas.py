# Faça um programa que receba o valor da venda, escolha a condição de pagamento no menu e mostre o total da venda
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

# Outras formas de fazer
valor_da_venda = float(input("Valor da venda: R$"))
codigo = int(input("Código: "))

acoes = {
    1: {"descricao": "Desconto de 10%", "porcentagem": 10},
    2: {"descricao": "Desconto de 5%", "porcentagem": 5},
    3: {"descricao": "Sem desconto", "porcentagem": 0},
    4: {"descricao": "Acréscimo de 5%", "porcentagem": -5},
    5: {"descricao": "Desconto de 8%", "porcentagem": 8},
    6: {"descricao": "Desconto de 7%", "porcentagem": 7},
}

if codigo in acoes:
    acao = acoes[codigo]
    porcento = acao["porcentagem"] / 100
    if porcento > 0:
        desconto = valor_da_venda * porcento
        valor_da_venda -= desconto
    else:
        acrescimo = valor_da_venda * abs(porcento)
        valor_da_venda += acrescimo
    print(f"{acao['descricao']} - Total da venda: R${valor_da_venda:.2f}")
else:
    print("Código inválido.")
