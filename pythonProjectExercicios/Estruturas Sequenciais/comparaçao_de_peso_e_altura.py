# Peça o nome, a altura e o peso de duas pessoas e apresente o nome da mais pesada e o nome da mais alta.

nome = input("Digite seu nome: ")
altura = float(input("Altura: "))
peso = float(input("Peso: "))

nome2 = input("Digite seu nome: ")
altura2 = float(input("Altura: "))
peso2 = float(input("Peso: "))

if peso > peso2:
    print(f"Mais pesada: {nome}")
elif peso < peso2:
    print(f"Mais pesada: {nome2}")
else:
    print(f"Pesos iguais!")
if altura > altura2:
    print(f"Mais ala: {nome}")
elif altura < altura2:
    print(f"Mais alta: {nome2}")
else:
    print(f"Alturas iguais!")

# Outras formas de fazer

# 1
pessoas = []

for i in range(2):
    nome = input("Digite o nome da pessoa {}: ".format(i+1))
    altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))
    peso = float(input("Digite o peso da pessoa {}: ".format(i+1)))
    pessoas.append({"nome": nome, "altura": altura, "peso": peso})

if pessoas[0]["peso"] > pessoas[1]["peso"]:
    print("A pessoa mais pesada é:", pessoas[0]["nome"])
elif pessoas[0]["peso"] < pessoas[1]["peso"]:
    print("A pessoa mais pesada é:", pessoas[1]["nome"])
else:
    print("As pessoas têm o mesmo peso!")

if pessoas[0]["altura"] > pessoas[1]["altura"]:
    print("A pessoa mais alta é:", pessoas[0]["nome"])
elif pessoas[0]["altura"] < pessoas[1]["altura"]:
    print("A pessoa mais alta é:", pessoas[1]["nome"])
else:
    print("As pessoas têm a mesma altura!")
