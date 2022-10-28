#13. Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

soma, produto, maior = 0, 1, 0
n1 = int(input('\033[34mPrimeiro número: \033[m'))
n2 = int(input('\033[31mSegundo número: \033[m'))
opcao = 0
while opcao != 5:
    print(f'''
    \033[7;30;43m{" " * 9}MENU{" " * 10}\033[m
    \033[7;33;40m[1] somar{" " * 14}\033[m
    \033[7;30;43m[2] multiplicar{" " * 8}\033[m
    \033[7;33;40m[3] maior{" " * 14}\033[m
    \033[7;30;43m[4] novos números{" " * 6}\033[m
    \033[7;33;40m[5] sair do programa{" " * 3}\033[m
    ''')
    opcao = int(input('Escolha uma das opções acima: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma do valores digitados acima é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'A multiplicação dos valores digitados acima é {produto}')
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior número do valores digitados acima é {maior}')
    elif opcao == 4:
        n1 = int(input('Novo número: '))
        n2 = int(input('Novo número: '))
    elif opcao > 5:
        print('OPÇÃO INVÁLIDA!')
print('Você saiu do programa.')
