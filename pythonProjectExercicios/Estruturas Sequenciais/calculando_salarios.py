# Faça um programa que recebe o valor do salário-mínimo e o valor do salário de um funcionário, calcule e mostre a
# quantidade de salários-mínimos que esse funcionário ganha.

salario_Minino = float(input("Salário Mínimo: R$"))
salario_Funcionario = float(input("Salário do Funcionário: R$"))
print(f"Quantidade de salários mínimos: R${salario_Funcionario / salario_Minino:.2f}")

# Outras formas de fazer

# 1
salario_minimo = float(input("Digite o salário mínimo: R$"))
salario_funcionario = float(input("Digite o salário do funcionário: R$"))
quantidade_salarios_minimos = salario_funcionario / salario_minimo
print("O funcionário ganha {:.2f} salários mínimos".format(quantidade_salarios_minimos))

# 2
salario_minimo = float(input("Digite o salário mínimo: R$"))
salario_funcionario = float(input("Digite o salário do funcionário: R$"))
quantidade_salarios_minimos = salario_funcionario / salario_minimo
print(f"O funcionário ganha {quantidade_salarios_minimos:.2f} salários mínimos")
