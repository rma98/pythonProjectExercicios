# Leia uma letra do alfabeto e mostrar uma mensagem: se é vogal ou consoante.

alfabeto = input("Alfabeto: ").upper()
if alfabeto == "A" or alfabeto == "E" or alfabeto == "I" or alfabeto == "O" or alfabeto == "U":
    print("Vogal!")
else:
    print("Alfabeto!")

# Outras formas de fazer

# 1
alfabeto = input("Alfabeto: ").upper()
vogais = "AEIOU"
if alfabeto in vogais:
    print("Vogal!")
else:
    print("Alfabeto!")

# 2
alfabeto = input("Alfabeto: ").upper()
if alfabeto.isalpha():
    if alfabeto in ["A", "E", "I", "O", "U"]:
        print("Vogal!")
    else:
        print("Consoante!")
else:
    print("Não é uma letra do alfabeto!")

# 3
alfabeto = input("Alfabeto: ").upper()
vogais = {"A", "E", "I", "O", "U"}
print("Vogal!" if alfabeto in vogais else "Consoante!" if alfabeto.isalpha() else "Não é uma letra do alfabeto!")
