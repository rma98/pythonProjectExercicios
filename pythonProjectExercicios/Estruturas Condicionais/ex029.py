#29. A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# -> Até 9 anos: MIRIM
# -> Até 14 anos: INFANTIL
# -> Até 19 anos: JÍNOR
# -> Até 20 anos: SÊMIOR
# -> Acima: MASTER

from datetime import date

ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_de_nascimento
print(f'O atleta tem \033[36m{idade}\033[m anos.')
if idade <= 9:
    print('\033[1;31mClassificação: MIRIM\033[m')
elif idade <= 14:
    print('\033[4;32mClassificação: INFANTIL\033[m')
elif idade <= 19:
    print('\033[33mClassificação: JÚNIOR\033[m')
elif idade <= 25:
    print('\033[34mClassificação: SÊNIOR\033[m')
else:
    print('\033[35mClassificação: MASTER\033[m')
