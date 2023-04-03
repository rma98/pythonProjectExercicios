# Leia uma letra do alfabeto e mostrar uma mensagem: se é vogal ou consoante.

letra_Alfabeto = input("Letra do alfabeto: ").upper()
if letra_Alfabeto == "A" or letra_Alfabeto == "E" or letra_Alfabeto == "I" or letra_Alfabeto == "O" or letra_Alfabeto == "U":
    print("Vogal")
else:
    print("Consoante")

# Outras formas de fazer

# 1
vogais = ['A', 'E', 'I', 'O', 'U']
letra_alfabeto = input("Letra do alfabeto: ").upper()
if letra_alfabeto in vogais:
    print("Vogal")
else:
    print("Consoante")

# 2
import re
letra_alfabeto = input("Letra do alfabeto: ").upper()
if re.match("[AEIOU]", letra_alfabeto):
    print("Vogal")
else:
    print("Consoante")
