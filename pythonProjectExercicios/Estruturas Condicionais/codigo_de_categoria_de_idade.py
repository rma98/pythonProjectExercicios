# Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# -> 5 até 7 anos - Infantil A
# -> 8 até 10 anos - Infantil B
# -> 11 até 13 anos - Juvenil A
# -> 14 até 17 anos - Juvenil B
# -> Maiores de 18 anos - Adulto

idade = int(input("Idade: "))
if idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade <= 10:
    print("Infantil B")
elif idade >= 11 and idade <= 13:
    print("Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Juvenil B")
elif idade >= 18:
    print("Adulto")
else:
    print("Abaixo dos 5 anos!")

# Outras formas de fazer

# 1
idade = int(input("Idade: "))

categorias = {
    range(5, 8): "Infantil A",
    range(8, 11): "Infantil B",
    range(11, 14): "Juvenil A",
    range(14, 18): "Juvenil B",
    range(18, 200): "Adulto"
}

categoria = None
for faixa_etaria, nome_categoria in categorias.items():
    if idade in faixa_etaria:
        categoria = nome_categoria
        break

if categoria is None:
    print("Abaixo dos 5 anos!")
else:
    print(categoria)

# 2
idade = int(input("Idade: "))

categorias = [
    (5, 7, "Infantil A"),
    (8, 10, "Infantil B"),
    (11, 13, "Juvenil A"),
    (14, 17, "Juvenil B"),
    (18, None, "Adulto")
]

categoria = None
for faixa_etaria in categorias:
    if faixa_etaria[1] is None:
        if idade >= faixa_etaria[0]:
            categoria = faixa_etaria[2]
            break
    elif idade >= faixa_etaria[0] and idade <= faixa_etaria[1]:
        categoria = faixa_etaria[2]
        break

if categoria is None:
    print("Abaixo dos 5 anos!")
else:
    print(categoria)
