#1. Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def titulo(txt):
    print(txt)
    print('-' * 20)


def area(larg, compr):
    ar_terreno = larg * compr
    print(f'A área do terreno \033[32m{larg}\033[mx\033[33m{compr}\033[m é de \033[34m{ar_terreno}m²\033[34m')


titulo('Controle de Terrenos')

largura = float(input(f'\033[32mLargura (m): \033[m'))
comprimento = float(input('\033[33mComprimento (m): \033[m'))

area(largura, comprimento)
