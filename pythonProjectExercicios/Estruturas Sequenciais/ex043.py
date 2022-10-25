#43. Faça um programa que recebe o peso de uma pesa em quilos, calcule e mostre esse peso em gramas.

peso = int(input("Peso: "))
print(f"{peso}kg convertido em gramas é: {peso * 1000}g")

#43.1 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ = 3,27

dinheiro_na_carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Você pode comprar US${dinheiro_na_carteira / 3.27:.2f} Dólares.')
