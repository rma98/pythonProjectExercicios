#32. Imprima um número de minutos de um ano. Lembra-se de verificar os anos bissextos (que são os anos mútiplos de 4).

ano = int(input("Ano: "))
um_Dia = 24
uma_Hora = 60
minutos_Em_Um_Dia = um_Dia * uma_Hora
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"No ano Bissexto, 1 ano possui {minutos_Em_Um_Dia * 366} minutos.")
else:
    print(f"Um ano possui {minutos_Em_Um_Dia * 365} minutos.")
