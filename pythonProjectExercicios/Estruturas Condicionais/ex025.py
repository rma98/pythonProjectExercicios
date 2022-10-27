#25. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela,
# não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input('Qual é o valor da casa? R$'))
salario_do_comprador = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos vai ser pago? '))
prestacao = valor_da_casa / (anos * 12)
minimo = salario_do_comprador * 30 / 100
print(f'Para pagar uma casa de \033[32mR${valor_da_casa:.2f}\033[m em \033[33m{anos}\033[m anos, a prestação será de '
      f'\033[31mR${prestacao:.2f}\033[m\n')
if prestacao <= minimo:
    print(f'\033[34mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print(f'\033[35mEmpréstimo NEGADO!\033[m')
