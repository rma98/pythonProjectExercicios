#20. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano da contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = dict()

dados['nome'] = input('Nome: ')
ano_nasc = int(input('Ano de Nascimento: '))
atual = date.today().year
dados['idade'] = atual - ano_nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contrataçaõ: '))
    dados['salário'] = float(input('Ano de Contrataçaõ: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - atual)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
