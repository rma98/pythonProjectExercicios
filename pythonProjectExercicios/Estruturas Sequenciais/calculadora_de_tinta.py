# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura: '))
alt = float(input('Altura: '))
print(f'Sua parede tem dimensão de {larg}x{alt} e sua área de {larg * alt}m²'
      f'\nPara pintar essa parede, você precisará de {larg * alt / 2:.2f}l de tinta.')

# Outras formas de fazer

# 1
# pede a largura da parede
largura = float(input('Informe a largura da parede em metros: '))

# pede a altura da parede
altura = float(input('Informe a altura da parede em metros: '))

# calcula a área da parede
area = largura * altura

# calcula a quantidade de tinta necessária para pintar a parede
tinta = area / 2

# exibe as informações na tela
print(f'A sua parede tem {largura:.2f} metros de largura e {altura:.2f} metros de altura, '
      f'com uma área total de {area:.2f} metros quadrados.\n'
      f'Você precisará de {tinta:.2f} litros de tinta para pintar toda a parede.')
