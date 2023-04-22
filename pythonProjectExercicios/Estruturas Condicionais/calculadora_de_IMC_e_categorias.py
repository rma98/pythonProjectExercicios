# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
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

# Outras formas de fazer

# 1
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = calcular_imc(peso, altura)
print(f'O IMC dessa pessoa é de {imc:.1f}.')

if imc < 18.5:
    print(f'Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print(f'Parabéns, você está na faixa de peso normal')
elif 25 <= imc < 30:
    print(f'Você está em sobrepeso')
elif 30 <= imc < 40:
    print(f'Você está em obesidade!')
else:
    print(f'Você está em obesidade mórbida, cuidado!')

# 2
peso, altura = [float(input('Digite seu peso: ')), float(input('Digite sua altura: '))]
imc = peso / (altura ** 2)
categorias = ['abaixo do peso normal', 'na faixa de peso normal', 'em sobrepeso', 'em obesidade', 'em obesidade mórbida']

if imc < 18.5:
    categoria = categorias[0]
elif 18.5 <= imc < 25:
    categoria = categorias[1]
elif 25 <= imc < 30:
    categoria = categorias[2]
elif 30 <= imc < 40:
    categoria = categorias[3]
else:
    categoria = categorias[4]

print(f'O IMC dessa pessoa é de {imc:.1f}.')
print(f'Você está {categoria}.')

# 3
peso, altura = float(input('Digite seu peso: ')), float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

categorias = {
    (0, 18.5): 'abaixo do peso normal',
    (18.5, 25): 'na faixa de peso normal',
    (25, 30): 'em sobrepeso',
    (30, 40): 'em obesidade',
    (40, 1000): 'em obesidade mórbida'
}

categoria = None
for faixa, desc in categorias.items():
    if faixa[0] <= imc < faixa[1]:
        categoria = desc

print(f'O IMC dessa pessoa é de {imc:.1f}.')
print(f'Você está {categoria}.')
