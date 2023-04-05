# Elaborar um algoritmo que lê três valores X, Y, Z e escreva a mensagem: "São múltiplos"  ou "Não são múltiplos",
# se os três 3 números forem múltiplos entre eles.

x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
if x % y == 0 and x % z == 0:
    print("São múltiplos!")
else:
    print("Não são múltiplos!")

# Outras formas de fazer

# 1
x = int(input("X: "))
y = int(input("Y: "))
if x // y * y == x:
    print("São múltiplos!")
else:
    print("Não são múltiplos!")

# 2
def sao_multiplos(x, y, z):
    return x % y == 0 and x % z == 0

x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
if sao_multiplos(x, y, z):
    print("São múltiplos!")
else:
    print("Não são múltiplos!")

# 3
x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
print("São múltiplos!" if x % y == 0 and x % z == 0 else "Não são múltiplos!")
