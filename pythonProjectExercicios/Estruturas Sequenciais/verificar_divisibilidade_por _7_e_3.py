# Criar um algoritmo que pergunta um número ao usuário e imprime se esse número é múltiplo de 7 e de 3 ao mesmo tempo.

numero = int(input("Número: "))
if numero % 7 == 0 and numero % 3 == 0:
    print(True)
else:
    print(False)

#Outras fornas de fazer:

# 1
numero = int(input("Número: "))
print(True) if numero % 7 == 0 and numero % 3 == 0 else print(False)

# 2
def eh_divisivel_por_7_e_3(numero):
    return numero % 7 == 0 and numero % 3 == 0

numero = int(input("Número: "))
print(eh_divisivel_por_7_e_3(numero))

# 3
eh_divisivel_por_7_e_3 = lambda numero: numero % 7 == 0 and numero % 3 == 0

numero = int(input("Número: "))
print(eh_divisivel_por_7_e_3(numero))


# 4
numero = int(input("Número: "))
if (numero & 3 == 0) and (numero & 112 == 0):
    print(True)
else:
    print(False)

# Exemplos do uso de lambada

# 1
soma = lambda x, y: x + y
resultado = soma(3, 5) # resultado é igual a 8

# 2
numeros = [5, 2, 8, 1, 9]
numeros_ordenados = sorted(numeros, key=lambda x: x)
