#3. Tendo como dados entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcula o peso ideal para essa
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
