# Pergunte ao usuário quatro valores e imprima SIM se a média deles é múltiplo de 5 ou múltiplo de 7 ou múltiplo de 9,
# caso contrário imprima NÃO.

valor1 = float(input("VAlor 1:"))
valor2 = float(input("VAlor 2:"))
valor3 = float(input("VAlor 3:"))
valor4 = float(input("VAlor 4:"))
media = (valor1 + valor2 + valor3 + valor4) / 4
if media % 5 == 0 or media % 7 == 0 or media % 9 == 0:
    print("SIM")
else:
    print("NÃO")
print(media)

# Outras formas de fazer

# 1
valores = []
for i in range(4):
    valor = float(input(f"Valor {i+1}: "))
    valores.append(valor)
media = sum(valores) / len(valores)
if media % 5 == 0 or media % 7 == 0 or media % 9 == 0:
    print("SIM")
else:
    print("NÃO")
print(media)

# 2
valores = [float(input(f"Valor {i+1}: ")) for i in range(4)]
media = sum(valores) / len(valores)
if any(media % n == 0 for n in [5, 7, 9]):
    print("SIM")
else:
    print("NÃO")
print(media)

# 3
valores = [float(input(f"Valor {i+1}: ")) for i in range(4)]
media = sum(valores) / len(valores)
divisores = [5, 7, 9]
if any(media % n == 0 for n in divisores):
    print("SIM")
else:
    print("NÃO")
print(media)
