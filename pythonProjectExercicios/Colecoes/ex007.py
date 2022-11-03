#7. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

valores = list()
maior = 0
menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v + 1}º valor na posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'{"=-" * 30}')
print(f'Você digitou os números {valores}')
print(f'O maior valor é {maior} nas posições', end=' ')
for pos, valor in enumerate(valores):
    if valores[pos] == maior:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor é {menor} nas posições', end=' ')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}...', end=' ')
#print(f'O maior valor é {max(valores)}')
#print(f'O menor valor é {min(valores)}')
