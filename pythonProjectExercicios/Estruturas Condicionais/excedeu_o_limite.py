# Escreva um programa que leia a velocidade de um carro. Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

velocidade_do_carro = float(input('Velocidade: '))
if velocidade_do_carro > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h\n'
          f'Você deve pagar uma multa de R${(velocidade_do_carro - 80) * 7:.2f}')
print('Tenha um Bom-dia! Dirija com segurança!')

# Outras formas de fazer

# 1
velocidade_do_carro = float(input('Velocidade: '))

if velocidade_do_carro > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h\n'
          f'Você deve pagar uma multa de R${(velocidade_do_carro - 80) * 7:.2f}')
else:
    print('Parabéns, você não foi multado!')
    
print('Tenha um bom dia! Dirija com segurança!')

# 2
try:
    velocidade_do_carro = float(input('Velocidade: '))
    if velocidade_do_carro > 80:
        print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h\n'
              f'Você deve pagar uma multa de R${(velocidade_do_carro - 80) * 7:.2f}')
    else:
        print('Parabéns, você não foi multado!')
except ValueError:
    print('Valor inválido! Digite um número válido para a velocidade.')

print('Tenha um bom dia! Dirija com segurança!')
