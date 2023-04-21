# Pergunte ao usuário quatro valores e imprima SIM se a média deles é múltiplo de 5 ou múltiplo de 7 ou múltiplo de 9,
# caso contrário imprima NÃO.

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
valor3 = int(input("Valor 3: "))
valor4 = int(input("Valor 4: "))
media = (valor1 + valor2 + valor3 + valor4) / 4
if media % 5 == 0 or media % 7 == 0 or media % 9 == 0:
    print("SIM!")
else:
    print("NÃO!")

# Outras formas de fazer

# 1
valores = []
for i in range(4):
    valor = int(input(f"Valor {i+1}: "))
    valores.append(valor)

media = sum(valores) / 4

if media % 5 == 0 or media % 7 == 0 or media % 9 == 0:
    print("SIM!")
else:
    print("NÃO!")

# 2
valores = [int(input(f"Valor {i+1}: ")) for i in range(4)]

media = sum(valores) / 4

if media % 5 == 0 or media % 7 == 0 or media % 9 == 0:
    print("SIM!")
else:
    print("NÃO!")

