#54. Faça um programa que defina a largura e a altura de uma parede em metros. Posteriomente, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = 5
altura = 3
print(f"Quantidade de tinta necessária: {largura * altura / 2}L")

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura: '))
alt = float(input('Altura: '))
print(f'Sua parede tem dimensão de {larg}x{alt} e sua área de {larg * alt}m²'
      f'\nPara pintar essa parede, você precisará de {larg * alt / 2:.2f}l de tinta.')
