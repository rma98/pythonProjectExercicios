# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

year = int(input('Que ano você que analisar? Coloque 0 para analisar o ano atual: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano de {year} É BISSEXTO!')
else:
    print(f'O ano de {year} NÃO É BISSEXTO!')

# Outras formas de fazer:

# 1
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")

# 2
import calendar

ano = int(input("Digite o ano: "))
if calendar.isleap(ano):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")

# 3
ano = int(input("Digite o ano: "))
bissexto = {True: "é bissexto", False: "não é bissexto"}
print(f"O ano {ano} {bissexto[ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)]}")
