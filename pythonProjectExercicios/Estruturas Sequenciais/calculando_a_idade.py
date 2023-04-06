# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# -> a. a idade dessa pessoa em anos;
# -> b. a idade dessa pessoa em meses;
# -> c. a idade dessa pessoa em dia;
# -> d. a idade dessa pessoa em semanas.

from datetime import date

ano_Nasc = int(input("Ano de Nascimento: "))
ano_Atual = date.today().year
idade = ano_Atual - ano_Nasc
mes = idade * 12
dia = idade * 365
semana = mes * 4
print(f"a idade em anos -> {idade} anos\na idade em meses -> {mes} meses\na idade em dias -> {dia} dias"
      f"\na idade em semanas -> {semana} semanas")

# Outras formas de fazer

# 1
# from dateutil.relativedelta import relativedelta
# from datetime import date

# ano_Nasc = int(input("Ano de Nascimento: "))
# data_Nasc = date(ano_Nasc, 1, 1)
# data_Atual = date.today()
# idade = relativedelta(data_Atual, data_Nasc)
# print(f"a idade em anos -> {idade.years} anos\na idade em meses -> {idade.months} meses\na idade em dias -> {idade.days} dias"
#       f"\na idade em semanas -> {idade.weeks} semanas")

# 2
# import arrow

# ano_Nasc = int(input("Ano de Nascimento: "))
# data_Nasc = arrow.get(ano_Nasc, 1, 1)
# data_Atual = arrow.now()
# idade = data_Atual - data_Nasc
# print(f"a idade em anos -> {idade.years} anos\na idade em meses -> {idade.months} meses\na idade em dias -> {idade.days} dias"
#       f"\na idade em semanas -> {idade.weeks} semanas")

# 3
# import pendulum

# ano_Nasc = int(input("Ano de Nascimento: "))
# data_Nasc = pendulum.datetime(ano_Nasc, 1, 1)
# data_Atual = pendulum.now()
# idade = data_Atual - data_Nasc
# print(f"a idade em anos -> {idade.years} anos\na idade em meses -> {idade.months} meses\na idade em dias -> {idade.days} dias"
#      f"\na idade em semanas -> {idade.weeks} semanas")
