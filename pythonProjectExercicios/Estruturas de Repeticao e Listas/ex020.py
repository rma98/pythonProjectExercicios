#20. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vítorias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0
while True:
      print(f'{"-=" * 13}'
            f'\nVAMOS JOGAR PAR OU ÍMPAR'
            f'\n{"-=" * 13}')
      jogador = int(input('Digite um valor: '))
      computador = randint(0, 10)
      total = jogador + computador
      tipo = ' '
      while tipo not in 'PI':
            tipo = input('PAR OU ÍMPAR | \"P\" OU \"I\": ').strip().upper()
      print(f'Você jopgou {jogador} e o computador {computador}. Total de {total}. ', end='')
      print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
      if tipo == 'P':
            if total % 2 == 0:
                  print('VOCÊ VEMCEU!')
                  v += 1
            else:
                  print('VOCÊ PERDEU!')
                  break
      elif tipo == 'I':
            if total % 2 == 0:
                  print('VOCÊ VEMCEU!')
                  v += 1
            else:
                  print('VOCÊ PERDEU!')
                  break
      print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
