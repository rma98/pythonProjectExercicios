# Imprima o número de dias de um ano. Lembra-se de verificar os anos bissextos (que são os anos múltiplos de 4).

from datetime import date

ano = int(input("Ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} É bissexto, e possui 366 dias!")
else:
    print(f"O ano de {ano} Não é bissexto, e possui 365 dias!")

# Outras formas de fazer

# 1
import calendar

ano = int(input("Ano: "))
if calendar.isleap(ano):
    print(f"O ano de {ano} É bissexto, e possui 366 dias!")
else:
    print(f"O ano de {ano} Não é bissexto, e possui 365 dias!")

# 2
from datetime import date, timedelta

ano = int(input("Ano: "))
data_inicio = date(ano, 1, 1)
data_fim = date(ano, 12, 31)
dias_do_ano = (data_fim - data_inicio).days + 1
if dias_do_ano == 366:
    print(f"O ano de {ano} É bissexto, e possui 366 dias!")
else:
    print(f"O ano de {ano} Não é bissexto, e possui 365 dias!")
