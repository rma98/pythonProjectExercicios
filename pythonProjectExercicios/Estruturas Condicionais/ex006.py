#6. Imprima o número de dias de um ano. Lembra-se de verificar os anos bissextos (que são os anos múltiplos de 4).

from datetime import date

ano = int(input("Ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} É bissexto, e possui 366 dias!")
else:
    print(f"O ano de {ano} Não é bissexto, e possui 365 dias!")

#6.1 Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

year = int(input('Que ano você que analisar? Coloque 0 para analisar o ano atual: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano de {year} É BISSEXTO!')
else:
    print(f'O ano de {year} NÃO É BISSEXTO!')
