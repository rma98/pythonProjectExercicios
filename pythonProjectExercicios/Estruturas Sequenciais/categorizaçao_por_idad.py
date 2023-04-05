# Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# -> 5 até 7 anos = Infantil A
# -> 8 até 10 anos = Infantil B
# -> 11 até 13 anos = Juvenil A
# -> 14 até 17 anos = Juvenil B
# -> Maiores de 18 anos = Adulto

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
    print("Abaixo dos 5 anos de idade")

# Outras formas de fazer

# 1
categorias = {
    (5, 7): "Infantil A",
    (8, 10): "Infantil B",
    (11, 13): "Juvenil A",
    (14, 17): "Juvenil B",
    (18, float("inf")): "Adulto"
}

idade = int(input("Idade: "))

for faixa_etaria, categoria in categorias.items():
    if idade >= faixa_etaria[0] and idade <= faixa_etaria[1]:
        print(categoria)
        break
else:
    print("Abaixo dos 5 anos de idade")

# 2
idade = int(input("Idade: "))

categoria = "Infantil A" if idade >= 5 and idade <= 7 \
            else "Infantil B" if idade >= 8 and idade <= 10 \
            else "Juvenil A" if idade >= 11 and idade <= 13 \
            else "Juvenil B" if idade >= 14 and idade <= 17 \
            else "Adulto" if idade >= 18 \
            else "Abaixo dos 5 anos de idade"

print(categoria)

# 3
categorias = [
    (5, 7, "Infantil A"),
    (8, 10, "Infantil B"),
    (11, 13, "Juvenil A"),
    (14, 17, "Juvenil B"),
    (18, float("inf"), "Adulto")
]

idade = int(input("Idade: "))

categoria = next((categoria for faixa_etaria in categorias \
                  if idade >= faixa_etaria[0] and idade <= faixa_etaria[1]), \
                 "Abaixo dos 5 anos de idade")

print(categoria)
