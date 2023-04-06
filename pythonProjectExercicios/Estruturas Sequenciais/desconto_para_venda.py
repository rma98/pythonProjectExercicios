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

# Outras formas de fazer

# 1
valor_Da_Venda = float(input("Valor da venda R$: "))
codigo = int(input("Código: "))

descontos_acrescimos = {
    1: 0.1,
    2: 0.05,
    3: 0,
    4: 0.05,
    5: 0.08,
    6: 0.07
}

if codigo in descontos_acrescimos:
    fator = 1 - descontos_acrescimos[codigo] if codigo < 4 else 1 + descontos_acrescimos[codigo]
    valor_Da_Venda *= fator
    print(f"O valor da venda foi de R${valor_Da_Venda:.2f}")
else:
    print("Código inválido!")

# 2
valor_Da_Venda = float(input("Valor da venda R$: "))
codigo = int(input("Código: "))

descontos_acrescimos = [
    (1, 0.1),
    (2, 0.05),
    (3, 0),
    (4, 0.05),
    (5, 0.08),
    (6, 0.07)
]

for tupla in descontos_acrescimos:
    if codigo == tupla[0]:
        fator = 1 - tupla[1] if codigo < 4 else 1 + tupla[1]
        valor_Da_Venda *= fator
        print(f"O valor da venda foi de R${valor_Da_Venda:.2f}")
        break
else:
    print("Código inválido!")

# 3
def calcular_valor_venda(valor_Da_Venda, codigo):
    if codigo == 1:
        porcento = 10/100
    elif codigo == 2:
        porcento = 5/100
    elif codigo == 3:
        porcento = 0
    elif codigo == 4:
        porcento = 5/100
    elif codigo == 5:
        porcento = 8/100
    elif codigo == 6:
        porcento = 7/100
    else:
        return None
    
    fator = 1 - fator * porcento if codigo < 4 else 1 + porcento
    return valor_Da_Venda * fator

valor_Da_Venda = float(input("Valor da venda R$: "))
codigo = int(input("Código: "))

valor_final = calcular_valor_venda(valor_Da_Venda, codigo)
if valor_final is not None:
    print(f"O valor da venda foi de R${valor_final:.2f}")
else:
    print("Código inválido!")
