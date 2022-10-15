#24. Baseado na idade (inteiro) e no salário (real) que o usuário informe deve mostrar se é ou não obrigatório e o
# pagamento do imposto e o valor do imposto que deve ser pago.
# -> Paga pagar impostos, o contribuinte deve ter mais de 18 anos e ganhar mais de R$1.903,98.
# -> O valor do imposto devido é de 9,85% do valor do salário.

idade = int(input("Idade: "))
salario = float(input("Salário: "))
if idade > 18 and salario > 1903.98:
    porcento = 9.85/100
    imposto = salario * porcento
    novo_Salario = salario - imposto
    print(f"É obrigatório o pagamento do imposto!\nNovo Salário: R${novo_Salario:.2f}")
else:
    print("Não é obrigatório o pagamento do imposto!")
