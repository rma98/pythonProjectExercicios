# Determine o número de dias que uma pessoa já viveu até a data de HOJE (03/04/2018). Considere que um mês tenha 30 doas.

idade = int(input("Idade: "))
dia, mes, ano = 3, 4, 2018
print(f"{idade * ano * mes} dias")

# Outras formas de fazer

# 1
idade = int(input("Idade: "))
DIAS_POR_ANO = 365
MESES = 12
dias = idade * DIAS_POR_ANO * MESES
print(f"{dias} dias")

# 2
from datetime import date

data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_nasc.split("/"))
hoje = date.today()
dias = (hoje - date(ano, mes, dia)).days
print(f"{dias} dias")

# 3
idade = int(input("Idade: "))
dias_por_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
dias = idade * sum(dias_por_mes.values())
print(f"{dias} dias")
