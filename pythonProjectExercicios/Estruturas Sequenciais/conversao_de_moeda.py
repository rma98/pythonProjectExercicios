# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ = 3,27

dinheiro_na_carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Você pode comprar US${dinheiro_na_carteira / 3.27:.2f} Dólares.')

# Outras formas de fazer

# 1
reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolares = reais / 3.27
print(f'Você pode comprar US${dolares:.2f} dólares.')

# 2
TAXA_DE_CAMBIO = 3.27
reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolares = round(reais / TAXA_DE_CAMBIO, 2)
print(f'Você pode comprar US${dolares} dólares.')

# 3
TAXA_DE_CAMBIO = 3.27
reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolares = reais / TAXA_DE_CAMBIO
print('Você pode comprar US$%.2f dólares.' % dolares)
