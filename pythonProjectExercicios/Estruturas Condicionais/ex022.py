#22. Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens de até 200km e R$0.45 para viagens mais longas.

distancia_da_viagem = int(input('Distância: '))
if distancia_da_viagem > 0 and distancia_da_viagem <= 200:
    print(f'O preço da passagem é de R${distancia_da_viagem * 0.50:.2f}')
else:
    print(f'O preço da passagem é de R${distancia_da_viagem * 0.45:.2f}')
