#11. Pergunte ao usuário cinco valores e imprima "SIM" se a soma deles é múltipla de 5 ou é par, mas não é múltipla de 9,
# caso contrário imprima "NÃO".

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
valor3 = int(input("Valor 3: "))
valor4 = int(input("Valor 4: "))
valor5 = int(input("Valor 5: "))
soma = valor1 + valor2 + valor3 + valor4 + valor5
if soma % 5 == 0 or soma % 2 == 0 or soma % 9 != 0:
    print("SIM!")
else:
    print("NÃO!")
