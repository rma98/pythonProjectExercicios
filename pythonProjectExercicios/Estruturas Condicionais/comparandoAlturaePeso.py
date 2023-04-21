# Peça o nome, a altura e o peso de duas pessoas e apresente o nome da mais pesada e o nome da mais alta.

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

# Outras formas de fazer

# 1
pessoas = []

for i in range(2):
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    pessoas.append([nome, altura, peso])

mais_pesado = max(pessoas, key=lambda x: x[2])
mais_alto = max(pessoas, key=lambda x: x[1])

print(f"A pessoa mais pesada é: {mais_pesado[0]}")
print(f"A pessoa mais alta é: {mais_alto[0]}")

# 2
pessoa1 = {
    "nome": input("Nome: "),
    "altura": float(input("Altura: ")),
    "peso": float(input("Peso: "))
}

pessoa2 = {
    "nome": input("Nome: "),
    "altura": float(input("Altura: ")),
    "peso": float(input("Peso: "))
}

mais_pesado = pessoa1 if pessoa1["peso"] > pessoa2["peso"] else pessoa2
mais_alto = pessoa1 if pessoa1["altura"] > pessoa2["altura"] else pessoa2

print(f"A pessoa mais pesada é: {mais_pesado['nome']}")
print(f"A pessoa mais alta é: {mais_alto['nome']}")
