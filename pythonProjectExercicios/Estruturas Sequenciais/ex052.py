# Faça um programa que receba uma hora (uma variável para e outra para minutos), calcule e moostre:
# -> a. a hora digitada convertida em minutos;
# -> b. o total de minutos, ou seja, os minutos digitados mais a conversão anterior;
# -> c. o total de minutos convertidos em segundos.

hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
convertendo = hora * 60
total_Minutos = convertendo + minuto
print(f"Hora digitada convertida em minutos: {convertendo}min\nTotal de minutos: {total_Minutos}min"
      f"\nO total de minutos convertido em segundos: {total_Minutos * 60}s")
