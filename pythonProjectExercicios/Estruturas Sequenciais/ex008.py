#8. Criar um algoritmo que pergunta dois números ao usuário e informa a soma deles é maior que a subtração deles.

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
if valor1 + valor2 > valor1 - valor2:
    print(True)
else:
    print(False)
