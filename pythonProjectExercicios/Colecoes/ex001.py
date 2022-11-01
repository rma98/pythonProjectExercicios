#1. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem po extenso, de zero até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.

cont_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                    'doze', 'treze', 'quartoze', 'quimze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

res = 'S'
while res == 'S':
    n = int(input('\033[32mDigite um número entre 0 e 20: \033[m'))
    if 0 <= n <= 20:
        print(f'\033[33mVocê digitou o número {cont_por_extenso[n]}.\033[m')
    else:
        print(f'\033[31mNúmero Inválido. \033[m')
    res = input('\033[34mVocê deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: \033[m').strip().upper()[0]
    while res not in 'SN':
        res = input('\033[34mVocê deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: \033[m').strip().upper()[0]
    if res == 'N':
        break
