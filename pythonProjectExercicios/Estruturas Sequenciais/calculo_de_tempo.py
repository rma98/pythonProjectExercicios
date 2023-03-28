# Escreva um programa que calcule o tempo de uma de carro. Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.

distanica_Pecorrer = float(input("Distância a percorrer: "))
velocidade_Media = float(input("Velocidade Média: "))
print(f"Tempo da viagem: {distanica_Pecorrer/velocidade_Media}")

# Outras formas de fazer

def calcular_tempo_viagem(distancia, velocidade):
    tempo = distancia / velocidade
    return tempo

distancia = float(input("Distância a percorrer: "))
velocidade_media = float(input("Velocidade média: "))

tempo_viagem = calcular_tempo_viagem(distancia, velocidade_media)

print(f"Tempo da viagem: {tempo_viagem}")
