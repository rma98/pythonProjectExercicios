# Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão. Pergunte ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> -> 5 -> 8

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

# Outras formas de fazer

print('\033[34m', '-=' * 10, '\033[m')
print('\033[1mGERADOR DE PA\033[m')
print('\033[34m', '-=' * 10, '\033[m')
prim_termo = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n_termos = int(input('Quantidade de termos: '))
for i in range(prim_termo, prim_termo + (n_termos * r), r):
    print(i, end=' -> ')
print('FIM!')
