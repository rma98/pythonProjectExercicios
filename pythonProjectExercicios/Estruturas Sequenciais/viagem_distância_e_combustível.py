# Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz
# 12km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável TEMPO) e a velocidade média
# (variável VELOCIDADE) durante a viagem. Desta forma, será possível obter a distância percorrida com a fórmula
# DISTÂNCIA = TEMPO * VELOCIDADE. A partir do valor da distância, basta calcular a quantidade de litros de
# combustível utilizada na viagem com a fórmula LITROS = distância / 12. O programa deve apresentar os valores da
#velocidade média, tempo da viagem, distância percorrida e a quantidade de litros utilizada na viagem.

tempo = int(input("Tempo gasto: "))
velocidade = int(input("Velocidade: "))
distancia = tempo * velocidade
litros = distancia / 12
print(f"Velocidade Média: {velocidade}km\n"
      f"Tempo da Viagem: {tempo}\n"
      f"Distância Pecorrida: {distancia}\n"
      f"Quantidade de Litros: {litros:.2f}")

# Outras formas de fazer

# 1
MEDIA_CONSUMO = 12

tempo = int(input("Tempo gasto: "))
velocidade = int(input("Velocidade: "))
distancia = tempo * velocidade
litros = distancia / MEDIA_CONSUMO

print(f"Velocidade Média: {velocidade}km\n"
      f"Tempo da Viagem: {tempo}\n"
      f"Distância Pecorrida: {distancia}\n"
      f"Quantidade de Litros: {litros:.2f}")

# 2
MEDIA_CONSUMO = 12

tempo = int(input("Tempo gasto: "))
distancia = int(input("Distância percorrida: "))
velocidade = distancia / tempo
litros = distancia / MEDIA_CONSUMO

print(f"Velocidade Média: {velocidade}km\n"
      f"Tempo da Viagem: {tempo}\n"
      f"Distância Pecorrida: {distancia}\n"
      f"Quantidade de Litros: {litros:.2f}")

# 3
def calcular_distancia(tempo, velocidade):
    return tempo * velocidade

def calcular_litros(distancia):
    return distancia / 12

tempo = int(input("Tempo gasto: "))
velocidade = int(input("Velocidade: "))
distancia = calcular_distancia(tempo, velocidade)
litros = calcular_litros(distancia)

print(f"Velocidade Média: {velocidade}km\n"
      f"Tempo da Viagem: {tempo}\n"
      f"Distância Pecorrida: {distancia}\n"
      f"Quantidade de Litros: {litros:.2f}")
