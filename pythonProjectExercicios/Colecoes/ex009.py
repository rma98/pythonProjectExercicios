#9. Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = list()
for v in range(1, 6):
    valor = int(input(f'Digite o {v}º valor: '))
    if v == 1 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'{"=-" * 30}'
      f'\nO valores digitados em ordem foram {valores}')
