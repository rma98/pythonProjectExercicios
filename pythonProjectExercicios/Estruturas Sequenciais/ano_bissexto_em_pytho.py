# Imprima um número de minutos de um ano. Lembra-se de verificar os anos bissextos (que são os anos múltiplos de 4).

ano = int(input("Ano: "))
um_Dia = 24
uma_Hora = 60
minutos_Em_Um_Dia = um_Dia * uma_Hora
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"No ano Bissexto, 1 ano possui {minutos_Em_Um_Dia * 366} minutos.")
else:
    print(f"Um ano possui {minutos_Em_Um_Dia * 365} minutos.")

# Outras formas de fazer

# 1
ano = int(input("Ano: "))
um_Dia = 24
uma_Hora = 60
minutos_Em_Um_Dia = um_Dia * uma_Hora
bissexto = minutos_Em_Um_Dia * 366
normal = minutos_Em_Um_Dia * 365
print(f"No ano Bissexto, 1 ano possui {bissexto} minutos." if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else f"Um ano possui {normal} minutos.")

# 2
def minutos_em_ano(ano):
    um_Dia = 24
    uma_Hora = 60
    minutos_Em_Um_Dia = um_Dia * uma_Hora
    return minutos_Em_Um_Dia * 366 if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else minutos_Em_Um_Dia * 365

ano = int(input("Ano: "))
print(f"No ano Bissexto, 1 ano possui {minutos_em_ano(ano)} minutos." if minutos_em_ano(ano) == minutos_Em_Um_Dia * 366 else f"Um ano possui {minutos_em_ano(ano)} minutos.")

# 3
try:
    ano = int(input("Ano: "))
    um_Dia = 24
    uma_Hora = 60
    minutos_Em_Um_Dia = um_Dia * uma_Hora
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"No ano Bissexto, 1 ano possui {minutos_Em_Um_Dia * 366} minutos.")
    else:
        print(f"Um ano possui {minutos_Em_Um_Dia * 365} minutos.")
except ValueError:
    print("Por favor, insira um ano válido.")
