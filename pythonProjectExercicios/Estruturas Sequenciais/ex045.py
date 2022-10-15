#45. Faça um programa que recebe o valor do salário mínimo e o valor do salário de um funcionário, calcule e mostre a
# quantidade de salários mínimos que esse funcionário ganha.

salario_Minino = float(input("Salário Mínimo: R$"))
salario_Funcionario = float(input("Salário do Funcionário: R$"))
print(f"Quantidade de salários mínimos: R${salario_Funcionario / salario_Minino:.2f}")
