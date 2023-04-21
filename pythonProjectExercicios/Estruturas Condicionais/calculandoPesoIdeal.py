# Tendo como dados entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcula o peso ideal para essa
# pessoa, utilizando as seguintes fórmulas:
# -> . Para homens (72,7 * altura) - 58
# -> Para mulheres (62,1 * altura) - 44,7

altura = float(input("Altura: "))
sexo = int(input("1- Masculino\n2- Feminino\n: "))
if sexo == 1:
    print(f"Peso ideal: {(72.7 * altura) - 58:.2f}")
elif sexo == 2:
    print(f"Peso ideal: {(62.1 * altura) - 44.7:.2f}")
else:
    print("Inválido!")

# Outras formas de fazer

# 1
altura = float(input("Altura: "))
sexo = int(input("1- Masculino\n2- Feminino\n: "))

formulas = {1: lambda h: 72.7 * h - 58, 2: lambda h: 62.1 * h - 44.7}

if sexo in formulas:
    peso_ideal = formulas[sexo](altura)
    print(f"Peso ideal: {peso_ideal:.2f}")
else:
    print("Inválido!")

# 2
altura = float(input("Altura: "))
sexo = int(input("1- Masculino\n2- Feminino\n: "))

formulas = [(72.7, -58), (62.1, -44.7)]

if sexo == 1 or sexo == 2:
    a, b = formulas[sexo - 1]
    peso_ideal = a * altura + b
    print(f"Peso ideal: {peso_ideal:.2f}")
else:
    print("Inválido!")

# 3
altura = float(input("Altura: "))
sexo = int(input("1- Masculino\n2- Feminino\n: "))

def peso_ideal_masculino(h):
    return 72.7 * h - 58

def peso_ideal_feminino(h):
    return 62.1 * h - 44.7

if sexo == 1:
    peso_ideal = peso_ideal_masculino(altura)
    print(f"Peso ideal: {peso_ideal:.2f}")
elif sexo == 2:
    peso_ideal = peso_ideal_feminino(altura)
    print(f"Peso ideal: {peso_ideal:.2f}")
else:
    print("Inválido!")
