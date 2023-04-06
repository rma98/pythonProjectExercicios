# Escreva um algoritmo que leia o código de um determinado produto e mostre sua classificação. Utilize a seguinte
# tabela como referência:
# -> 1 - Alimento não-perecível
# -> 2, 3 ou 4 - Alimento perecível
# -> 5 ou 6 - Vestuário
# -> 7 - Higiene Pessoal
# -> 8 - até 15 Limpeza e utensílios domésticos
# -> Qualquer outro código - Inválido

codigo = int(input("Código: "))
if codigo == 1:
    print("Alimento não-perecível")
elif codigo == 2 or codigo == 3 or codigo == 4:
    print("Alimento perecível")
elif codigo == 5 or codigo == 6:
    print("Vestuário")
elif codigo == 7:
    print("Higiene Pessoal")
elif codigo == 8 or codigo == 9 or codigo == 10 or codigo == 11 or codigo == 12 or codigo == 13 or codigo == 14 or codigo == 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Inválido!")

# Outras formas de fazer

# 1
codigo = int(input("Código: "))

produtos = {
    1: "Alimento não-perecível",
    2: "Alimento perecível",
    3: "Alimento perecível",
    4: "Alimento perecível",
    5: "Vestuário",
    6: "Vestuário",
    7: "Higiene Pessoal",
    8: "Limpeza e utensílios domésticos",
    9: "Limpeza e utensílios domésticos",
    10: "Limpeza e utensílios domésticos",
    11: "Limpeza e utensílios domésticos",
    12: "Limpeza e utensílios domésticos",
    13: "Limpeza e utensílios domésticos",
    14: "Limpeza e utensílios domésticos",
    15: "Limpeza e utensílios domésticos",
}

if codigo in produtos:
    print(produtos[codigo])
else:
    print("Inválido!")

# 2
codigo = int(input("Código: "))

produtos = [
    "Alimento não-perecível",
    "Alimento perecível",
    "Alimento perecível",
    "Alimento perecível",
    "Vestuário",
    "Vestuário",
    "Higiene Pessoal",
    "Limpeza e utensílios domésticos",
    "Limpeza e utensílios domésticos",
    "Limpeza e utensílios domésticos",
    "Limpeza e utensílios domésticos",
    "Limpeza e utensílios domésticos",
    "Limpeza e utensílios domésticos",
    "Limpeza e utensílios domésticos",
    "Limpeza e utensílios domésticos",
]

if codigo >= 1 and codigo <= len(produtos):
    print(produtos[codigo-1])
else:
    print("Inválido!")

# 3
def tipo_produto(codigo):
    produtos = {
        1: "Alimento não-perecível",
        2: "Alimento perecível",
        3: "Alimento perecível",
        4: "Alimento perecível",
        5: "Vestuário",
        6: "Vestuário",
        7: "Higiene Pessoal",
        8: "Limpeza e utensílios domésticos",
        9: "Limpeza e utensílios domésticos",
        10: "Limpeza e utensílios domésticos",
        11: "Limpeza e utensílios domésticos",
        12: "Limpeza e utensílios domésticos",
        13: "Limpeza e utensílios domésticos",
        14: "Limpeza e utensílios domésticos",
        15: "Limpeza e utensílios domésticos",
    }
    if codigo in produtos:
        return produtos[codigo]
    else:
        return "Inválido!"
codigo = int(input("Código: "))
print(tipo_produto(codigo))
