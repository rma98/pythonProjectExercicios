#23. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_do_funcionario = float(input('Salário do Funcionário: R$'))
if salario_do_funcionario > 1250:
    salario_do_funcionario += salario_do_funcionario * 10/100
    print(f'Salário do funcionário com um aumento de 10%: R${salario_do_funcionario:.2f}')
else:
    salario_do_funcionario += salario_do_funcionario * 15/100
    print(f'Salário do funcionário com um aumento de 15%: R${salario_do_funcionario:.2f}')
