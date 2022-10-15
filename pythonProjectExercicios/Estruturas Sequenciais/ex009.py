#9. Criar um algoritmo que pergunte o ano de nascimento do usuário e imprima se ee é de menor.

from datetime import date

ano_Nasc = int(input("Ano de Nascimento:"))
if date.today().year - ano_Nasc >= 18:
    print(True)
else:
    print(False)
