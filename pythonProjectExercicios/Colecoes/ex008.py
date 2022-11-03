#8. Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
res = 'SN'
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        print('Adicionado com sucesso.')
        valores.append(valor)
    else:
        print('Esse valor já existe na lista.')
    res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    while res not in 'SN':
        res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    if res in 'N':
        break
valores.sort()
print(f'{"=-" * 30}'
      f'\nO valores digitados em ordem crescente são {valores}')
