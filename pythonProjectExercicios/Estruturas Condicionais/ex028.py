#28. Faça um programa que leia o ano de nascimento de um jovem e informe. de acordo com sua idade:
# - Se ela ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
# Seu programa também deve mostrar tempo que falta ou que passou do prazo

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
