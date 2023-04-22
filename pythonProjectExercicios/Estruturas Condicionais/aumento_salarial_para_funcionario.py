# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_do_funcionario = float(input('Salário do Funcionário: R$'))
if salario_do_funcionario > 1250:
    salario_do_funcionario += salario_do_funcionario * 10/100
    print(f'Salário do funcionário com um aumento de 10%: R${salario_do_funcionario:.2f}')
else:
    salario_do_funcionario += salario_do_funcionario * 15/100
    print(f'Salário do funcionário com um aumento de 15%: R${salario_do_funcionario:.2f}')

# Outras formas de fazer

# 1
salario_do_funcionario = float(input('Salário do Funcionário: R$'))
aumento = salario_do_funcionario * 0.1 if salario_do_funcionario > 1250 else salario_do_funcionario * 0.15
novo_salario = salario_do_funcionario + aumento
print(f'Salário do funcionário com um aumento de {aumento*100/salario_do_funcionario:.0f}%: R${novo_salario:.2f}')

# 2
def calcular_aumento(salario):
    if salario > 1250:
        return salario * 0.1
    else:
        return salario * 0.15

salario_do_funcionario = float(input('Salário do Funcionário: R$'))
aumento = calcular_aumento(salario_do_funcionario)
novo_salario = salario_do_funcionario + aumento
print(f'Salário do funcionário com um aumento de {aumento*100/salario_do_funcionario:.0f}%: R${novo_salario:.2f}')
