#30. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}.')
if imc < 18.5:
    print(f'\033[31mVocê está ABAIXO DO PESO normal\033[m')
elif 18.5 <= imc < 25:
    print(f'\033[32mPARABÉNS, você está na faixa de PESO NORMAL\033[m')
elif 25 <= imc < 30:
    print(f'\033[33mVocê está em SOBREPESO\033[m')
elif 30 <= imc < 40:
    print(f'\033[34mVocê está em OBESIDADE!\033[m')
else:
    print(f'\033[35mVocê está em OBESIDADE MÓRBIDA, cuidado!\033[m')
