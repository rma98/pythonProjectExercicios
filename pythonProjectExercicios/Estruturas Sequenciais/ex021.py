#21. Leia uma letra do alfabeto e mostrar uma mensagem: se é vogal ou consoante.

letra_Alfabeto = input("Letra do alfabeto: ").upper()
if letra_Alfabeto == "A" or letra_Alfabeto == "E" or letra_Alfabeto == "I" or letra_Alfabeto == "O" or letra_Alfabeto == "U":
    print("Vogal")
else:
    print("Consoante")
