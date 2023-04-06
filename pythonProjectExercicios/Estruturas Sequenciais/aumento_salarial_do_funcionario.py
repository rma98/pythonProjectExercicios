# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_do_funcionario = float(input('Salário do funcionário: R$'))
aumento = salario_do_funcionario * 15/100
salario_do_funcionario += aumento
print(f'O novo salário do funcionário com 15% de aumento é de: R${salario_do_funcionario:.2f}')

# Outras formas de fazer

# 1
SALARIO_INICIAL = float(input('Salário do funcionário: R$'))
AUMENTO_PERCENTUAL = 0.15
aumento = SALARIO_INICIAL * AUMENTO_PERCENTUAL
salario_final = SALARIO_INICIAL + aumento
print(f'O novo salário do funcionário com 15% de aumento é de: R${salario_final:.2f}')

# 2
salario_do_funcionario = float(input('Salário do funcionário: R$'))
aumento = salario_do_funcionario * 0.15
salario_do_funcionario += aumento
novo_salario = round(salario_do_funcionario, 2)
print(f'O novo salário do funcionário com 15% de aumento é de: R${novo_salario}')

# 3
salario_do_funcionario = float(input('Salário do funcionário: R$'))
percentual_aumento = float(input('Percentual de aumento: '))
aumento = salario_do_funcionario * (percentual_aumento / 100)
salario_do_funcionario += aumento
print(f'O novo salário do funcionário com {percentual_aumento}% de aumento é de: R${salario_do_funcionario:.2f}')
