#21. Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# a -> quantas pessoas tem mais de 18 anos.
# b -> quantos homens foram cadastrados.
# c -> quantas mulheres tem menos de 20 anos.

res = 'S'
p = tot_p_maiores18 = p_homens = p_mulheres = 0
while res == 'S':
    print(f'{"-" * 20}'
          f'\nCADASTRO DE PESSOAS'
          f'\n{"-" * 20}')
    idade = int(input('Digite a idade: '))
    sexo = input('Informe o sexo \"M\" para MASCULINO e \"F\" para FEMININO: \n').strip().upper()[0]
    while sexo not in 'MF':
        print('Você digitou errado. Tente novamente.')
        sexo = input('Informe o sexo \"M\" para MASCULINO e \"F\" para FEMININO: \n').strip().upper()[0]
    p += 1
    print(f'\033[32m{p}º PESSOA CADASTRADA\033[m')
    if idade > 18:
        tot_p_maiores18 += 1
    if sexo in 'M':
        p_homens += 1
    if sexo in 'F' and idade < 20:
        p_mulheres += 1
    res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
    while res not in 'SN':
        res = input('Você deseja continuar? Aperte \"S\" para SIM ou \"N\" para NÃO: ').strip().upper()[0]
print(f'{"-" * 20}'
      f'\n\033[31mFIM DO PROGRAMA!\033[m'
      f'\n{"-" * 20}'
      f'\n\033[33m{tot_p_maiores18} pessoas são maiores de 18 anos.\033[m'
      f'\n\033[34m{p_homens} pessoas são homens.\033[m'
      f'\n\033[35m{p_mulheres} mulheres tem menos de 20 anos.\033[m')
