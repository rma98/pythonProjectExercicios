#16. Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print(f'''
{"-" * 20}
{"JOGA NA MEGA SENA":^20}
{"-" * 20}
''')
lista = []
jogos = []
qtde = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtde:
    cont= 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 3, f'SORTEANDO {qtde} jogos', '-=' * 3)
for indice, list in enumerate(jogos):
    print(f'Jogo {indice + 1}: {list}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
