#27. Baseado no mês, na idade (inteiro) e no salário (real) que o usuário informe, o algoritmo deve mostrar se é ou não
# obrigatório a contribuição ao sindicato e o valor que deve ser pago. Para contribuir com o sindicato, o contribuinte
# deve ter mais de 25 anos, ganhar mais de R$1345.80 e estar no mês de maio.
# -> O valor da contribuição é de 3.96 do valor do salário.

idade = int(input("Idade: "))
salario = float(input("Salário: "))
mes = input("MêS: ").lower()
if idade > 25 and salario > 1345.80 and mes == "maio":
    porcento = 3.96/100
    desconto = salario * porcento
    novo_Salario = salario - desconto
    print(f"É obrigatório!\n{novo_Salario:.2f}")
else:
    print("Não é obrigatório!")
