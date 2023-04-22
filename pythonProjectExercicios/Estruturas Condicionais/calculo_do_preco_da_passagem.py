# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens de até 200km e R$0.45 para viagens mais longas.

distancia_da_viagem = int(input('Distância: '))
if distancia_da_viagem > 0 and distancia_da_viagem <= 200:
    print(f'O preço da passagem é de R${distancia_da_viagem * 0.50:.2f}')
else:
    print(f'O preço da passagem é de R${distancia_da_viagem * 0.45:.2f}')

# Outras formas de fazer

# 1
distancia_da_viagem = int(input('Distância: '))
preco = distancia_da_viagem * 0.50 if distancia_da_viagem <= 200 else distancia_da_viagem * 0.45
print(f'O preço da passagem é de R${preco:.2f}')

# 2
distancia_da_viagem = int(input('Distância: '))
tabela_de_precos = {0: 0, 200: 0.50, float('inf'): 0.45}
preco_por_km = next(v for k, v in tabela_de_precos.items() if distancia_da_viagem <= k)
preco = distancia_da_viagem * preco_por_km
print(f'O preço da passagem é de R${preco:.2f}')

# 3
def calcular_preco(distancia):
    if distancia <= 200:
        return distancia * 0.50
    else:
        return distancia * 0.45

distancia_da_viagem = int(input('Distância: '))
preco = calcular_preco(distancia_da_viagem)
print(f'O preço da passagem é de R${preco:.2f}')
