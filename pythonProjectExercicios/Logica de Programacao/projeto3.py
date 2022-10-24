# Medidor de Velocidade

'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ela tomou multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir: "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11km a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima."
'''

velocidade_maxia_permitida = 80
velocidade = int(input("Velocidade: "))
if velocidade <= velocidade_maxia_permitida:
  print("Não houve multa!")
elif velocidade > velocidade_maxia_permitida and velocidade <= velocidade_maxia_permitida + 10:
  print("Levou multa leve!")
elif velocidade >= velocidade_maxia_permitida + 11 and velocidade <= velocidade_maxia_permitida + 20:
  print("Levou multa grave!")
elif velocidade > velocidade_maxia_permitida + 20:
  print("Levou multa gravíssima!")
