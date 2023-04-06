# Faça um programa que defina a largura e a altura de uma parede em metros. Posteriormente, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = 5
altura = 3
print(f"Quantidade de tinta necessária: {largura * altura / 2}L")

# Outras formas de fazer

# 1
# Definindo a largura e altura da parede
largura = 5
altura = 3

# Calculando a área da parede
area = largura * altura / 2

# Exibindo o resultado
print("Quantidade de tinta necessária: " + str(area) + "L")

# 2
largura = 5
altura = 3
area = largura * altura / 2
mensagem = "Quantidade de tinta necessária: {}L".format(area)
print(mensagem)

# 3
largura = 5
altura = 3
area = largura * altura / 2
print(f"Quantidade de tinta necessária: {area}L")
