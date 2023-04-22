# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
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

# Outras formas de fazer

# 1
from datetime import datetime

ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.now().year - ano_de_nascimento
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

# 2
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_de_nascimento
print(f'O atleta tem \033[36m{idade}\033[m anos.')

classificacoes = {9: ('\033[1;31mMIRIM\033[m', 'vermelho em negrito'),
                  14: ('\033[4;32mINFANTIL\033[m', 'verde sublinhado'),
                  19: ('\033[33mJÚNIOR\033[m', 'amarelo'),
                  25: ('\033[34mSÊNIOR\033[m', 'azul'),
                  float('inf'): ('\033[35mMASTER\033[m', 'magenta')}

for idade_limite, (classificacao, cor) in classificacoes.items():
    if idade <= idade_limite:
        print(f'Classificação: {classificacao} ({cor})')
        break

# 3
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_de_nascimento
print(f'O atleta tem \033[36m{idade}\033[m anos.')

def obter_classificacao(idade):
    if idade <= 9:
        return '\033[1;31mMIRIM\033[m (vermelho em negrito)'
    elif idade <= 14:
        return '\033[4;32mINFANTIL\033[m (verde sublinhado)'
    elif idade <= 19:
        return '\033[33mJÚNIOR\033[m (amarelo)'
    elif idade <= 25:
        return '\033[34mSÊNIOR\033[m (azul)'
    else:
        return '\033[35mMASTER\033[m (magenta)'

classificacao = obter_classificacao(idade)
print(f'Classificação: {classificacao}')
