# Um prêmio em dinheiro será dividido entre três ganhadores de um concurso.
# - O primeiro ganhador receberá 46% do valor total do prêmio
# - O segundo ganhador receberá 32% do valor total do prêmio
# - O terceiro receberá o restante
# Escreva um programa que defina uma variável com o valor para o prêmio e, em seguida, calcule e imprima a quantia que
# deve ser distribuída para cada um dos ganhadores.

premio = float(input("Prêmio: R$"))
primeiro_Lugar = premio * 46/100
segundo_Lugar = premio * 32/100
terceiro_Lugar = premio * 22/100
print(f"Prêmio do primeiro ganhador: R${primeiro_Lugar:.2f}\nPrêmio do segundo ganhador: R${segundo_Lugar:.2f}"
      f"\nPrêmio do terceiro ganhador: R${terceiro_Lugar:.2f}")

# Outras formas de fazer

# 1
porcentagens = [0.46, 0.32, 0.22]
premio = float(input("Prêmio: R$"))
vencedores = []

for i, porcentagem in enumerate(porcentagens):
    valor = porcentagem * premio
    vencedores.append(valor)
    print(f"Prêmio do {i+1}º ganhador: R${valor:.2f}")

# 2
porcentagens = [0.46, 0.32, 0.22]
premio = float(input("Prêmio: R$"))
vencedores = [porcentagem * premio for porcentagem in porcentagens]

for i, valor in enumerate(vencedores):
    print(f"Prêmio do {i+1}º ganhador: R${valor:.2f}")

