#11. Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas que vão contar
# apenas os valores pares e os valores ímpares digitados, respectivamente. No final, mostre o conteúdo das três listas geradas.

valores = []
pares = []
impares = []
res = ''
while True:
    valores.append(int(input('Digite um número: ')))
    res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    while res not in 'SN':
        res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    if res == 'N':
        break
for pos, valor in enumerate(valores):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'{"=-" * 30}'
      f'\nA lista completa é {valores}'
      f'\nA lista de pares é {pares}'
      f'\nA lista de ímpares é {impares}')
