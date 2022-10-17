#14. Elaborar um algoritmo que lê três valores X, Y, Z e escreva a mensagem: "São múltiplos" ou "Não são múltiplos", se
# os 3 números forem múltiplos entre eles.

x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
if x % y == 0 and x % z == 0:
    print("São múltiplos!")
else:
    print("Não múltiplos!")
