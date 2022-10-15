#22. Imprima o número de dias de um ano. Lembra-se de verificar os anos bissextos.

ano = int(input("Ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} possui 366 dias.")
else:
    print(f"O ano de {ano} possui 365 dias.")
