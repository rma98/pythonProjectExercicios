#5. Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> -> 5 -> 8

#Utilizando a estrutura FOR
print(f'{"=" *32}\n10 PRIMEIROS TERMOS DE UMA PA\n{"=" *32}')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end=" -> ")
print('FIM')

# Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão. Pergunte ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> -> 5 -> 8

#Utilizando a estrutura WHILE
print(f'\033[34m{"-=" *10}\033[m'
      f'\n\033[1mGERADOR DE PA'
      f'\n\033[34m{"-=" *10}\033[m')
prim_termo = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = prim_termo
cont = 1
tot = 0
mais = 10
while mais != 0:
      tot += mais
      while cont <= tot:
            print(f'{termo} -> ', end="")
            termo += r
            cont += 1
      print('PAUSA!')
      mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!')
print(f'Progressão finalizada com {tot} termos mostrados.')
