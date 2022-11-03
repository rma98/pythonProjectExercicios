# Uma empresa de ônibus tem saídas diárias de Palmares para outras cidades de Pernambuco, conforme a tabela de preços a
# seguir:
# Escreva um programa que exiba na tela a lista de destinos disponíveis, com o valor da passagem e em seguida receba
# como entrada do usuário o código do destino escolhido e a quantia em dinheiro recebida do passageiro. Se o dinheiro
# recebido for insuficiente, imprima uma mensagem de erro e finalize o programa. Caso contrário, calcuole o troco e
# imprima na tela o destino escolhido, o valor da passagem e o valor do troco.
# Obs: O valor digitado pelo o usuário deve estar no intervalo [1-6]. Se for digitado um código fora deste limite, emita
# mensagem de erro e encerre o processamento.

print(f'''
\033[7;33;40m{"=" *50}\033[m
\033[7;30;43m{"EMPRESA DE ÔNIBUS - PALMARES":^50}\033[m
\033[7;33;40m{"=" *50}\033[m
\033[7;30;43m{"TABELA DE PREÇOS":^50}\033[m
\033[7;33;40m{"CÓDIGO":^10} {"DESTINO":^23} {"TARIFA (R$)":^15}\033[m
\033[7;30;43m{"1":^10} {"RECIFE":^23} {"R$226,30":^15}\033[m
\033[7;33;40m{"2":^10} {"ARCOVERDE":^23} {"R$37,00":^15}\033[m
\033[7;30;43m{"3":^10} {"GARANHUNS":^23} {"R$164,22":^15}\033[m
\033[7;33;40m{"4":^10} {"PESQUEIRA":^23} {"R$150,14":^15}\033[m
\033[7;30;43m{"5":^10} {"BELO JARDIM":^23} {"R$200,00":^15}\033[m
\033[7;33;40m{"6":^10} {"PETROLINA":^23} {"R$320,58":^15}\033[m
''')
qtde_de_dinheiro_do_passageiro = float(input('Informe o seu saldo: R$'))
codigo = int(input('Digite o código: '))
if codigo == 1:
    valor_da_passagem = 226.30
    if qtde_de_dinheiro_do_passageiro < valor_da_passagem:
        print('\033[31mSALDO INSUFICIENTE!\033[m')
    else:
        print(f'\033[34mDESTINO ESCOLHIDO RECIFE!\033[m'
              f'\nValor da passagem: \033[32mR${valor_da_passagem:.2f}\033[m'
              f'\nSaldo do Passageiro: \033[32mR${qtde_de_dinheiro_do_passageiro:.2f}\033[m'
              f'\nTroco: \033[31mR${qtde_de_dinheiro_do_passageiro - valor_da_passagem:.2f}\033[m')
elif codigo == 2:
    valor_da_passagem = 37
    if qtde_de_dinheiro_do_passageiro < valor_da_passagem:
        print('\033[31mSALDO INSUFICIENTE!\033[m')
    else:
        print(f'\033[34mDESTINO ESCOLHIDO ARCOVERDE!\033[m'
              f'\nValor da passagem: \033[32mR${valor_da_passagem:.2f}\033[m'
              f'\nSaldo do Passageiro: \033[32mR${qtde_de_dinheiro_do_passageiro:.2f}\033[m'
              f'\nTroco: \033[31mR${qtde_de_dinheiro_do_passageiro - valor_da_passagem:.2f}\033[m')
elif codigo == 3:
    valor_da_passagem = 164.22
    if qtde_de_dinheiro_do_passageiro < valor_da_passagem:
        print('\033[31mSALDO INSUFICIENTE!\033[m')
    else:
        print(f'\033[34mDESTINO ESCOLHIDO GARANHUNS!\033[m'
              f'\nValor da passagem: \033[32mR${valor_da_passagem:.2f}\033[m'
              f'\nSaldo do Passageiro: \033[32mR${qtde_de_dinheiro_do_passageiro:.2f}\033[m'
              f'\nTroco: \033[31mR${qtde_de_dinheiro_do_passageiro - valor_da_passagem:.2f}\033[m')
elif codigo == 4:
    valor_da_passagem = 150.14
    if qtde_de_dinheiro_do_passageiro < valor_da_passagem:
        print('\033[31mSALDO INSUFICIENTE!\033[m')
    else:
        print(f'\033[34mDESTINO ESCOLHIDO PESQUEIRA!\033[m'
              f'\nValor da passagem: \033[32mR${valor_da_passagem:.2f}\033[m'
              f'\nSaldo do Passageiro: \033[32mR${qtde_de_dinheiro_do_passageiro:.2f}\033[m'
              f'\nTroco: \033[31mR${qtde_de_dinheiro_do_passageiro - valor_da_passagem:.2f}\033[m')
elif codigo == 5:
    valor_da_passagem = 200
    if qtde_de_dinheiro_do_passageiro < valor_da_passagem:
        print('\033[31mSALDO INSUFICIENTE!\033[m')
    else:
        print(f'\033[34mDESTINO ESCOLHIDO BELO JARDIM!\033[m'
              f'\nValor da passagem: \033[32mR${valor_da_passagem:.2f}\033[m'
              f'\nSaldo do Passageiro: \033[32mR${qtde_de_dinheiro_do_passageiro:.2f}\033[m'
              f'\nTroco: \033[31mR${qtde_de_dinheiro_do_passageiro - valor_da_passagem:.2f}\033[m')
elif codigo == 6:
    valor_da_passagem = 320.58
    if qtde_de_dinheiro_do_passageiro < valor_da_passagem:
        print('\033[31mSALDO INSUFICIENTE!\033[m')
    else:
        print(f'\033[34mDESTINO ESCOLHIDO PETROLINA!\033[m'
              f'\nValor da passagem: \033[32mR${valor_da_passagem:.2f}\033[m'
              f'\nSaldo do Passageiro: \033[32mR${qtde_de_dinheiro_do_passageiro:.2f}\033[m'
              f'\nTroco: \033[31mR${qtde_de_dinheiro_do_passageiro - valor_da_passagem:.2f}\033[m')
else:
    print('\033[31mCÓDIGO INVÁLIDO!\033[m')
