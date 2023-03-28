# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Temperatura em graus ºC: '))
print(f'A temperatura {temp}ºC convertida em graus Fahrenheit: {(temp * 9/5) +32}ºF')

# Outras formas de fazer

# 1
celsius = float(input("Temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperatura em graus Fahrenheit:", fahrenheit)

# 2
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Temperatura em graus Celsius: "))
print("Temperatura em graus Fahrenheit:", celsius_para_fahrenheit(temp))

# 3
temp = float(input("Temperatura em graus Celsius: "))
print("Temperatura em graus Fahrenheit:", temp * 1.8 + 32)
