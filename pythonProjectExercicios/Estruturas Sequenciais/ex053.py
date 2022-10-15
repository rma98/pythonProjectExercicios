#53. Um prêmio em dinheiro será dividido entre três ganhadores de um concurso.
# - O primeiro ganhador receberá 46% do valor total do prêmio
# - O segundo ganhador receberá 32% do valor total do prêmio
# - O terceiro receberá o restante
# Escreva um programa que defina uma variável com o valor para o prêmio e, em seguida, calcule e imprima a quantia que
# deve ser distribuída para cada um dos ganhandores.

premio = float(input("Prêmio: R$"))
primeiro_Lugar = premio * 46/100
segundo_Lugar = premio * 32/100
terceiro_Lugar = premio * 22/100
print(f"Prêmio do primeiro ganhador: R${primeiro_Lugar:.2f}\nPrêmio do segundo ganhandor: R${segundo_Lugar:.2f}"
      f"\nPrêmio do terceiro ganhandor: R${terceiro_Lugar:.2f}")
