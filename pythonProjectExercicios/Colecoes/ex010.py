#10. Crie um programa que vai ler vários números e colocar em uma lista. Depos disso, mostre:
# a -> Quantos números foram digitados.
# b -> A lista de valores ordenada de forma descrecente.
# c -> Se o valor 5 foi digitado e está ou não na lista.

valores = list()
res = ''
while True:
    valores.append(int(input('Digite um valor: ')))
    res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    while res not in 'SN':
        res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    if res == 'N':
        break
valores.sort(reverse=True)
print(f'{"=-" * 30}'
      f'\nVocê digitou {len(valores)} elementos.'
      f'\nO valores em ordem descrecente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
