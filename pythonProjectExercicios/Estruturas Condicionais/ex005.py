#5. Leia uma letra do alfabeto e mostrar uma mensagem: se é vogal ou consoante.

alfabeto = input("Alfabeto: ").upper()
if alfabeto == "A" or alfabeto == "E" or alfabeto == "I" or alfabeto == "O" or alfabeto == "U":
    print("Vogal!")
else:
    print("Alfabeto!")
