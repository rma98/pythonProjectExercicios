#15. Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a
# matriz na tela, com a formatação correta.
# Aprimorando o desafio:
# a -> A soma de todos os valores pares digitados.
# b -> A soma dos valores da terceira coluna.
# c -> O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]: '))
print(f'{"=-" * 30}')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print(f'{"=-" * 30}')
print(f'A soma dos valores pares é {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print( f'A soma dos valores da terceira coluna é {scol}')
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}')
