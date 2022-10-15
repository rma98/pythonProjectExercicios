#19. Tendo como dados de entrada a altura e o sexo de uma pessoa construa um algoritmo que calcula o peso ideal para
# essa pessoa utilizando as seguintes fórmulas:
# -> Para homens (72,7 * altura) - 58
# -> Para mulheres (62,1 * altura) - 44,7

altura = float(input("Altura: "))
sexo = input("Sexo M ou F:").upper()
if sexo == "M":
    print(f"peso ideal para homens: {(72.7 * altura)- 58:.2f}")
elif sexo == "F":
    print(f"Peso ideal para mulheres: {(62.1 * altura) - 44.7:.2f}")
