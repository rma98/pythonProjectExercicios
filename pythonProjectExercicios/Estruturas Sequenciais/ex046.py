#46. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# -> a. a idade dessa pessoa em anos;
# -> b. a idade dessa pessoa em meses;
# -> c. a idade dessa pessoas em dias;
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
