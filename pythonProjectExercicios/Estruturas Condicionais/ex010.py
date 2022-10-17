#10. Baseado no mês, na idade (inteiro) e no salário (real) que o usuário informe, o algoritmo deve mostrar se é ou não
# obrigatório a contribuição ao sindicato e o valor que deve ser pago. Para contribuir com o sindicato, o contribuinte
# deve ter mais de 25 anos, ganhar mais de R$1345.80 e estar no mês de maio.
# -> O valor da contribuição é de 3.96% do valor do salário.

idade = int(input("Idade: "))
salario = float(input("Salário: R$"))
if idade > 25 and salario > 1345.80:
    porcento = 3.96/100
    contribuicao = salario * porcento
    salario -= contribuicao
    print(f"É obrigatório!\nContribuição: R${contribuicao:.2f}\nSalário: R${salario:.2f}")
else:
    print(f"Não é obrigatório!\nSalário: R${salario:.2f}")
