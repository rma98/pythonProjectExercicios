#6. Imprima o número de dias de um ano. Lembra-se de verificar os anos bissextos (que são os anos múltiplos de 4).

ano = int(input("Ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("É bissexto, 366 dias!")
else:
    print("Não é bissexto, 365 dias!")
