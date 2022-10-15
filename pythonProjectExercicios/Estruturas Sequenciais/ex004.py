#4. Escreva um programa que pergunte a quantidade de KM pecorridos por um carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por
# dia e R$0,15 por KM rodado.

qtde_Km_Pecorrido = int(input("Quantidade de KM pecorrido: "))
qtde_Dia = int(input("Quantidade de dias em que o carro foi alugado: "))
print(f"Preço a pagar: {qtde_Km_Pecorrido * 0.15 + qtde_Dia * 60:.2f}")
