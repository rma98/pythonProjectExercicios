#1. Peça o nome, a altura e o peso de duas pessoas e aprensente o nome da mais pesada e o nome da mais alta.

nome = input("Nome: ")
altura = float(input("Altura: "))
peso = float(input("Peso: "))
nome2 = input("Nome: ")
altura2 = float(input("Altura: "))
peso2 = float(input("Peso: "))

if peso > peso2:
    print(f"A pessoa mais pesada é: {nome}")
elif peso < peso2:
    print(f"A pessoa mais pesada é: {nome2}")
else:
    print(f"Pesos iguais!")
if altura > altura2:
    print(f"A pessoa mais alta é: {nome}")
elif altura < altura2:
    print(f"A pessoa mais alta é: {nome2}")
else:
    print(f"Alturas iguais!")
