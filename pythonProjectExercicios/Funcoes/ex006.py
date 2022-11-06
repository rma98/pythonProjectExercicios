#6. Crie um programa que tenha uma função chamada voto() que vai receber o ano de nascimento de uma pessoa, retornando
# um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições.


def voto(ano_nasc=0):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano_nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


ano = int(input('Ano de Nascimento: '))
print(voto(ano))
