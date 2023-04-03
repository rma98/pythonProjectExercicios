# Tendo como dados de entrada a altura e o sexo de uma pessoa construa um algoritmo que calcula o peso ideal para
# essa pessoa utilizando as seguintes fórmulas:
# -> Para homens (72,7 * altura) - 58
# -> Para mulheres (62,1 * altura) - 44,7

altura = float(input("Altura: "))
sexo = input("Sexo M ou F:").upper()
if sexo == "M":
    print(f"peso ideal para homens: {(72.7 * altura)- 58:.2f}")
elif sexo == "F":
    print(f"Peso ideal para mulheres: {(62.1 * altura) - 44.7:.2f}")

# Outras formas de fazer

# 1
altura = float(input("Altura: "))
sexo = input("Sexo M ou F: ").upper()

if sexo == "M":
    peso_ideal = 72.7 * altura - 58
    print(f"Peso ideal para homens: {peso_ideal:.2f}")
elif sexo == "F":
    peso_ideal = 62.1 * altura - 44.7
    print(f"Peso ideal para mulheres: {peso_ideal:.2f}")
else:
    print("Sexo inválido.")

# 2
altura = float(input("Altura: "))
sexo = input("Sexo M ou F: ").upper()

peso_ideal = (72.7 * altura - 58) if sexo == "M" else (62.1 * altura - 44.7) if sexo == "F" else None

if peso_ideal is not None:
    print(f"Peso ideal para {sexo}: {peso_ideal:.2f}")
else:
    print("Sexo inválido.")

# 3
# import numpy as np

# altura = float(input("Altura: "))
# sexo = input("Sexo M ou F: ").upper()

# if sexo == "M":
#     peso_ideal = np.multiply(altura, 22.0) - 44.0
#     print(f"Peso ideal para homens: {peso_ideal:.2f}")
# elif sexo == "F":
#     peso_ideal = np.multiply(altura, 22.0) - 49.0
#     print(f"Peso ideal para mulheres: {peso_ideal:.2f}")
# else:
#     print("Sexo inválido.")
