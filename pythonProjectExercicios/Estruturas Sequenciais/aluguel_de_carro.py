# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por
# dia e R$0,15 por KM rodado.

qtde_Km_Pecorrido = int(input("Quantidade de KM percorrido: "))
qtde_Dia = int(input("Quantidade de dias em que o carro foi alugado: "))
print(f"Preço a pagar: {qtde_Km_Pecorrido * 0.15 + qtde_Dia * 60:.2f}")

# Outras formas de fazer

# 1
qtde_Km_Pecorrido = int(input("Quantidade de KM percorrido: "))
qtde_Dia = int(input("Quantidade de dias em que o carro foi alugado: "))

preco_Km = 0.15
preco_Dia = 60

valor_Km = qtde_Km_Pecorrido * preco_Km
valor_Dia = qtde_Dia * preco_Dia
total = valor_Km + valor_Dia

print(f"Preço a pagar: {total:.2f}")

# 2
qtde_Km_Pecorrido = int(input("Quantidade de KM percorrido: "))
qtde_Dia = int(input("Quantidade de dias em que o carro foi alugado: "))

preco_Km = 0.15
preco_Dia = 60

total = qtde_Km_Pecorrido * preco_Km + qtde_Dia * preco_Dia

print(f"Preço a pagar: {total:.2f}")

# 3
qtde_Km_Pecorrido = int(input("Quantidade de KM percorrido: "))
qtde_Dia = int(input("Quantidade de dias em que o carro foi alugado: "))

total = qtde_Km_Pecorrido * 0.15 + qtde_Dia * 60

print(f"Preço a pagar: {total:.2f}")

# 4
def calcular_preco(qtde_Km_Pecorrido, qtde_Dia):
    preco_Km = 0.15
    preco_Dia = 60
    valor_Km = qtde_Km_Pecorrido * preco_Km
    valor_Dia = qtde_Dia * preco_Dia
    total = valor_Km + valor_Dia
    return total

qtde_Km_Pecorrido = int(input("Quantidade de KM percorrido: "))
qtde_Dia = int(input("Quantidade de dias em que o carro foi alugado: "))

preco_total = calcular_preco(qtde_Km_Pecorrido, qtde_Dia)

print(f"Preço a pagar: {preco_total:.2f}")
