# Criar um algoritmo que pergunta um número ao usuário e imprime se esse número não é múltiplo de 7.

num = int(input("Número: "))
if num % 7 != 0:
    print(True)
else:
    print(False)

# Outras formas de fazer

# 1
num = int(input("Número: "))
print(True) if num % 7 == 0 else print(False)

# 2
def is_multiple_of_7(num):
    return num % 7 == 0

num = int(input("Número: "))
print(is_multiple_of_7(num))
