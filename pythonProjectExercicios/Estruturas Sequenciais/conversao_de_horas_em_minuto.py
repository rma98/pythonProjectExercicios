# Faça um programa que receba uma hora (uma variável para e outra para minutos), calcule e mostre:
# -> a. A hora digitada convertida em minutos;
# -> b. O total de minutos, ou seja, os minutos digitados mais a conversão anterior;
# -> c. O total de minutos convertidos em segundos.

hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
convertendo = hora * 60
total_Minutos = convertendo + minuto
print(f"Hora digitada convertida em minutos: {convertendo}min\nTotal de minutos: {total_Minutos}min"
      f"\nO total de minutos convertido em segundos: {total_Minutos * 60}s")

# Outras formas de fazer

# 1
hora, minuto = int(input("Hora: ")), int(input("Minuto: "))
total_minutos = hora * 60 + minuto
print(f"{hora}h{minuto:02d}min equivalem a {total_minutos} minutos e {total_minutos * 60} segundos.")

# 2
def converter_para_minutos(horas, minutos):
    return horas * 60 + minutos

def converter_para_segundos(minutos):
    return minutos * 60

hora = int(input("Hora: "))
minuto = int(input("Minuto: "))

total_minutos = converter_para_minutos(hora, minuto)
total_segundos = converter_para_segundos(total_minutos)

print(f"{hora}h{minuto:02d}min equivalem a {total_minutos} minutos e {total_segundos} segundos.")


# 3
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
total_minutos = hora * 60 + minuto
total_segundos = total_minutos * 60
print(f"{hora}h{minuto:02d}min equivalem a {total_minutos} minutos e {total_segundos} segundos.")

# 4
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))

total_minutos = hora * 60 + minuto
total_segundos = total_minutos * 60

mensagem = f"{hora}h{minuto:02d}min equivalem a {total_minutos} minutos e {total_segundos} segundos."
print(mensagem)
