#17. Peça o nome, a altura e o peso de duas pessoas e apresente o nome da mais pesada e o nome da mais alta.

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
