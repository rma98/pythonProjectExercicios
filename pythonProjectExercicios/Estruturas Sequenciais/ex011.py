#11. Criar um algoritmo que pergunta um número ao usuário e imprime se esse número é múltilplo de 7 e de 3 ao mesmo tempo.

numero = int(input("Número: "))
if numero % 7 == 0 and numero % 3 == 0:
    print(True)
else:
    print(False)
