# Faça um programa que leia o ano de nascimento de um jovem e informe. de acordo com sua idade:
# - Se ela ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
# Seu programa também deve mostrar tempo que falta ou que passou do prazo.

from datetime import date

ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
sexo = int(input('Informe seu sexo\n1- MASCULINO\n2-Feminino\n:'))
idade = date.today().year - ano_de_nascimento
print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos em {date.today().year}.')
if sexo == 1:
    if idade == 18:
        print(f'Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        ano = date.today().year + saldo
        print(f'Ainda faltam {saldo} anos para o alistamento.'
              f'\nSeu alistamento será em {ano}.')
    else:
        saldo = idade - 18
        ano = date.today().year - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos.'
              f'\nSeu alistamento foi em {ano}.')
elif sexo == 2:
    print('MULHERES NÃO SÃO OBRIGATÓRIAS FAZER O ALISTAMENTO MILITAR NO BRASIL!')
else:
    print('SEXO INVÁLIDO!')

# Outras formas de fazer

# 1
from datetime import date

ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
sexo = input('Informe seu sexo (M/F): ').upper()
idade = date.today().year - ano_de_nascimento
print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos em {date.today().year}.')

if sexo == 'M':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        ano = date.today().year + saldo
        print(f'Ainda faltam {saldo} anos para o alistamento.'
              f'\nSeu alistamento será em {ano}.')
    else:
        saldo = idade - 18
        ano = date.today().year - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos.'
              f'\nSeu alistamento foi em {ano}.')
elif sexo == 'F':
    print('Mulheres não são obrigadas a se alistar no Brasil.')
else:
    print('Sexo inválido.')

# 2
from datetime import date

ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
sexo = input('Informe seu sexo (M/F): ').upper()
idade = date.today().year - ano_de_nascimento
print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos em {date.today().year}.')

mensagens = {
    'M': {
        18: 'Você tem que se alistar IMEDIATAMENTE!',
        -1: 'Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.',
        1: 'Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'
    },
    'F': {
        18: 'Mulheres não são obrigadas a se alistar no Brasil.'
    }
}

if sexo in mensagens:
    diferenca = idade - 18
    mensagem = mensagens[sexo].get(diferenca, '')
    if mensagem:
        if diferenca > 0:
            ano = date.today().year - diferenca
        else:
            ano = date.today().year + abs(diferenca)
        print(mensagem.format(abs(diferenca), ano))
else:
    print('Sexo inválido.')
