#2. Efetuar o cáclculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz
# 12km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável TEMPO) e a velocidade média
# (variável VELOCIDADE) durante a viagem. Desta forma, será possível obter a distância pecorrida com a fórmula
# DISTÂNCIA = TEMPO * VELOCIDADE. A partir do valor das distância, basta calcular a quantidade de litros de
# combustível utilizada na viagem com a fórmula LITROS = distância / 12. O programa deve apresentar os valores da
#velocidade média, tempo da viagem, distância pecorrida e a quantidade de litros utilizada na viagem.

tempo = int(input("Tempo gasto: "))
velocidade = int(input("Velocidade: "))
distancia = tempo * velocidade
litros = distancia / 12
print(f"Velocidade Média: {velocidade}km\n"
      f"Tempo da Viagem: {tempo}\n"
      f"Distância Pecorrida: {distancia}\n"
      f"Quantidade de Litros: {litros:.2f}")
