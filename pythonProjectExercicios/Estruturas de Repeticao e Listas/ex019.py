#19. Faça um programa que mostre a tabuada de vários números, um de cada fez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

n = -999
while n < 0:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    print(f'{"-=" * 8}'
          f'\nTABUADA DE {num}'
          f'\n{"-=" * 8}')
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
    print(f'{"-=" * 8}')
print(f'{"=" * 17}'
      f'\nFIM DO PROGRAMA!'
      f'\n{"=" * 17}')
